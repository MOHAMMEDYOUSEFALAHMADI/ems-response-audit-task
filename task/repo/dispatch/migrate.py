"""Map raw CSV rows (schema v1 or v2) to the canonical Incident model.

Schema v2 went live 2025-07-01 (see docs/SCHEMA_CHANGELOG.md).
"""

from __future__ import annotations

from datetime import datetime

from .models import DISTRICT_BY_NAME, RIYADH, Incident

# v1 column -> v2 column, used to read v2 rows through the v1 code path
V2_FIELD_MAP = {
    "call_received_at": "dispatched_at",
    "unit_dispatched_at": "dispatched_at",
    "unit_arrived_at": "on_scene_at",
}


def detect_version(header: list[str]) -> int:
    return 2 if "schema_version" in header else 1


def _parse_v1(ts: str) -> datetime:
    return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S").replace(tzinfo=RIYADH)


def _parse_v2(ts: str) -> datetime:
    return datetime.strptime(ts.rstrip("Z"), "%Y-%m-%dT%H:%M:%S").replace(tzinfo=RIYADH)


def from_v1(row: dict) -> Incident:
    return Incident(
        incident_id=row["incident_id"],
        call_at=_parse_v1(row["call_received_at"]),
        dispatched_at=_parse_v1(row["unit_dispatched_at"]),
        on_scene_at=_parse_v1(row["unit_arrived_at"]),
        district_code=DISTRICT_BY_NAME.get(row["district"].strip(), "UNKNOWN"),
        caller_name=row["caller_name"],
        caller_phone_hash=row["caller_phone_hash"],
        priority=int(row["priority"]),
        hijri_date=row["hijri_date"],
    )


def from_v2(row: dict) -> Incident:
    def get(v1_col):
        return row[V2_FIELD_MAP[v1_col]]

    return Incident(
        incident_id=row["incident_id"],
        call_at=_parse_v2(get("call_received_at")),
        dispatched_at=_parse_v2(get("unit_dispatched_at")),
        on_scene_at=_parse_v2(get("unit_arrived_at")),
        district_code=row["district_code"],
        caller_name=row["caller_name"],
        caller_phone_hash=row["caller_phone_hash"],
        priority=int(row["priority"]),
        hijri_date=row["hijri_date"],
    )

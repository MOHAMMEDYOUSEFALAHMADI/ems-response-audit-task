from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

RIYADH = timezone(timedelta(hours=3))

DISTRICTS = {"OLY": "العليا", "MLZ": "الملز", "NSM": "النسيم", "SWD": "السويدي", "NKH": "النخيل", "RWD": "الروضة"}
DISTRICT_BY_NAME = {v: k for k, v in DISTRICTS.items()}


@dataclass(frozen=True)
class Incident:
    incident_id: str
    call_at: datetime  # timezone-aware; when the call was received/created at the PSAP
    dispatched_at: datetime  # timezone-aware
    on_scene_at: datetime  # timezone-aware
    district_code: str
    caller_name: str
    caller_phone_hash: str
    priority: int
    hijri_date: str

    @property
    def response_seconds(self) -> float:
        return (self.on_scene_at - self.call_at).total_seconds()

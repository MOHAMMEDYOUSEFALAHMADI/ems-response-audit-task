from __future__ import annotations

import csv
from pathlib import Path

from .dedup import deduplicate
from .migrate import detect_version, from_v1, from_v2
from .models import Incident


def read_rows(path: Path) -> tuple[list[str], list[dict]]:
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def load_file(path: str | Path) -> list[Incident]:
    header, rows = read_rows(Path(path))
    conv = from_v2 if detect_version(header) == 2 else from_v1
    return [conv(r) for r in rows]


def load_incidents(data_dir: str | Path) -> list[Incident]:
    """Load every incidents_*.csv in data_dir, canonicalize, and de-duplicate."""
    incidents: list[Incident] = []
    for p in sorted(Path(data_dir).glob("incidents_*.csv")):
        incidents.extend(load_file(p))
    return deduplicate(incidents)

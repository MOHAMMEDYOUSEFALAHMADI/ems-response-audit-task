from __future__ import annotations

from .models import Incident


def deduplicate(incidents: list[Incident]) -> list[Incident]:
    """Remove duplicate incident records (see docs/DATA_DICTIONARY.md)."""
    seen, out = set(), []
    for inc in sorted(incidents, key=lambda i: i.call_at):
        if inc.incident_id in seen:
            continue
        seen.add(inc.incident_id)
        out.append(inc)
    return out

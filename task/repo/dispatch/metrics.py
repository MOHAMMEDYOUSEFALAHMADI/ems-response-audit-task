from __future__ import annotations

import statistics
from collections import defaultdict

from .models import RIYADH, Incident


def month_key(inc: Incident) -> str:
    return inc.call_at.astimezone(RIYADH).strftime("%Y-%m")


def monthly_report(incidents: list[Incident]) -> dict:
    groups: dict[tuple[str, str], list[float]] = defaultdict(list)
    for inc in incidents:
        groups[(month_key(inc), inc.district_code)].append(inc.response_seconds)
    report: dict = {}
    for (month, dist), vals in sorted(groups.items()):
        report.setdefault(month, {})[dist] = {"count": len(vals), "median_response_s": statistics.median(vals)}
    return report

from datetime import datetime
from pathlib import Path

from dispatch.hijri import gregorian_to_hijri
from dispatch.loader import load_incidents
from dispatch.metrics import monthly_report
from dispatch.models import RIYADH, Incident

DATA = Path(__file__).resolve().parent.parent / "data"


def test_hijri_known_date():
    assert gregorian_to_hijri(2025, 3, 1) == (1446, 9, 1)  # 1 Ramadan 1446


def test_loads_both_files():
    incs = load_incidents(DATA)
    assert len(incs) > 2000
    assert {i.call_at.year for i in incs} == {2025}


def test_monthly_report_median():
    def t(m):
        return datetime(2025, 1, 5, 10, m, tzinfo=RIYADH)

    incs = [Incident(str(k), t(0), t(1), t(k), "OLY", "x", "p", 1, "") for k in (5, 10, 20)]
    rep = monthly_report(incs)
    assert rep["2025-01"]["OLY"] == {"count": 3, "median_response_s": 600.0}

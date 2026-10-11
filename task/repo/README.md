# dispatch-analytics (synthetic)

Monthly ambulance response-time reporting for a fictional Riyadh EMS region. **All data is synthetic.**

```bash
python -m dispatch.report data --out report.json   # writes {"months": {"YYYY-MM": {"<district>": {...}}}}
python -m pytest -q
```

| Path | Purpose |
|---|---|
| `dispatch/loader.py` | Reads every `data/incidents_*.csv` and returns canonical `Incident` objects |
| `dispatch/migrate.py` | Maps schema v1 and v2 rows to the canonical model |
| `dispatch/dedup.py` | Duplicate-incident handling |
| `dispatch/metrics.py` | Monthly per-district aggregation |
| `dispatch/hijri.py` | Gregorian to Hijri (tabular) helper |
| `docs/` | Data dictionary and schema changelog (source of truth for definitions) |

Requires Python 3.10+ and the standard library only.

# Task: The response-time KPI that got better overnight

You are a software engineer on the Red Crescent analytics team (synthetic scenario). The repository in `repo/`
produces the monthly response-time report used by regional leadership (`python -m dispatch.report data --out report.json`).

Leadership noticed three things in the 2025 report:
1. From **July 2025** median response times in every district suddenly improved by several minutes, although
   no operational change was made. The CAD schema was migrated mid-year.
2. For **January-June** almost every incident is reported under district `UNKNOWN`, and caller names in the
   loaded data look corrupted.
3. Ops staff believe incident counts for two sandstorm surge days are inflated.

Your job: find the root causes, fix them in the code, and add regression tests. Read `repo/docs/` carefully;
it is the source of truth for definitions.

## Requirements
- Keep the public interfaces working: `dispatch.loader.load_incidents(data_dir)`, the `Incident` dataclass
  fields, and the CLI `python -m dispatch.report <data_dir> --out <file>` with output `{"months": {"YYYY-MM": {"<district_code>": {"count": int, "median_response_s": float}}}}`.
- The fix must work on **any** dataset in the same formats, not just the files in `repo/data/`
  (your code will be run against fresh data). Do not hard-code values or edit the data files.
- Existing tests must still pass. Add tests that would have caught each bug.
- Write `repo/NOTES.md` (max ~1 page): root cause of each issue, how you verified it, and any remaining risks.
- Only the Python standard library is available.

"""CLI: python -m dispatch.report <data_dir> --out report.json"""

from __future__ import annotations

import argparse
import json

from .loader import load_incidents
from .metrics import monthly_report


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("data_dir")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    rep = monthly_report(load_incidents(a.data_dir))
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump({"months": rep}, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()

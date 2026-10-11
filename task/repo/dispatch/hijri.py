"""Gregorian -> Hijri using the tabular Islamic calendar (may differ by +-1 day from Umm al-Qura)."""


def gregorian_to_hijri(y: int, m: int, d: int) -> tuple[int, int, int]:
    a = (14 - m) // 12
    yy, mm = y + 4800 - a, m + 12 * a - 3
    jd = d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045
    l = jd - 1948440 + 10632
    n = (l - 1) // 10631
    l = l - 10631 * n + 354
    j = ((10985 - l) // 5316) * ((50 * l) // 17719) + (l // 5670) * ((43 * l) // 15238)
    l = l - ((30 - j) // 15) * ((17719 * j) // 50) - (j // 16) * ((15238 * j) // 43) + 29
    hm = (24 * l) // 709
    hd = l - (709 * hm) // 24
    return 30 * n + j - 30, hm, hd


def format_hijri(y: int, m: int, d: int) -> str:
    return f"{y:04d}-{m:02d}-{d:02d}"

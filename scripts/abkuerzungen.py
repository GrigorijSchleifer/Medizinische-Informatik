#!/usr/bin/env python3
"""Erzeugt anhang-abkuerzungen.qmd aus abkuerzungen.tsv.

Aufruf aus dem Projektordner:  python3 scripts/abkuerzungen.py
Die Spalte "Modul" wird automatisch aus den Modul-Dateien ermittelt.
Am Ende werden häufige Abkürzungen gemeldet, die im Buch stehen,
aber noch nicht in abkuerzungen.tsv eingetragen sind.
"""
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
CANDIDATE = re.compile(r"(?<![\wÄÖÜäöü-])(?:e|i)?[A-ZÄÖÜ][A-ZÄÖÜ0-9-]+[a-z]?(?![\wÄÖÜäöü])")


def pattern(abbr):
    return re.compile(r"(?<![\wÄÖÜäöü])" + re.escape(abbr) + r"(?![\wÄÖÜäöü])")


def main():
    modules = sorted(ROOT.glob("[0-9][0-9]-*.qmd"))
    texts = [m.read_text(encoding="utf-8") for m in modules]
    rows = [l.split("\t") for l in (ROOT / "abkuerzungen.tsv").read_text(encoding="utf-8").splitlines()[1:] if l.strip()]
    rows.sort(key=lambda r: r[0].lower().lstrip("e") if r[0][:1] == "e" and r[0][1:2].isupper() else r[0].lower())

    known, lines, missing = set(), [], []
    for abbr, full, meaning in rows:
        variants = [v.strip() for v in abbr.split("/")]
        known.update(variants)
        hits = [ROMAN[i] for i, t in enumerate(texts) if any(pattern(v).search(t) for v in variants)]
        if not hits:
            missing.append(abbr)
        lines.append(f"| **{abbr}** | {full} | {meaning} | {', '.join(hits) or '–'} |")

    out = [
        "# Abkürzungsverzeichnis {#abkuerzungen}",
        "",
        "Automatisch erzeugt aus `abkuerzungen.tsv` (`python3 scripts/abkuerzungen.py`) — "
        "nicht von Hand bearbeiten. Spalte *Modul* = Module, in denen die Abkürzung vorkommt.",
        "",
        "| Abkürzung | ausgeschrieben | Bedeutung / Klinik-Beispiel | Modul |",
        "|---|---|---|---|",
        *lines,
        "",
    ]
    (ROOT / "anhang-abkuerzungen.qmd").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(rows)} Abkürzungen → anhang-abkuerzungen.qmd")
    if missing:
        print("Nicht im Buch gefunden:", ", ".join(missing))

    counts = Counter(m for t in texts for m in CANDIDATE.findall(t))
    todo = [f"{a}({n})" for a, n in counts.most_common() if n >= 3 and a not in known and a not in ROMAN]
    print("Im Buch, aber nicht in der Liste (≥ 3×):", " ".join(todo))


if __name__ == "__main__":
    main()

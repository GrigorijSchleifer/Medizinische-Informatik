#!/usr/bin/env python3
"""Erzeugt themen.md: Überblick über alle Abschnitte und Prüfungsfragen des Buchs.

Aufruf aus dem Projektordner:  python3 scripts/themenindex.py
Abschnitte ohne Frage werden als "offen" markiert.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADING = re.compile(r"^(#{1,3})\s+(.*?)\s*(\{[^}]*\})?\s*$")
QUESTION_BLOCK = re.compile(r"^:::\s*\{\.exam-question\}")


def parse(path):
    """Liefert (Kapiteltitel, [(Ebene, Titel, [Fragen])])."""
    chapter, sections = None, []
    in_question, in_code = False, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if QUESTION_BLOCK.match(line):
            in_question = True
            continue
        if in_question:
            if line.startswith(":::"):
                in_question = False
            elif line.strip():
                question = re.sub(r"^Frage:\s*", "", line.strip())
                if sections:
                    sections[-1][2].append(question)
            continue
        m = HEADING.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2)
            if level == 1:
                chapter = title
            else:
                sections.append((level, title, []))
    return chapter, sections


def main():
    files = sorted(ROOT.glob("[0-9][0-9]-*.Rmd"))
    out = ["# Themenindex", "",
           "Automatisch erzeugt mit `python3 scripts/themenindex.py` — nicht von Hand bearbeiten.", ""]
    summary = ["| Modul | Fragen | Offene Abschnitte |", "|---|---|---|"]
    body = []
    for path in files:
        chapter, sections = parse(path)
        # Ein Abschnitt gilt als offen, wenn weder er noch seine Unterabschnitte eine Frage haben.
        n_questions = sum(len(q) for _, _, q in sections)
        is_open = []
        for i, (level, _, questions) in enumerate(sections):
            j, total = i + 1, len(questions)
            while j < len(sections) and sections[j][0] > level:
                total += len(sections[j][2])
                j += 1
            is_open.append(total == 0)
        # Gezählt werden die kleinsten offenen Einheiten (nicht ## und ### doppelt).
        n_open = sum(1 for i, o in enumerate(is_open)
                     if o and not (i + 1 < len(sections) and sections[i + 1][0] > sections[i][0]))
        summary.append(f"| {chapter} | {n_questions} | {n_open} |")
        body += ["", f"## {chapter}", "", f"Datei: `{path.name}`", ""]
        for (level, title, questions), open_ in zip(sections, is_open):
            indent = "" if level == 2 else "  "
            mark = " — **offen**" if open_ else ""
            body.append(f"{indent}- **{title}**{mark}")
            for q in questions:
                body.append(f"{indent}  - {q}")
    out += summary + body
    target = ROOT / "themen.md"
    target.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{target.name} geschrieben ({len(files)} Module).", file=sys.stderr)


if __name__ == "__main__":
    main()

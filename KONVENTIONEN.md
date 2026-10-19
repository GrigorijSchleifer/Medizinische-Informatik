# Konventionen für Inhalte

Gilt für alle, die Inhalte ergänzen — Menschen wie Claude (Terminal, Cloud,
geplante Aufgaben). Wer mit Claude arbeitet, gibt diese Datei als Kontext mit
(z. B. in der lokalen `CLAUDE.md`: `@KONVENTIONEN.md`).

## Vor dem Ergänzen

1. Aktuellen Stand holen (`git pull`).
2. Themenindex erzeugen und lesen: `python3 scripts/themenindex.py` → `themen.md`.
   Ist ein Thema schon abgedeckt, die bestehende Antwort ergänzen statt eine
   zweite Frage dazu anzulegen.
3. Abgelehnte Themenvorschläge stehen in `abgelehnt.md` — nicht erneut vorschlagen.

## Wohin

- Ein Modul = eine Datei (`01-…Rmd` bis `10-…Rmd`), Gliederung nach dem
  (Muster-)Kursbuch der Bundesärztekammer.
- `#` = Modul (nur einmal pro Datei), `##` = Kursbuch-Punkt, `###` = Unterthema.
- Neue Fragen unter den passenden Kursbuch-Punkt; Platzhaltersatz darunter
  löschen, sobald dort eine Frage steht.

## Format einer Frage

```markdown
::: {.exam-question}
Frage: <so formuliert, wie ein Prüfer im Fachgespräch fragen würde>
:::

::: {.exam-answer}
**Antwort:**

<Kernaussage in 2–3 Sätzen, dann Vertiefung als Liste/Tabelle>

Merksatz: <ein Satz zum Behalten>

*(Quelle: …)*
:::
```

## Quellenangabe (Pflicht)

Genau eine dieser Formen, am Ende jeder Antwort:

- `*(Quelle: Kap. N, <Kapiteltitel> — "Medizinische Informatik kompakt".)*`
- `*(Quelle: Curriculum/Allgemeinwissen — <konkrete Quelle, z. B. § 341 SGB V, gematik, BSI>.)*`
- Mischform: `*(Quelle: Kap. N, <Titel>; ergänzt um <was> aus Curriculum/Allgemeinwissen.)*`

Bei Themen, die sich schnell ändern (ePA, TI, E-Rezept, DiGA, KHZG, EHDS,
KI-Verordnung …), einen Stand angeben: `Stand: 10/2026`.

## Inhaltliche Regeln

- Sprache: Deutsch. Fachbegriffe bei Bedarf mit englischem Original.
- Keine wörtlichen Passagen aus "Medizinische Informatik kompakt" oder
  anderen Büchern übernehmen — eigene Formulierungen, Kapitelverweis genügt.
  (Das Buch soll öffentlich online gehen.)
- Keine Patientendaten, keine internen Daten aus Kliniken.
- Lieber eine korrekte kurze Antwort als eine lange unsichere; Unsicheres
  als solches kennzeichnen.

## Arbeitsweise mit Git

- Im Terminal: direkt auf `main`, kleine Commits, vor jeder Sitzung `git pull`.
- Claude in der Cloud / geplante Aufgaben: immer auf einem eigenen
  `claude/…`-Branch, Änderungen kommen nur per Pull Request nach `main`.

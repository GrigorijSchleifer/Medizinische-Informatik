# Medizinische Informatik — Prüfungsvorbereitung

Ein Quarto-Buch (https://quarto.org) mit Fragen & Antworten zur Zusatz-Weiterbildung
"Medizinische Informatik", strukturiert nach dem (Muster-)Kursbuch der
Bundesärztekammer (10 Module).

## Voraussetzungen

- **Quarto** (bringt pandoc mit)
  ```bash
  brew install --cask quarto   # macOS
  ```
- **R** mit den Paketen `rmarkdown` und `knitr` (für den R-Codeblock in Modul VI)

## Buch rendern

Im Projektordner (wo `_quarto.yml` liegt):

```bash
quarto render
```

Erzeugt eine statische HTML-Site im Ordner `_book/`.
Zum Schreiben mit Live-Vorschau: `quarto preview` (lädt bei jedem Speichern neu).

## Lokal ansehen

```bash
cd _book
python3 -m http.server 8000 --bind 127.0.0.1
```

Dann im Browser: <http://127.0.0.1:8000>

(`--bind 127.0.0.1` hält den Server lokal — nicht im Netzwerk erreichbar.)

## Struktur

| Datei | Modul (nach Kursbuch) |
|---|---|
| `01-modul-i-angewandte-informatik.qmd` | I — Angewandte Informatik |
| `02-modul-ii-datenschutz-datensicherheit.qmd` | II — Datenschutz/Datensicherheit |
| `03-modul-iii-statistik-epidemiologie-biometrie.qmd` | III — Statistik/Epidemiologie/Biometrie |
| `04-modul-iv-medizinische-dokumentation.qmd` | IV — Medizinische Dokumentation |
| `05-modul-v-bildverarbeitung-biosignalverarbeitung.qmd` | V — Bildverarbeitung/Biosignalverarbeitung |
| `06-modul-vi-entscheidungsunterstuetzung.qmd` | VI — Entscheidungsunterstützung |
| `07-modul-vii-informations-kommunikationssysteme.qmd` | VII — Informations-/Kommunikationssysteme |
| `08-modul-viii-management-gesundheits-it.qmd` | VIII — Management in der Gesundheits-IT |
| `09-modul-ix-informationsmanagement-klinische-forschung.qmd` | IX — Informationsmanagement/Klin. Datenmanagement/Forschung |
| `10-modul-x-telemedizin-telematik.qmd` | X — Telemedizin und Telematik |

Am Ende jedes Kapitels steht ein Abschnitt **Quellen**: entweder ein
Kapitelverweis auf "Medizinische Informatik kompakt" (De Gruyter, 2015), oder
ein Hinweis, dass die Antwort auf dem Curriculum/Allgemeinwissen basiert
(für Themen, die im Buch von 2015 nicht oder nicht mehr aktuell behandelt sind,
z. B. DSGVO, FHIR).

## Stand: was steht schon im Buch?

```bash
python3 scripts/themenindex.py
```

Erzeugt `themen.md` (nicht im Repo, wird lokal erzeugt): pro Modul die Zahl der
Fragen, alle Abschnitte mit ihren Fragen und eine Markierung **offen** für
Abschnitte, in denen noch keine Frage steht.

## Mitarbeiten

Regeln für neue Inhalte (Format, Quellenangabe, keine wörtlichen Buchzitate)
stehen in [`KONVENTIONEN.md`](KONVENTIONEN.md). Abgelehnte Themenvorschläge
werden in [`abgelehnt.md`](abgelehnt.md) gesammelt.

- Im Terminal wird direkt auf `main` gearbeitet.
- Claude in der Cloud arbeitet auf eigenen `claude/…`-Branches; Änderungen
  kommen nur per Pull Request nach `main`.

## Lizenz

Die Inhalte stehen unter [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.de)
(Namensnennung – Nicht kommerziell – Weitergabe unter gleichen Bedingungen).
Ausgenommen sind gekennzeichnete Inhalte Dritter.

# Medizinische Informatik — Prüfungsvorbereitung

Ein Bookdown-Projekt (R Markdown) mit Fragen & Antworten zur Zusatz-Weiterbildung
"Medizinische Informatik", strukturiert nach dem (Muster-)Kursbuch der
Bundesärztekammer (10 Module).

## Voraussetzungen

- **R** (getestet mit R 4.5)
- R-Pakete: `bookdown`, `servr`
  ```r
  install.packages(c("bookdown", "servr"))
  ```
- **pandoc** (System-Tool, nicht über R installierbar)
  ```bash
  brew install pandoc   # macOS
  ```

## Buch rendern

Im Projektordner (wo `index.Rmd` liegt):

```bash
Rscript -e 'bookdown::render_book(".")'
```

Erzeugt eine statische HTML-Site im Ordner `_book/`.

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
| `01-modul-i-angewandte-informatik.Rmd` | I — Angewandte Informatik |
| `02-modul-ii-datenschutz-datensicherheit.Rmd` | II — Datenschutz/Datensicherheit |
| `03-modul-iii-statistik-epidemiologie-biometrie.Rmd` | III — Statistik/Epidemiologie/Biometrie |
| `04-modul-iv-medizinische-dokumentation.Rmd` | IV — Medizinische Dokumentation |
| `05-modul-v-bildverarbeitung-biosignalverarbeitung.Rmd` | V — Bildverarbeitung/Biosignalverarbeitung |
| `06-modul-vi-entscheidungsunterstuetzung.Rmd` | VI — Entscheidungsunterstützung |
| `07-modul-vii-informations-kommunikationssysteme.Rmd` | VII — Informations-/Kommunikationssysteme |
| `08-modul-viii-management-gesundheits-it.Rmd` | VIII — Management in der Gesundheits-IT |
| `09-modul-ix-informationsmanagement-klinische-forschung.Rmd` | IX — Informationsmanagement/Klin. Datenmanagement/Forschung |
| `10-modul-x-telemedizin-telematik.Rmd` | X — Telemedizin und Telematik |

Jede Frage-Antwort-Box ist mit ihrer Quelle gekennzeichnet: entweder ein
Kapitelverweis auf "Medizinische Informatik kompakt" (De Gruyter, 2015), oder
ein Hinweis, dass die Antwort auf dem Curriculum/Allgemeinwissen basiert
(für Themen, die im Buch von 2015 nicht oder nicht mehr aktuell behandelt sind,
z. B. DSGVO, FHIR).

## Status

Module I–III sind mit Fragen/Antworten gefüllt. Module IV–X sind noch
Platzhalter-Struktur (Curriculum-Gliederung ohne Inhalt).

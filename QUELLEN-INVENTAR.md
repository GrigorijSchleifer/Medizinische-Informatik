# Quellen-Inventar: (Muster-)Kursbuch Medizinische Informatik (BÄK)

Erfasst am 04.11.2026 auf Stand `main` (Commit `98f7813`) mit:

```bash
grep -rn 'Kursbuch' *.qmd
```

**Nur erfasst, nichts geändert.** Auflagen, Jahreszahlen und Seitenzahlen im
Buch bleiben so, wie sie sind. Die Vereinheitlichung entscheidet der Autor,
sobald ihm die 2. Auflage vorliegt.

Stand der Prüfung:

- Verifiziert: Die BÄK listet das Kursbuch als „2. Auflage, Stand: 17./18.02.2022“
  (<https://www.bundesaerztekammer.de/themen/aerzte/aus-fort-und-weiterbildung/weiterbildung/muster-kursbuecher>).
- Verifiziert: Der im Buch verwendete Wortlaut der Lerninhalte stammt aus der
  1. Auflage 2020 (PDF `20200428_MKB-MedInformatik.pdf`).
- **Nicht** verifiziert: ob die 2. Auflage denselben Wortlaut hat, und keine
  einzige Seitenzahl.

## Literaturangaben (mit Auflage, Jahr, Abschnitt oder Seite)

| Datei | Zeile | zitierte Auflage | Jahr | Abschnitt | Seitenzahl | Wortlaut des Zitats |
|---|---|---|---|---|---|---|
| `01-modul-i-angewandte-informatik.qmd` | 155 | 2. Auflage | 2022 | 4.1 | S. 10 | `- Bundesärztekammer: [(Muster-)Kursbuch Medizinische Informatik](https://www.bundesaerztekammer.de/fileadmin/user_upload/BAEK/Themen/Aus-Fort-Weiterbildung/Weiterbildung/Kursbuecher/2018/20220217_18_MKB_MedInformatik.pdf), 2. Auflage, 2022, Abschnitt 4.1, S. 10` |
| `01-modul-i-angewandte-informatik.qmd` | 234 | 2. Auflage | 2022 | 4.1 | S. 10 | `- Bundesärztekammer: [(Muster-)Kursbuch Medizinische Informatik](https://www.bundesaerztekammer.de/fileadmin/user_upload/BAEK/Themen/Aus-Fort-Weiterbildung/Weiterbildung/Kursbuecher/2018/20220217_18_MKB_MedInformatik.pdf), 2. Auflage, 2022, Abschnitt 4.1, S. 10` |
| `09-modul-ix-informationsmanagement-klinische-forschung.qmd` | 325 | — | — | Kap. 2.7 | — | `- Curriculum/Allgemeinwissen — § 630e BGB (Aufklärung), (Muster-)Kursbuch BÄK Kap. 2.7 (Blended Learning/E-Learning)` |
| `anhang-wbo-abgleich.qmd` | 3–4 | 2. Auflage | 2022 | — | — | `Dieses Buch ist nach dem **(Muster-)Kursbuch Medizinische Informatik** der` / `Bundesärztekammer (2. Auflage, 2022) gegliedert. …` (Auflage und Jahr stehen in Zeile 4) |

## Erwähnungen ohne Literaturangabe

Diese Treffer nennen das Kursbuch nur allgemein, ohne Auflage, Jahr, Abschnitt
oder Seite.

| Datei | Zeile | zitierte Auflage | Jahr | Abschnitt | Seitenzahl | Wortlaut des Zitats |
|---|---|---|---|---|---|---|
| `anhang-abkuerzungen.qmd` | 34 | — | — | — | — | `\| **BÄK** \| Bundesärztekammer \| Herausgeberin des (Muster-)Kursbuchs \| IV, VIII, IX \|` |
| `anhang-wbo-abgleich.qmd` | 7 | — | — | — | — | `Kursbuch nicht nennt.` |
| `anhang-wbo-abgleich.qmd` | 20 | — | — | — | — | `Jeder Punkt der WBO-Liste wurde mit den Lerninhalten des Kursbuchs verglichen.` |
| `anhang-wbo-abgleich.qmd` | 26 | — | — | — | — | `## Themen, die im Kursbuch fehlen` |
| `anhang-wbo-abgleich.qmd` | 28 | — | — | — | — | `\| WBO-Bereich \| Thema, das im Kursbuch fehlt \| Stand in diesem Buch \|` |
| `index.qmd` | 19 | — | — | — | — | `des (Muster-)Kursbuchs der Bundesärztekammer — ein Kapitel pro Modul — und ist` |
| `vorwort.qmd` | 5 | — | — | — | — | `des (Muster-)Kursbuchs der Bundesärztekammer gegliedert — ein Kapitel pro Modul.` |

## Zusammenfassung

- **Varianten der Auflagenangabe:** nur „2. Auflage, 2022“ (3 Stellen). Die Angabe
  „1. Auflage 2020“ kommt in keiner `.qmd`-Datei vor. Ebenso wenig der
  Dateiname `20200428_MKB-MedInformatik.pdf`; die Links zeigen auf
  `20220217_18_MKB_MedInformatik.pdf`.
- **Seitenzahlen:** nur „S. 10“ (2 Stellen, beide Modul I, beide mit „2. Auflage,
  2022, Abschnitt 4.1“). Eine Seitenzahl **ohne** Auflagenangabe gibt es nicht.
- **Ohne Auflage und ohne Jahr:** Modul IX, Zeile 325, „Kap. 2.7 (Blended
  Learning/E-Learning)“. Hinweis zur Prüfung durch den Autor: In der
  Dokumenteninformation der 2. Auflage, wie sie am 01.11.2026 in eine
  Arbeitssitzung eingefügt wurde, heißt Kapitel 2.7 „Lehr-/Kursformat“; die
  Änderung von „Blended Learning, E-Learning-Anteil“ dorthin ist dort für den
  17./18.02.2022 vermerkt. Nicht gegen das PDF geprüft.
- **Offen für den Autor:** ob der übernommene Wortlaut (aus der 1. Auflage 2020)
  in der 2. Auflage identisch ist, und ob „S. 10“ für Abschnitt 4.1 in der
  2. Auflage stimmt.

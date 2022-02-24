---
aliases: 
---
# Karnaugh Diagramme
Karnaugh Diagramme können benutzt werden, um Logik zu minimieren.
Dabei schreibt man die Logik in eine Tabelle und umkreist in diesen Tabellen dann die 1en (bzw 0en), um sie zusammen zu fassen.
bei [[Sum-of-products|SOPs]] werden die 1en umkreist und man erhält am Ende wieder eine [[Sum-of-products|SOP]].
Wenn wir die 0en Umkreisen, erhalten wir eine [[Product-of-sums|POS]], welche den negierten Ausgang beschreibt.
Beispiel siehe [[DT-Projekt1]] und 
![[DT-Projekt1_23.11.2021 16-57-35.excalidraw 2]]
## Aufbau des Diagrams
Die Diagramme sind mithilfe des [[Gray Code|Gray Codes]] aufgebaut, bei dem sich immer nur 1 Bit ändert.
## Umkreis-Regeln
Beim Umkreisen gelten folgende Regeln:
Wir müssen immer so viele Felder wie möglich mit einem Kreis umkreisen, dabei darf dieser Kreis nur eine Kantenlänge von $2^n$ haben (also 0,1,2,4,8...). Da ein Karnaugh-Diagram wie ein Verrücktes-Labyrinth Brett nirgens aufhört, sondern die linkeste Spalte angrenzend an die rechte ist, dürfen wir unsere Kreise also auch über Kanten und Ecken ziehen.
Wir sind fertig, sobald wir jede 1 (oder 0) mindestens einmal umreist haben
### [[Don't Care|Don't Cares]]
Wenn es [[Don't Care|don't cares]] gibt, dürfen, müssen wir sie aber nicht umkreisen.
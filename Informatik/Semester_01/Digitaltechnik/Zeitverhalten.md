---
aliases: 
---
# Zeitverhalten
## Kombinatorisch
Das Zeitverhalten ist immer sofort, also es gibt kein Delay zwischen der Eingang und der Ausgang ändert sich -> nicht realitätsnah
## reale Schaltungselemente
Reale Schaltungselemente benötigen für jeden Vorgang immer eine gewisse Zeit (z.B. für das Umladen von MOSFET Gate-Kapazitäten). Dabei ist eine zentrale Frage, ab wann ist der Ausgang stabil und wir können uns sicher sein, dass er auch das anzeigt was wir erwarten.
## Ausbreitungsverzögerung (propagation delay)
$t_{pd}$ steht für die Ausbreitungsverzögerung, also die maximale Zeit vom Eingang zum Ausgang
## Kontaminationsverzögerung (contamination delay)
$t_{cd}$ steht für die minimale Zeit vom Eingang zum Ausgang
## Ursache von Verzögerungen
- Kapazitöten
- Induktivitäten
- Wiuderstände
- Lichtgeschwindigkeit ist die maximale Ausbreitungsgeschwindigkeit

## Unterschied Kontamination- und Ausbreitungsverzögerung
Da es mehrere "Wege" für die Eingänge in einer Schaltung geben kann, (bspw der eine "läuft" über 3 And-Gates, der andere über 1 Or-Gate) kann die minimale und maximale Zeitverzögerung unterschiedlich sein

## Störimpulse (Glitches)
Wenn die Zeit der Verzögerung noch nicht abgelaufen ist, kann es zu Glitches kommen, bei denen der Ausgang hin und herspringt.
In einem [[Karnaugh Diagramme|Karnaugh Diagramm]] kann man glitche sehen, wenn 2 Kreise eine gemeinsame Kante haben->Beim Übergang der beiden Kreise kann(muss nicht) ein Glitch auftreten. Entfernen kann man diesen Glitch durch einen weiteren Kreis, der sich über die beiden Kreise aufspannt.
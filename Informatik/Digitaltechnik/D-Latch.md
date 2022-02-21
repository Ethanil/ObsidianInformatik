---
aliases: 
---
# D-Latch
Bei einem D-Latch haben wir neben einem Dateneingang $D$ noch ein Taktsignal $CLK$, welches die Funktionsweise des Latches bestimmt.
## Funktionsweise
Wenn die Clock auf $1$ ist, dann ist das Latch transparent und der Input $D$ wird im Latch gespeichert. Wenn die Clock auf $0$ ist, ist es egal was der Input ist, der Output ist immer gleich dem vorherigen Wert von $D$ während $CLK$ das letzte mal auf $1$ war.
![[D-Latch_21.02.2022 18-49-23.excalidraw.md]]
## Problematik
Breites Abtastfenster (die Zeit der Transparenz) sorgt für Unschärfe, da unklar ist, ob der wirkliche Wert oder ein Störimpuls übernommen wurde.
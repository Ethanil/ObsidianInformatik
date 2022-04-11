---
aliases: 
---
# Gray Code
Beim Gray Code, werden in der Wahrheitstabelle (bspw bei 2 Eingängen) die Möglichkeiten wie folgt dargestellt (bspw [[Konjunktion(und)|Und-Gatter]]):

| A   | B   | Y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 1   | 1   |
| 1   | 0   | 0   |

Anstatt wie sonst

| A   | B   | Y   |
| --- | --- | --- |
| 0   | 0   | 0   |
| 0   | 1   | 0   |
| 1   | 0   | 0   |
| 1   | 1   | 1   |

Der Vorteil ist, dass sich immer nur exakt 1 Bit ändert und nicht manchmal 2 (Zeile 2->3 und 3->4). Das ganze gilt auch von der letzten in die erste Zeile.

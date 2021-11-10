# Paritätsfunktion
## 1 Paritätsbit
Durch [[XOR]] können wir herausfinden, ob die Quersumme von gegebenen inputs gerade bzw ungerade sind. Dies können wir benuzten um Fehler in unserer übertragenen Bitfolge zu finden.
Dafür hängen wir einfach ein Paritätsbit an unsere Bitfolge dran und checken im nachhinein, ob die Quersumme der Bitfolge+Paritätsbit ungerade bzw gerade ist. Wenn sie gerade ist haben wir eine gerade Anzahl an Übertragungsfehlern, wenn sie ungerade ist eine ungerade Anzahl (d.h. wenn sie ungerade ist, ist immer ein Fehler aufgetreten bei gerade kann es sein, dass es 0 Fehler waren)
1011 || 1 -> 1011 || 1 : Gerade, 0 Fehler
1011 || 1 -> 1001 || 1 : Ungerade, 1 Fehler
1011 || 1-> 1000 || 1 : Gerade, 2 Fehler 

## Mehrere Paritätsbits
Ein einzelnes Paritätsbit ist also 1-Fehlererkennend
-> Die Lösung ist mehrere Paritätsbits anzuhängen:

|     |     |     |     |
| --- | --- | --- | --- |
| 1   | 0   |     | 1   |
| 1   | 1   |     | 0   |
|     |     |     |     |
| 0   | 1   |     |     |

Bspw. 4 Paritätsbits, dann übertragen wir dies bspw. so:
1011 || 1001 -> 1001 || 1001
Und erzeugen eine neue Tabelle:

|     |     |     |     |
| --- | --- | --- | --- |
| 1   | 0   |     | 1   |
| 0   | 1   |     | 1   |
|     |     |     |     |
| 1   | 1   |     |     |

Durch den Unterschied in Paritätsbits (1001 zu 1111) wissen wir das und auch genau was kaputt gegangen ist und können die Fehler dementsprechend korrigieren.
Der Nachteil ist, dass wir eine viel längere Bitfolge übertragen müssen (4 Bits-> 8 Bits)

## Bessere fehlerkorrigierende Codes
- Reed-Solomon Codes
- diverses anderes
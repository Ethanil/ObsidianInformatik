---
aliases: 
---
# Zeitverhalten synchroner sequentieller Logik
Siehe [[Zeitverhalten]] der kombinatorischen Logik.
Was passiert bei einer zeitgleichen Änderung von $D$ und $CLK$?
-> Es kommt zu einem [[Metastabilität|metastabilen Zustand]]
Um dies zu verhindern muss der Dateneingang $D$ im Abtast-Zeitfenster um die Taktflanke stabil sein.
## Zeitgrößen
- $t_{setup}$ ist das Zeitintervall vor der Taktflanke in der $D$ stabil sein muss
- $t_{hold}$ ist das Zeitintervall nach der Taktflanke in der $D$ stabil sein muss
- $t_a=t_{setup}+t_{hold}$ ist das Abtastzeitfenster
- $t_{ccq}$ Kontaminationsverzögerung: kürzeste Zeit bis Q umschaltet
- $t_{pcq}$ Laufzeitverzögerung: längste Zeit bis Q sich stabilisiert
## maximale Taktrate bestimmen
$t_{ccq}+t_{cd}$ dürfen zusammen addiert nicht kleiner als $t_{hold}$ sein.
Die maximale Taktrate kann berechnet werden durch:
$$f_{CLK}=\frac{1}{t_{CLK}}\leq\frac{1}{t_{pcq}+t_{pd}+t_{setup}}$$
Also durch den kritischen Pfad zwischen 2 Registern.
## Taktverschiebung
Durch leichte Zeitverzögerung der $CLK$ an den jeweiligen Registern kommt noch eine $t_{skew}$ hinzu, welche sowohl zu $t_{hold}$ beim Überprüfen, ob $t_{ccq}+t_{cd}$ nicht zu klein ist, als auch zu $t_{pcq}+t_{pd}+t_{setup}$ beim Berechnen der maximalen Taktrate addiert wird.
## Asynchrone Eingänge
Manchmal kann es sein, dass man auch asynchrone Eingänge benutzen muss, wie bspw. Benutzereingaben. Bei diesen können die Timing-Bedingungen nicht garantiert werden.
-> Wir benutzen also ein Schieberegister, bei derm das erste [[D-Flip-Flop|Flip-Flop]] [[Metastabilität|metastabil]] werden kann, welches idR vor der nächsten Taktfalnke in einen stabilen Zustand kippt und somit ist das zweite [[D-Flip-Flop|Flip-Flop]] nicht [[Metastabilität|metastabil]].
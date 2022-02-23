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

$t_{ccq}+t_{cd}$ dürfen zusammen addiert nicht kleiner als $t_{hold}$ sein
### Median Filter
Der Median Filter ersetzt einen Pixel mit dem Medianwert seiner Nachbarschaft, das heißt wir erhalten immer nur Grautöne, die im orginal erhalten waren (wir interpolieren also keine neuen Werte).
Wir unterdrücken damit isolierte Punkte bzw Rauschen und erhalten gleichzeitig die Schärfe der Kanten(vergleiche [[Lineare Filter#Gauss-Filter|Gauss-Filter]]). Der Nachteil ist allerdings, dass er sehr Rechenintensiv ist.
![[Pasted image 20230926111701.png# 1/2 left shadow]]
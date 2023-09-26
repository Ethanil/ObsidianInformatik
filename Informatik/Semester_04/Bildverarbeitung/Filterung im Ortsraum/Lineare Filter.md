## Tiefpass
Bei einem Tiefpass-Filter unterdrücken wir hohe Frequenzen (also feine Details werden entfernt)
![[Pasted image 20230926101627.png# 1/2 left shadow]]

Alle Koeffizenten sind ausnahmslos positiv und normalisiert (die Summe ergibt 1), daraus folgt auch dass sie nur positive Werte produzieren.
Sie versuchen allgemein einen mittelwert für einen pixel zu berechnen.
### Mittelwert Filter
Wir summieren alle Nachbarn auf und teilen durch die Anzahl der Felder.
![[Pasted image 20230926103812.png# 1/4 left shadow]]
Der Mittelwert filter entfernt Details und weicht Kanten auf.
![[Pasted image 20230926104020.png# 1/2 left shadow]]
### Gauss-Filter

## Hochpass
Bei einem Hochpass-Filter unterdrücken wir niedrige Frequenzen (also grobe Strukturen werden entfernt)
![[Pasted image 20230926101647.png# 1/2 left shadow]]
## Bandpass
Unterdrückung von hohen und niedrigen Frequenzen (also nur mittlere bleiben Übrig)
![[Pasted image 20230926101706.png# 1/2 left shadow]]

## Bandstop
Unterdrückung von mittleren Frequenzen (negation von Bandpass)
![[Pasted image 20230926101723.png# left 1/2 shadow]]

## Tiefpass
Bei einem Tiefpass-Filter unterdrücken wir hohe Frequenzen (also feine Details werden entfernt)
![[Pasted image 20230926101627.png# 1/2 left shadow]]

Alle Koeffizenten sind ausnahmslos positiv und normalisiert (die Summe ergibt 1), daraus folgt auch dass sie nur positive Werte produzieren.
Sie versuchen allgemein einen mittelwert für einen pixel zu berechnen.
Die Matrix ist typischerweise so aufgebaut, dass mittig ein hoher Wert steht und am Rand kleine.
### Mittelwert Filter (Boxfilter)
Wir summieren alle Nachbarn auf und teilen durch die Anzahl der Felder.
![[Pasted image 20230926103812.png# 1/4 left shadow]]
Der Mittelwert filter entfernt Details und weicht Kanten auf. Dabei schwingt er bei Kanten.
![[Pasted image 20230926104020.png# 1/2 left shadow]]
### Gauss-Filter
Wir verwenden folgende Formel um die Gewichte der Matrix zu erhalten:
$$\begin{align*}
G(x,y) = \frac{1}{2 \cdot \pi \sigma^{2}}e^{\frac{-x^{2}+y^{2}}{2\sigma^{2}}}
\end{align*}$$
![[Pasted image 20230926104454.png# 1/4 left shadow]]
Der Gauss-Filter entfernt Details und schwingt dabei (fast) nicht bei Kanten.
![[Pasted image 20230926104740.png# 1/2 left shadow]]

Vergleiche [[Nichtlinearer Filter#Median Filter|median Filter]].
### Anwendungsgebiete
 ![[Pasted image 20230926110306.png# 1/2 left shadow|Entfernung von Gauß'schem Rauschen]] 
![[Pasted image 20230926110243.png# 1/2 left shadow| Entfernung von periodischem Rauschen]]
![[Pasted image 20230926110215.png# 1/2 left shadow | Aufbereitung von Halbtonbildern]]
![[Pasted image 20230926110621.png# 1/2 left shadow | ROI(Region of Interest) Maske]]                                                     
## Hochpass
Bei einem Hochpass-Filter unterdrücken wir niedrige Frequenzen (also grobe Strukturen werden entfernt)
![[Pasted image 20230926101647.png# 1/2 left shadow]]

Die Koeffizienten können sowohl negativ als auch positiv sein, deren Summe 0 ergibt. Wir produzieren also auch negative Werte!
Bei einem Hochpass-Filter schauen wir uns die Ableitung der Werte des Bildes an.
### Erste Ableitung/Differenzfilter/partieller Gradienter
#### xy-Differenz
![[Pasted image 20230926114641.png# 1/4 left shadow]]
Der xy-Differenz-Filter beschreibt die Differenz in x und in y Richtung:
$$\Delta f \approx \sqrt{(f_{0,0}-f_{0,1})^{2}-(f_{0,0}-f_{1,0})^{2}} \approx |f_{0,0}-f_{0,1}|+|f_{0,0}-f_{1,0}|$$
#### Kreuzdifferenz
![[Pasted image 20230926114726.png# 1/4 left shadow]]
Der Kreuzdifferenz-Filter beschreibt die Differenz eines Bereichs "zwischen" 4 Pixeln:
$$\Delta f \approx \sqrt{(f_{0,0}-f_{1,1})^{2}+(f_{0,1}-f_{1,0})^{2}} \approx |f_{0,0}-f_{1,1}|+|f_{0,1}-f_{1,0}|$$
#### Roberts Operatoren
Reiner Hochpass-Filter
![[Pasted image 20230926115132.png# 1/2 left shadow]]
![[Pasted image 20230926115151.png# 1/2 left shadow]]
#### Prewitt Operatoren
Bildet zuerst mittels Tiefpass-Filter(simpler Boxfilter) den Durchschnitt von "oben" und "unten" (bzw "rechts" und "links") und subtrahiert diese danach.
![[Pasted image 20230926115216.png# 1/2 left shadow]]
![[Pasted image 20230926115230.png# 1/2 left shadow]]
#### Sobel Operatoren
Wie Prewitt, nur dass ein "Gauss"-Ansatz zur Tiefpass-Filterung verwendet wird
![[Pasted image 20230926115624.png# 1/2 left shadow]]
![[Pasted image 20230926115652.png# 1/2 left shadow]]
#### Kirsch-Kompass
Hier werden 8 Richtungen betrachtet und nicht nur 2
![[Pasted image 20230926120050.png# 1/2 left shadow]]
### Zweiter Ableitung

## Bandpass
Unterdrückung von hohen und niedrigen Frequenzen (also nur mittlere bleiben Übrig)
![[Pasted image 20230926101706.png# 1/2 left shadow]]

## Bandstop
Unterdrückung von mittleren Frequenzen (negation von Bandpass)
![[Pasted image 20230926101723.png# left 1/2 shadow]]

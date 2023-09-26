## Tiefpass
![[Pasted image 20230926101627.png# 1/2 left shadow|Bei einem Tiefpass-Filter unterdrücken wir hohe Frequenzen (also feine Details werden entfernt)]]

Alle Koeffizenten sind ausnahmslos positiv und normalisiert (die Summe ergibt 1), daraus folgt auch dass sie nur positive Werte produzieren.
Sie versuchen allgemein einen mittelwert für einen pixel zu berechnen.
Die Matrix ist typischerweise so aufgebaut, dass mittig ein hoher Wert steht und am Rand kleine.
### Mittelwert Filter (Boxfilter)

![[Pasted image 20230926103812.png# 1/4 left shadow|Wir summieren alle Nachbarn auf und teilen durch die Anzahl der Felder.]]
![[Pasted image 20230926104020.png# 1/2 left shadow|Der Mittelwert filter entfernt Details und weicht Kanten auf. Dabei schwingt er bei Kanten.]]
### Gauss-Filter
Wir verwenden folgende Formel um die Gewichte der Matrix zu erhalten:
$$\begin{align*}
G(x,y) = \frac{1}{2 \cdot \pi \sigma^{2}}e^{\frac{-x^{2}+y^{2}}{2\sigma^{2}}}
\end{align*}$$
![[Pasted image 20230926104454.png# 1/4 left shadow|3x3 Matrix]]
![[Pasted image 20230926104740.png# 1/2 left shadow| Der Gauss-Filter entfernt Details und schwingt dabei (fast) nicht bei Kanten.]]

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
Die erste Ableitung ist ein Richtungsabhängiger Filter, der nur durch Kombination der Partialergebnisse auf ein korrektes Gesamtergebnis kommt. Anwendung ist v.a. in der Automatisierung, Inspektion, Computervision und der optischen Messtechnik, da er Übergänge hervorhebt und robust gegenüber Rauschen ist.
Wir leiten also in mindestens 2 unterschiedliche Richtungen ab und verwendet eine Differenzmaske um ein Gesamtergebnis zu erhalten.
#### xy-Differenz
![[Pasted image 20230926114641.png# 1/4 left shadow]]
Der xy-Differenz-Filter beschreibt die Differenz in x und in y Richtung:
$$\Delta f \approx \sqrt{(f_{0,0}-f_{0,1})^{2}-(f_{0,0}-f_{1,0})^{2}} \approx |f_{0,0}-f_{0,1}|+|f_{0,0}-f_{1,0}|$$
#### Kreuzdifferenz
![[Pasted image 20230926114726.png# 1/4 left shadow]]
Der Kreuzdifferenz-Filter beschreibt die Differenz eines Bereichs "zwischen" 4 Pixeln:
$$\Delta f \approx \sqrt{(f_{0,0}-f_{1,1})^{2}+(f_{0,1}-f_{1,0})^{2}} \approx |f_{0,0}-f_{1,1}|+|f_{0,1}-f_{1,0}|$$
#### Roberts Operatoren
![[Pasted image 20230926115132.png# 1/2 left shadow|Reiner Hochpass-Filter]]
![[Pasted image 20230926115151.png# 1/2 left shadow|Roberts Operatoren]]
#### Prewitt Operatoren
![[Pasted image 20230926115216.png# 1/2 left shadow|Bildet zuerst mittels Tiefpass-Filter(simpler Boxfilter) den Durchschnitt von "oben" und "unten" (bzw "rechts" und "links") und subtrahiert diese danach.]]
![[Pasted image 20230926115230.png# 1/2 left shadow|Prewitt Operatoren]]
#### Sobel Operatoren
![[Pasted image 20230926115624.png# 1/2 left shadow|Wie Prewitt, nur dass ein "Gauss"-Ansatz zur Tiefpass-Filterung verwendet wird]]
![[Pasted image 20230926115652.png# 1/2 left shadow|Sobel Operatoren]]
#### Kirsch-Kompass
![[Pasted image 20230926120050.png# 1/2 left shadow|Hier werden 8 Richtungen betrachtet und nicht nur 2]]
![[Pasted image 20230926120118.png# 1/2 left shadow|Kirsch Kompass]]
### Zweiter Ableitung
Linien und Punktet-Detektor, da die zweite Ableitung verwendet wird und wie so keinen Ausschlag mehr bei Rampen und homogenen Flächen haben, sondern nur einen großen Ausschlag bei scharfen Unstetigkeiten, einzelnen Punkten oder dünnen linien und einen mittleren Ausschlag bei Übergängen(Stufen).
Die zweite Ableitung erzeugt immer Doppelkanten, wobei die eigentliche Kante des Bildes zwischen diesen beiden Kanten liegt.
Diese linearen Filter sind dabei richtungsunabhängig(Punkte haben auch keine Richtung) und kommen somit mit einer einzelnen Filtermaske aus. Sie heben kleine Details hervor und verstärken Rauschen. Dies entspricht der menschlichen Wahrnehmung, ist also sehr relevant für die Bildverbesserung.
#### Differenzfilter
![[Pasted image 20230926121336.png# 1/4 left shadow|Die einfachste Art ist eine Art Boxfilter, der nach unterschieden in der Umgebung sucht.]]

#### Laplacian Filter
$$L(x,y) = \Delta^{2}f(x,y) = \frac{\partial^{2}f(x,y)}{\partial x^{2}} + \frac{\partial^{2}f(x,y)}{\partial y^{2}}$$
![[Pasted image 20230926121544.png# 1/4 left shadow]]$$\begin{align*}
&1 \geq \alpha \geq-1 \\\\
x = &\begin{cases}
4 &&1\geq \alpha \geq 0 \\
4(1-\alpha)&&0>\alpha \geq -1
\end{cases}
\end{align*}$$
#### Laplacian-of-Gaussian (LOG)-Filter
Wir reduzieren das Rauschen mittels eines Gauss-Filters und danach dann einen Laplacian Filter.

### Kantenextraktion
Wir wollen versuchen Kanten in unserem Bild zu finden. Dafür können wir bspw. die bekannten Filter mit einem Schwellenwert binarisieren. Dies führt allerdings fast nie zu einem guten Ergebnis. Eine andere Möglichkeit ist es mit LoG Kanten zu finden und dort die Zero-Corssings zu berechnen(Marr-Hildreth Operator) 
#### Konturverfolgung nach Canny
Wir wollen ein Binärbild mit möglichst geschlossenen Konturen erschaffen.
Dabei identifizieren wir von einem Startpunkt aus den nächsten Konturpunkt entlang eines Suchstrahls. Die Richtung der Kante ergibt sich aus dem bereits erhaltenen Punkten oder dem Gradienten. Diese "Fortlaufende Kantensuche" führt allerdings zu falschen Konturen, wenn einmal ein Fehler gemacht wurde.
Wir gehen wie folgt vor:
1. Tiefpass mit Gauß-Filter
2. Berechne kombinierten Gradientenbetrag und Richtung der 1. partiellen Ableitung (z.B. nach Sobel). Die Richtung zeigt dabei dei Kantennormale n
3. Die Kantennormale wird in 0°, 45°, 90° und 145° gerundet
4. non-maximal supression auf dem Gradientenbild:
	1. "Verdünne" Gradienten
	2. Unterdrücke lokale minima(Suche in der 8-[[Nachbarschaft]] entlang von n das Pixel mit dem maximalen Gradienten) => Dadurch erhalten wir "Dünne" Kanten
5. Verfolge die Kanten in alle Richtungen mittels [[Schwellwert-Hysterese]] um Kanten zu verbinden => Wir legen 2 Grenzen fest, einmal $T_{1}$ und einmal $T_{2}$, wenn ein Wert größer als $T_{1}$ ist, dann wird er unabhängig von seinen Nachbarn hinzugefügt, wenn er nur größer als $T_{2}$ ist, dann wird er nur dann hinzugefügt, wenn ein Nachbar bereits hinzugefügt wurde. (Wir wählen $T_{2}:T_{1} \approx 1:3$)
## Bandpass
Unterdrückung von hohen und niedrigen Frequenzen (also nur mittlere bleiben Übrig)
![[Pasted image 20230926101706.png# 1/2 left shadow]]

## Bandstop
Unterdrückung von mittleren Frequenzen (negation von Bandpass)
![[Pasted image 20230926101723.png# left 1/2 shadow]]

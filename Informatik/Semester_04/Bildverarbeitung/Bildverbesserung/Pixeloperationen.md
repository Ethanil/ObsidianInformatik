## negativ
Wir negieren die Werte.
![[Pasted image 20230925105813.png|200]]
## Binarisierung
Wir legen eine Grenze fest und setzen alle Werte unter der Grenze auf einen Wert und alle anderen auf einen anderen.
![[Pasted image 20230925105832.png|200]]
## Quantisierung
Gleich wie Binarisierung nur mit mehreren Werten.
![[Pasted image 20230925105853.png|200]]
## Fensterung
Bei der Fensterung werden bestimmte Bereiche hervorgehoben und unterdrückt. ![[Pasted image 20230925105931.png|right|200]]
## Kontrastspreizung
Bei der Kontrastspreizung werden die Werte versucht gleichmäßig zu verteilen.
![[Pasted image 20230925111013.png]]
## Histogrammausgleich
Wir Transformieren die Grauwertskala anhand der Kurve der Summenwahrscheinlichkeiten
![[Pasted image 20230925114631.png|600]]
Ziel ist an sich das gleiche wie die Spreizung, aber wir können bspw gut mit Ausreißern umgehen.
## Dynamik Kompression
Wir Skalieren die Lichtintensitöten bei der Abbildung nichtlinear (bspw mit log)
$$g[m,n] = c \times \log(1+|i[m,n]|)$$
## Gamme Korrektur
Wiedergabe der Intensitäten von Pixeln auf einem bildarstellenden Medium ist idr. nichtlinear.
$$g[m,n] = f_{max}\left(\frac{f[m,n]}{f_{max}}\right)^{\gamma}$$
## Differenz
Detektion dynamischer Bildbereiche
$$g[m,n]=f_{1}[m,n] - f_{2}[m,n]$$
## Mittelung
Unterdrückung von unkorreliertem Rauschen ( aka arithmetisches Mittel)
$$g[m,n] = \frac{1}{k}\sum_{k}f_{i}[m,n]$$
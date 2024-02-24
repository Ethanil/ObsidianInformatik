---
aliases: 
---
Aus Sicht der Rendering-Pipeline gibt es mehrere Koordinatensysteme:
- Weltkoordinaten, die die gesamte Szene beschreiben
- Objektkoordinaten, die die Lage von 3D-Objekten lokal festlegen
- Projektionskoordinaten, die man nach Anwendung der [[Pipeline#Projektion]] erhält
- Normierte Koordinaten
- Bildschirmkoordinaten
## Affine Unterräume
Ein affiner Unterraum ist ein um einen festen Vektor verschobenen [[Untervektorraum]] 
### Baryzentrische Koordinaten
![[Pasted image 20240223234443.png# shadow float right 2/3]]
In einem affinen Unterraum kann jeder Punkt in baryzentrischen Koordinaten dargestellt werden, also als eine Gewichtung von Punkten in diesem.
## Position durch Transformation
In einer 3D-Szene wird oft das selbe 3D-Objekt mehrfach instanziert und transformiert, sodass es wie unterschiedliche Objekte wirkt.
### Lineare Abbildungen
Lineare Abbildungen lassen den Ursprung des 3D-Objektes invariant und lassen sich im dreidimensionalen als $3x3$-Matrix darstellen:
- Skalierung
- Scherung
- Rotation
Normalen der Objekte können dabei nicht auch einfach mit der selben Matrix multipliziert werden, sondern müssen mit der transponierten inversen Matrix multipliziert werden.
### Affine Abbildungen
Eine Affine Abbildung ist eine Lineare Abbildung bei der eine Vektor auf das Ergebnis gerechnet wird.
### Homogene Koordinaten
Mithilfe von homogenen Koordinaten können sowohl Lineare, als auch affine Abbildungen durch reine Matrixmultiplikation dargestellt werden. Dazu werden die 3D-Koordinaten zu homogenen 4D-Koordinaten verändert.

## Rotation um eine beliebige Ursprungsachse
Die Rotation um eine beliebige Ursprungsachse wird durchgeführt, indem das Objekt an den Ursprung verschoben wird, dort rotiert wird und dann wieder zurückverschoben wird.
## Links
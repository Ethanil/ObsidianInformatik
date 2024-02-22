---
aliases: 
---
![[Pasted image 20240222225112.png# shadow ]]
# Anwendung
![[Pasted image 20240222225829.png# shadow float right 1/2]]
Der Abschnitt wird auf der CPU ausgeführt. Die zu zeichnende Geometrie wird an den nächsten Abschnitt übergeben.
In diesem Abschnitt wird beispielsweise
- Kollisionserkennung und -behandlung
- Beschleunigungsalgorithmen
- Animationen
- Simulationen
ausgeführt.
Der output dieser Stufe sind
- 3D-Objekte bestehend aus graphischen Primitiven
- Position und Art des Lichts
- Position und Ausrichtung der Kamera
- Zusätzliche Informationen über das zu erstellende Bild
# Geometrie
![[Pasted image 20240222225815.png# shadow float right 4/5]]
In dieser Stufe werden die meisten Operationen durchgeführt, die pro Polygon bzw pro Vertex durchgeführt werden
## Model and View Transform
In diesem Schritt wird das Koordinatensystem des Modells über ein Weltkoordinatensystem in ein Koordinatensystem der Kamera überführt. Die Blickrichtung der Kamera ist hierbei dann -z.
## Vertex Shading
In diesem Schritt wird die Beleuchtung und die Materialeigenschaften pro Vertex ausgewertet. Es werden also Position, Normale, Farbe und weiteres pro Vertex gespeichert. Diese Daten werden dann bei der Rasterisierung zur endgültigen Berechnung der Farbe eines Pixels verwendet.
## Projektion
In diesem Schritt wird das sichtbare Volumen in den Einheitswürfel mit Extrempunkten $(-1,-1,-1)$ transformiert.
Zwei Arten dies zu tun sind zum einen Parallelprojektion(Kamera ist hier im unendlichen und parallele Linien bleiben parallel) und Perspektivische Projektion(Kamera ist im endlichen und das sichtbare Volumen bildet einen Pyramidenstumpf)
## Clipping
In diesem Schritt wird die Anzahl der Primitiven reduziert:
- Primitive außerhalb des sichtbaren Volumens werden verworfen
- Primitive die teilweise sichtbar sind werden durch welche ersetzt, die ganz im Sichtbaren liegen
## Screen Mapping
In diesem Schritt werden die verbleibenden Primitive auf die Bildschirmkoordinaten projiziert. Dies wird durch eine Translation gefolgt von einer Skalierung gemacht.
# Rasterisierung
![[Pasted image 20240222233333.png# shadow float right 3/4]]

## Links
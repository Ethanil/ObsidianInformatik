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
## 


## Links
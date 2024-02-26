---
aliases: 
---
a![[Pasted image 20240222225112.png# shadow ]]
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

Der Output der Geometrie Stufe sind die verbleibenden Primitive als 2D Vertices mit z-Koordinaten, Shading Parametern und weitere Informationen
# Rasterisierung
![[Pasted image 20240222233333.png# shadow float right 3/4]]
Bei der Rasterisierung werden die Operationen pro Pixel durchgeführt
## Triangle Setup
In diesem Schritt wird eine Vorberechnung ausgeführt um graphische Primitive in Pixel umzurechnen. Es wird berechnet:
- Steigung der Primitivkanten
- Schnittpunktberechnung zwischen Primitivkante und Bildschirmzeile
- Sortierung nach x-Koordinate
Daraus ergibt sich eine sortierte Zahlenliste zu jeder Bildschirmzeile eines jeden Primitivs
## Triangle Conversion
In diesem Schritt werden für alle Pixel Fragmente generiert. Dabei können mehrere Fragmente einer Pixelposition zugeordnet sein. Hierbei werden den Fragmenten durch Interpolation Eigenschhaften zugerodnet:
- Tiefe des Fragments
- Shading Information
- Normale
- Texturkoordinate
- Weitere
## Pixel Shading
In diesem Schritt werden eine oder mehrere Farben den Fragementen zugeordnet. Durch verschiedene Operationen(die zum teil nacheinander auf das selbe Fragment angewand werden können) können verschiedene Resultate entstehen. Beispielhafte Operationen
- Phong Shading
- Texturierung
- Bump Mapping
## Merging
Das Ergebnis aller Berechnungen soll im Color Buffer gespeichert werden. Dafür erhält jeder Pixel exakt einen Wert in diesem 2D-Array.
In diesem Schritt wird die Sichtbarkeit der Fragmente berechnet, typischerweise durch einen z(Depth)-Buffer.
Die Reihenfolge in der die Fragemente abgearbeitet werden ist dabei irrelevant. Es können teilweise transparente Fragmente verarbeitet werden, dabei wird dann ein weiterer (alpha-)Kanal zusätzlich zu den RGB-Werten benötigt.
Während des Mergings kann auch ein Stencil angewand werden, um beispielsweise eine Bestimmte Region von Fragmenten zu verwerfen.
In diesem Schritt können auch Bilder Accumuliert werden und überlagert werden, um beispielsweise ein Motion-Blur zu erzeugen.
### Flimmern
Wenn das Bild aufgebaut wird(also der Bildschirm entscheidet ein neues Bild zu zeigen), während es gerade geändert wird(also aus der Grafikpipeline ein neues Bild entsteht), dann kann es zu Flimmern kommen. Um dies zu verhindern verwenden wir einen Buffer, in dem die Grafikpipeline ein neues Bild aufbaut dieses dann instantan mit dem angezeigten ausgetauscht werden kann
### Tearing
![[Pasted image 20240223003756.png# shadow float right 1/2]]
Ein Problem beim Abbilden der Daten mit bspw. einem Monitor ist das Tearing. Tearing entsteht, wenn das swappen des neuen Bildes nicht mit der Wiederholungsrate des Bildschirms getimed ist. Um dies zu verbessern wird V-Sync verwendet, welches das swappen mit der Wiederholungsrate synchronisiert. Dabei kann es allerdings vorkommen, dass die Grafikpipeline auf das wechseln des Buffers warten muss. Die Lösung hierfür ist einen dritten Buffer zu verwenden, wodurch die Grafikpipeline immer einen Buffer zum bearbeiten hat und der Monitor immer ein aktuell anzuzeigendes nächstes Bild hat.
## Links
Die Skelettierung ist eine Verdünnung von Segmenten auf eine Skelettlinie mit folgenden Eigenschaften
- Genau 1 Pixel breit
- Genau in der Mitte eines lokalen Segments
- Wiederspiegelung der Ursprungsform
- Robustheit gegenüber Störungen
- Konvergenz auf eindeutiges Ergebnis
- Linien werden nicht verkürzt

Andere Art dies zu sehen:
- Wir definieren $D_{\max}$ als die größt mögliche eingeschlossene Scheibe auf dem Sekelett
- $D_{\max}$ muss die Form an mindestens zwei Positionen berühren
- Es existiert keine größere eingeschlossene Scheibe, welche $D_{\max}$ einschließt

Durch [[Morphologische Transformationen]] können wir eine Skelettierung ausführen, indem wir das Bild durch Masken verdünnen, bis es konvergiert.

## Euler'sche Skelettierung
Wir verwenden die Euler'sche Charakteristik, die ein Objekt mittels seiner Anzahl an Ecken, Kanten und Flächen beschreibt (Objekt = Ecken - Kanten + Flächen).
Dies können wir zu Skelettierung verwenden indem wir für jedes Pixel in einer 3x3 Umgebung überprüfen, ob wir es entfernen Können ohne die Euler'sche Charakteristik zu verletzen (und keine Endpunkte dadurch entfernen).
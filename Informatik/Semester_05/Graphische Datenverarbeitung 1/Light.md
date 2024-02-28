---
aliases: 
---
Ziel in der Darstellung von 3D-Modellen ist häufig der Photorealismus.
Wir betrachten Licht als Lichtstrahlen, die wir entlang ihrer Richtung verfolgen können.
# Lichtreflexion
Lichtreflexion hängt vom Material ab. Es gibt verschiedene Arten von Reflexion:
- diffus
- glänzend
- spiegelnd
- anisotrop
- durchscheinend
- weitere, komplexe Oberflächenstrukturen
## Ambiente Beleuchtung
Ambiente Beleuchtung ist immer vorhanden und Unabhängig von Einfallswinkel und Lichtposition
## Ideal diffuse Relfexion
![[Pasted image 20240226161310.png# shadow float right 1/2]]
Es wird das Lambert'sche Beleuchtungsmodell verwendet, welches Abhängig von dem Winkel, mit dem das Licht auf die Oberfläche trifft, aber unabhängig von der Richtung zum Betrachter, das Licht reflexiert
## Ideal spiegelnde Relfexion
![[Pasted image 20240226161417.png# shadow float right 1/2]]
Wir berechnen mit dem Lichtvektor L und der Normalen N den reflexierten Vektor R(L)
## Spekulare Relfexion
Eine spekulare Relfexion stellt eine glänzende, aber nicht spigelnde Oberfläcche da. Typischerweise wird in die Vorzugsrichtung r reflektiert und damit ist der Winkel zwischen dieser idealen Reflexionsrichtung und der Betrachterposition wichtig. Materialien erhalten einen Spiegelungsexponent S, der festlegt wieviel prozent von der eingehenden Strahlung reflexiert wird.
### Phong shading
![[Pasted image 20240226163147.png# shadow float right 1/2]]
Beim Phong shading wird das Skalarprodukt zwischen der reflektierten Lichtrichtung(R(L)) und der Richtung zum Betrachter (V) hoch einem exponenten genommen. Umso kleiner dieser exponent, umso größer und intensiver ist der spekulare Fleck.
### Blinn-Phong
![[Pasted image 20240226163436.png# shadow float right 1/2]]
Hierbei wird ein Halbierungs-Vektor H zwischen einfallender Lichtrichtung und Blickrichtung erstellt und das Skalarprodukt zwischen diesem und der normalen genommen und das Produkt dann hoch einem Exponenten, der den gleichen Effekt wie der beim Phong-shading hat.
## Kombination von Beleuchtungsmodellen
Für eine annähernde 
## Links
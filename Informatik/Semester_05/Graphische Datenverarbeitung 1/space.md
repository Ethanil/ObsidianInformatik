---
aliases: 
---
# Beschleunigungsalgorithmen
## Culling
Beim Culling werden nicht sichtbare Teile aus der Szene entfernt.
- view frustrum: Objekte außerhalb des frustrums werden entfernt
- backface: Faces, die auf der Rückseite von Models liegen, werden entfernt
- occlusion, portal: Objekte, welche von anderen verdeckt werden, werden entfernt
- detail: Kleine und weit entfernte Objekte, werden entfernt
## Räumliche Datenstrukturen
### Bounding Volume
Ein Bouding Volume ist ein Hüllkörper einfacher Geometrie, der das Objekt umschließt. Dabei können bspw axis-aligned-bounding-boxes verwendet werden.
## Links
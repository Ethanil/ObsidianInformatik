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
#### Bounding Volume Hierachy
Mithilfe einer aufgestellten Hüllkörperhierarchy kann view-frustrum-culling schneller durchgeführt werden, da nicht gegen jedes Objekt gecheckt werden muss.
### Räumliche Aufteilung
In dieser Variante teilen wir unsere Szene räumlich auf und können so direkt nur die Objekte überprüfen, die für das Anzeigen in Frage kommen.
### oct-tree
Hierbei wird eine objektabhängige, hierarchiche Unterteilung des Raumes mit achsenparallelen Boxen unterschiedlicher Größe gemacht.
### kd-tree
Ein kd-tree ist ein flexiblerer oct-tree bei dem nicht alle achsen der selben tiefe auf der selben höhe/breite liegen müssen.
### bsp-tree
Bei einem Binary Space Partition-tree wird der Raum nicht achsenparallel aufgeteilt.
## Links
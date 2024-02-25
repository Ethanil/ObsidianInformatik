---
aliases: 
---
Das Culling ist dafür da nicht sichtbare Teile von der Szene zu trennen.
# Backface Culling
Das Backface Culling wird durch die Grafikkarte durchgeführt und entfernt abgewandte Primitive von Objekten. Im kanonischen Sichtvolumen sind alle Sehstrahlen parallel, wodurch die Betrachtungsrichtung mit der Normale der Faces die sichtbaren Primitive definieren kann.
# Clipping
Beim Clipping werden nur Objekte gerastert, welche auch vollständig oder zumindest teilweise sichtbar sind. Clipping ist das entfernen der Primitiven, die außerhalb des sichtbaren Bereiches liegen.
Das Clipping wird nach der Projektion in das kanonische Sichtvolumen durchgeführt. Clipping verhindert wrap-around von Punkten die an sich im unendlichen liegen, indem sie vorher geclipped werden.
## Liang-Barsky-Algorithmus
Der Liang-Barsky-Algorithmus wird verwendet um Linien zu clippen, allerdings ist das Berechnen aller möglichen Schnitte unnötig und kann durch den Cohen-Sutherland-Algorithmus effizienter gelöst werden
## Cohen-Sutherland-Algorithmus
Der Cohen-Sutherland-Algorithmus ist dafür da um einen (für den 2D-Fall) 4
## Links
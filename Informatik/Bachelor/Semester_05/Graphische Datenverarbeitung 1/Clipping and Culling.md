---
aliases: 
---
Das Culling ist dafür da nicht sichtbare Teile von der Szene zu trennen.
# Backface Culling
Das Backface Culling wird durch die Grafikkarte durchgeführt und entfernt abgewandte Primitive von Objekten. Im kanonischen Sichtvolumen sind alle Sehstrahlen parallel, wodurch die Betrachtungsrichtung mit der Normale der Faces die sichtbaren Primitive definieren kann.
# Clipping
Beim Clipping werden nur Objekte gerastert, welche auch vollständig oder zumindest teilweise sichtbar sind. Clipping ist das entfernen der Primitiven, die außerhalb des sichtbaren Bereiches liegen.
Das Clipping wird nach der Projektion in das kanonische Sichtvolumen durchgeführt. Clipping verhindert wrap-around von Punkten die an sich im unendlichen liegen, indem sie vorher geclipped werden.
## Liang-Barsky-Algorithmus(L&B)
Der Liang-Barsky-Algorithmus wird verwendet um Linien zu clippen, allerdings ist das Berechnen aller möglichen Schnitte unnötig und kann durch den Cohen-Sutherland-Algorithmus effizienter gelöst werden
## Cohen-Sutherland-Algorithmus(CSA)
Der Cohen-Sutherland-Algorithmus ist dafür da um einen (für den 2D-Fall am Viereck) 4-Bit code für einen Punkt zu erhalten um herauszufinden, wo dieser sich im Verhältnis zu den Clip-Ebenen(bzw im 2-Dimensionalen Clip-Geraden) befindet. Durch Anwendung von logischem Oder und logischem Und auf 2 Punkte kann herausgefunden werden, ob die Linie dieser beiden Punkte vollständig innerhalb(Oder) bzw vollständig außerhalb(Und) befindet oder einen Übergang zwischen innen und außen hat, also *eventuell* geclipped werden muss.
## Sutherland-Hodgman-Algorithmus
Beim Sutherland-Hodgman-Algorithmus werden die zu clippenden Polygone sukzessive mit den Fenstergrenzen mittels CSA und L&B geclipped um korrekte Polygone zu erhalten
## Links
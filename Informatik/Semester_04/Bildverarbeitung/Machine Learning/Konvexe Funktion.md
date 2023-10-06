Eine Konvexe Funktion ist eine Funktion, wenn für alle $x,x'$ und für $\lambda \in (0,1)$ gilt:
$$f(\lambda x + (1-\lambda)x')\leq \lambda f(x) + (1-\lambda)f(x')$$
Also wenn wir eine Linie zwischen zwei Punkten $x,x'$ von der Funktion ziehen, dann sind alle Punkte zwischen $x$ und $x'$ unterhalb dieser Geraden:
![[Pasted image 20231005220733.png# 2/3 left shadow|Eine Konvexe Funktion]]

## Konvexe Menge
Eine Menge $M$ ist konvex, genau dann wenn $\lambda x + (1-\lambda) x' \in M$ 
Wenn eine Funktion konvex ist, dann sind alle seine [[Niveaumenge]]n auch konvex. Nicht alle Funktionen, die eine konvexe Niveaumenge haben sind konvex.

## Operationen die Konvexität beibehalten
- [[Schnittmenge]] zweier Konvexen Mengen
- [[Lineare Abbildungen|Lineare Abbildung]] einer Konvexen Menge
- [[Lineare Abbildungen|Lineare Abbildung]] des [[Komplement|Komplements]] einer konvexen Menge
- Lineare Kombination mit nicht-negativen Parametern und einer konvexen Funktion
- Punktwertiges maximum einer konvexen Funktion
- Projektion in einer Richtung einer konvexen Funktion.
- Komposition mit einer affinen Funktion und einer konvexen Funktion

## Eigenschaften
Jede Tangente einer Konvexen Funktion hat keine Schnittstelle mit der Funktion.
### Bregman Divergenz
Über die Tangente eines Punktes $x'$ der Konvexen Funktion können wir die Entfernung von $x$(ein weiterer Punkt der Funktion) zu $x'$ angeben:
$$D_{F}(x,x')=F(x)-F(x')-<\Delta F(x'),x-x'>$$
![[Pasted image 20231005223229.png# 5/6 left shadow|Bregman Divergenz]]

### Ableitbarkeit
Eine konvexe Funktion ist immer mindestens überall stückweise ableitbar
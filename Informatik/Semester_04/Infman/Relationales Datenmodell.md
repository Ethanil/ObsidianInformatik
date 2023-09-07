---
aliases: 
---
# Relationales Datenmodell 
Bei einem Relationalem Datenmodell werden die Daten in einem *einzigen* Konstrukt, der Relation gespeichert (Informall ist dies eine Tabelle)
## Logischer Entwurf
Beim logischen Entwurf wird das [[Konzeptionelles Datenmodell]], z.B. ein [[ER-Diagramm|ER-Modell]], auf ein logisches, also bspw eine relationales Datenmodell abgebildet.

## Mathematische Definition
### Menge aller Datentypen/Domänen D
$D=\{D_{1},D_{2},\dotso,D_{n}\}$
Domänen sind bspw ganze Zahlen, Zeichenketten, ...
### Schema R
$R=$ Menge von Attributen, $R=\{A_{1},A_{2},\dotso,A_{n}\}$
Jedes Attribut in R hat einen eindeutigen Namen. Mithilfe von $dom$ ordnen wir einem Attribut seine Domäne zu, also $dom(A)$ ist die Domäne von A, bspw die ganzen Zahlen. Eine Domäne bsteht aus *Attributswerten*
### Relation r
$r(R) \subseteq dom(A_{1}) \times dom(A_{2}) \times \dotso \times dom(A_{n})$

## Links
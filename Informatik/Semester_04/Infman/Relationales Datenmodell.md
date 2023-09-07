---
aliases: 
---
# Relationales Datenmodell 
Bei einem Relationalem Datenmodell werden die Daten in einem *einzigen* Konstrukt, der Relation gespeichert (Informall ist dies eine Tabelle ohne Reihenfolge und ohne Duplikate)
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

## Schlüssel
Schlüssel müssen auch für Relationen definiert werden
### Superschlüssel
Eine Attributsmenge $K$ heißt Superschlüssel einer Relation, wenn jedes $K$-Teiltupel genau ein Tupel eindeutig identifiziert
D.h. $K$ ist schlüsseleindeutig, wenn gilt: $\forall t_{1},t_{2} \in r: t_{1}(K) = t_{2}(K) \Rightarrow t_{1}= t_{2}$
#### Eigenschaften
| Bezeichung      | Bedeutung                                                           |
| --------------- | ------------------------------------------------------------------- |
| einfach         | falls $K$ nur aus einem Attribut besteht                            |
| zusammengesetzt | falls $K$ nicht einfach ist                                         |
| trivial         | falls $K$ aus allen Attributen der Relation besteht                 |
| minimal         | falls kein $K'\subset K$ exisitert, der auch ein Superschlüssel ist |

### Schlüsselkandidat
Ein Schlüsselkandidat, bzw Schlüssel ist ein minimaler Superschlüssel. Es kann mehrere Schlüsselkandidaten geben

### Primärschlüssel
Der Schlüsselkandidat, der für das Schema gewählt wird

### Fremdschlüssel
Eine Attributsmenge $K'$ eines Schemas $S$ heißt Fremdschlüssel bezüglich des Schemas $R$, falls Referenz $\uprho(K')$ der Primärschlüsel von $R$ ist und refernzielle Integrität erfüll
## Links
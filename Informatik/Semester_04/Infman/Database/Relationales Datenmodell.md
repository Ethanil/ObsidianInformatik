---
aliases: 
---
# Relationales Datenmodell 
Bei einem Relationalem Datenmodell werden die Daten in einem *einzigen* Konstrukt, der Relation gespeichert (Informell ist dies eine Tabelle ohne Reihenfolge und ohne Duplikate)
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

### Tupel t
$t \in r:$ Ein Tupel ist eine Abbildung $t: R \rightarrow \bigcup^{n}_{\{i=1\}}w \in D_{i}$ 
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
Eine Attributsmenge $K'$ eines Schemas $S$ heißt Fremdschlüssel bezüglich des Schemas $R$, falls Referenz $\uprho(K')$ der Primärschlüsel von $R$ ist und referenzielle Integrität erfüllt ist

#### Referenzielle Integrität
Werte für $K'$ in $s(S)$ nehmen nur Werte an für die in $R$ eine Entsprechung existiert
## Abbildung [[ER-Diagramm|ER-Modell]] in Relationales Modell
### Regel 1: Abbildung von Entitätstypen
Für jeden Entitätstypen wird ein eigenes Schema definiert und wir übernehmen den Schlüssel des Entitätstypen als PK (bzw minimieren ihn zuerst)
### Regel 2: Abbildung von Beziehungstypen
Für jeden Beziehungstyp wird ein eigenes Schema erzeugt wobei wir die Primärschlüssel aller beteiligter Schemata als Fremdschlüssel nehmen. Der Primärschlüssel des erzeugten Schemas ist immer der Fremdschlüssel der $N$-Seite(n) bzw. einer der 1-Seiten wenn es keine $N$-Seite gibt.
### Regel 3: Zusammenfassung von Schemata
Alle Schemata mit gleichem PK können zusammengefasst werden.
```ad-warning
title:Ausnahme
Schemata mit dünn besetzten Schemata sollten auch bei gleichem PK nicht zusammengefasst werden, da wir ansonsten viele `null` Einträge haben!
```
### Regel 4: Schwache Entitäten modelieren
Für jede schwache Entität wird ein eigenes Schema definiert, wobei wir den Schlüssel als PK übernehmen und den PK der "erzeugenden" Entität als FK und PK hinzufügen.
## Links
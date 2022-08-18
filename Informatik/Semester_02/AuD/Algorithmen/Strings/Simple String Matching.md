---
aliases: 
---
# Simple String Matching 
## Abstrakt
- T: Den String den wir suchen
- m: die Länge von T
- S: Der String in dem wir suchen
- n: die Länge von S
- R: Liste der Start-Indizes von gefundenen Strings (T in S)
- I: Liste der möglichen Kandidaten, bevor sie in R geschrieben werden
- r ist die Maximale Anzahl an Kandidaten, die gleichzeitig in I sein können
### Invariante
Nach i $\geq$ 0 iterationen gilt:
R beinhaltet genau die Start-Indizes von allen angetroffenen T's in S in aufsteigender Ordnung.
I beinhaltet genau die Start-Indizes aller möglichen Kandidaten T's in S in aufsteigender Ordnung, also sobald ein Anfang eines Strings gefunden wurde, wird er in I gespeichert. Sobald der Kandidat für korrekt gefunden wurde, wird er in R abgespeichert
### Variante
i wird bei jeder iteration um 1 größer
### Abbruchbedingung
n Iterationen abgeschlossen.
## Komplexität
Worst-Case runtime ist $O(n \cdot r) \subseteq O(n \cdot m)$

## Links
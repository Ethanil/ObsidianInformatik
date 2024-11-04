---
aliases: 
---
# Selectionsort 
## Abstrakt
- $S$: die zu sortierende Liste
- $m$: Pointer zum aktuellen Maximum im unsortierten Teil der Liste
- $j$: Pointer zum Element, was wir mit $m$ vergleichen
### Invariante
Nach $i \geq 0$ Iterationen:
Die Elemente am Ende der Liste sind korrekt sortiert.
### Variante
$i$ wird um 1 erhöht
### Abbruchbedingung
$i=|S|-1$
### Input
eine endliche geordnete Sequenz mit einer bestimmten Länge aus Elementen eines beliebigen Typs, Duplikate sind erlaubt
eine strenge schwache Ordnung "<" auf dem beliebigen Typ
### Output
eine Permutation der Sequenz mit den exakt gleichen Elementen wie vom Input, die gemäßt der Ordnung aufsteigend sortiert ist.
## Ablauf
Wir gehen durch den unsortierten Teil der Liste und setzen $m$ immer auf den Wert, der größer ist als das vorherige $m$ (bei Gleichheit bleibt das erste $m$!). Wenn wir am Ende der unsortierten Teil der Liste angekommen sind, tauschen wir dieses Element mit $m$.
## Komplexität
Die asymptomatische Komplexität ist $\Theta(T \cdot n^2)$ im best und worst case, wobei $T$ die Komplexität der Vergleichsoperation ist.
## FUCKY START
nach i=0 haben wir 1 Element sortiert, BECAUSE FUCK CONSINSTENCY

## Links
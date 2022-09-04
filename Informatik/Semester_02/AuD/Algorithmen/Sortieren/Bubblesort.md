---
aliases: 
---
# Bubblesort 
## Abstrakt
- S: Die zu sortierende Liste
### Invariante
Nach $i \geq 0$ Iterationen sind die elemente von S am ende von S an den richtigen Positionen
### Variante
i wird um 1 erhöht
### Abbruchbedingung
$i= |S|-1$
### Input
eine endliche geordnete Sequenz mit einer bestimmten Länge aus Elementen eines beliebigen Typs, Duplikate sind erlaubt
eine strenge schwache Ordnung "<" auf dem beliebigen Typ
### Output
eine Permutation der Sequenz mit den exakt gleichen Elementen wie vom Input, die gemäßt der Ordnung aufsteigend sortiert ist.
## Ablauf
Wir vergleichen von "vorne nach hinten" immer das Element mit dem nachfolgenden und falls dieses kleiner ist, vertauschen wir die beiden, bis wir am Ende angekommen sind. So schieben wir immer das größte Element der noch nicht sortierten Liste ganz ans ende. (Das Element steigt wie eine Blase auf)
## Komplexität
Asymptotische Komplexität $\Theta(T \cdot n^{2})$ im best und worst-case. T ist dabei die Komplexität des Komperators.

## FUCKY START
sobald wir `i=1` setzen ist der 1. fertig sortiert => fängt bei `i=0 j=0` an
## Links
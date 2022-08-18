---
aliases: 
---
# Mergesort 
## Abstrakt
- $S_{1}$: die erste vorsortierte Liste
- $S_{2}$: die zweite vorsortierte Liste
- $i_{1}$: der Pointer für die Liste $S_{1}$
- $i_{2}$: der Pointer für die Liste $S_{2}$
- $S$: Das Ergebnis
### Invariante
Vor und nach jeder Iteration vor der Termination:
$S$ besteht aus den Elementen, die wir von $S_{1}$ bzw $S_{2}$ herausgezogen haben
$S$ ist richtig sortiert
### Variante
$i_{1}+i_{2}$ erhöt sich immer um eins (Vor der Termination), weder $i_{1}$ noch $i_{2}$ werden kleiner
### Abbruchbedingung
$i_{1}=|S_{1}|$ oder $i_{2}=|S_{2}|$
## Ablauf
Wir vergleichen immer $S_{1}[i_{1}]$ mit $S_{2}[i_{2}]$ und fürgen das kleinere Element an $S$ an. Dann erhöhen wir den Pointer, von dem wir ein element genommen haben
## Komplexität
Die Komplexität ist $\Theta(T \cdot (|S_{1}|+|S_{2}|))$ im best und worst case. $T$ ist die Komplexität der Vergleichsoperation.

## Links
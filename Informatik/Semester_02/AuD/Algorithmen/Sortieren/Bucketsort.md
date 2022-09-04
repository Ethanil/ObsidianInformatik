---
aliases: 
---
# Bucketsort 
## Abstrakt
- S': Das am Ende sortierte Ergebnis
- B: Die Buckets die zum sortieren verwendet werden
- N: Die maximale Länge der Inputs
- A: Eine Liste der Inputs, wobei an Position 1 die Inputs der Länge 1 sind usw.
- M: Die Summe der Länge aller Inputs
### Invariante
Nach $i \geq 0$ Iterationen:
- A hat an seinen Positionen j die Strings der Länge j
- S' beinhaltet alle anderen Strings der Länge $N-i+1$, also alle schon aus A herausgenommenen. Sie sind sortiert nach dem Substring, der nach Position $N-i+1$ kommt.
- B ist leer
### Variante
i wird um 1 erhöt.
### Abbruchbedingung
N Iterationen sind abgeschlossen
## Ablauf
Wir nehmen immer eine "Gruppe" an längsten Strings aus A und sortieren sie nach ihrem letzten Buchstaben in B ein.
Danach fügen wir die Strings aus S' an der richtigen Stelle hinter den gerade hinzugefügten zu B hinzu (ohne die Reihenfolge der aus S' kommenden untereinander zu ändern).
## Komplexität
Die Asymptotische Komplexität ist $\Theta(M)$ im best und worst case.
## FUCKY START
Im 1. Induktionsschritt werden die Strings mit der größten Länge sortiert.

## Links
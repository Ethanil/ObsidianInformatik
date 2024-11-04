---
aliases: 
---
# Rechnen in Ganzen Zahlen, Primzahlen und Teiler
## Definition 2.1.1
Man sagt $p$ teilt $a$ und schreibt $p|a$ falls ein $m \in \mathbb{Z}$ exisitert mit $a=m\cdot p$ 
Eine natürliche Zahl $p>1$ heißt Primzahl, wenn $p$ nur durch $p$ und $1$ teilbar ist.
Die Zahl $ggT(a,b):=max\{q\in\mathbb{N} : q|a \text{ und } q|b\}$ heißt größter gemeinsamer Teiler von $a$ und $b$.
## Satz 2.1.2 (Division mit Rest)
Seien $a\in\mathbb{Z}$ und $b\in\mathbb{N}^*$. Dann gibt es eindeutig bestimmte Zahlen $q\in \mathbb{Z}$ und $r\in\{0,1,\dotso , b-1\}$ mit $a=q\cdot b+r$.
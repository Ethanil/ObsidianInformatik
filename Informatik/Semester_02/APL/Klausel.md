---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Klausel 
Eine Klausel ist eine endliche Menge an [[Literal|Literalen]]. Wir assoziieren mit der Klausel $C=\{L_1,\dotso,L_k\}$ die [[Disjunktion(oder)]] $\bigvee C \equiv L_{1} \lor \dotso \lor L_k$
Die leere Klausel $\square$ ist immer unerfüllbar($=0$).

## Klauselmenge
Eine endliche Klauselmenge steht für die [[Konjunktion(und)]] ihrer Klauseln. Für $K=\{C_1,\dotso,C_l\}$ ist $K \equiv C_{1}\land \dotso \land C_{l}$ eine [[Konjunktive und disjunktive Normalformen|KNF]]-Formel. Das heißt zu jeder endlichen [[Konjunktive und disjunktive Normalformen|KNF]]-Formel gehört eine [[Semester_02/APL/Logische Äquivalenz|äquivalente]] Klauselmenge.

## Beobachtungen
$C$ ist eine Klausel und $K$ eine Klauselmenge
Wenn $L$ und $\bar{L}$ aus $C$ sind, dann ist $C$ immer wahr ([[Grundlegende semantische Begriffe|Tautologie]])
Wenn $C\in K$ und $C \equiv 1$ dann ist $K \equiv K \backslash \{C\}$
Wenn die leere Klausel $\square$ in $K$ ist, dann ist $K$ nicht [[Erfüllbarkeit|erfüllbar]].
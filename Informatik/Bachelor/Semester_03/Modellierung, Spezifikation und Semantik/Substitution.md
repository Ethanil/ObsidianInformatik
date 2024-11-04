---
aliases: 
---
# Substitution 
Eine Substitution ist eine Funktion, mit einer endlichen Menge an Metavariablen als Definitionsvereich. Jedem dieser Metavariablen ist ein Ausdruck zugeordnet.

## Notation
$[MV_{1} \rightarrow \xi_{1}, \dotso, MV_{n} \rightarrow \xi_{n}]$
Hier werden den Metavariablen $MV_{1}$ bis $MV_{n}$ die Ausdrücke $\xi_{1}$ bis $\xi_{n}$ zugewiesen.

## Grundsubstitution
Wenn im Bildbereich keine Metavariablen vorkommen, heißt die Substitution Grundsubstitution.

## Substitutionsanwendung
Wenn wir eine Substitution $\eta$ auf einen beliebigen Ausdruck $\xi$ anwenden (Notation: $\xi \eta$), dann ist das Ergebnis ein Ausdruck, bei dem jedes freies Auftreten von Metavariablen in $\xi$ gemäß der Substitution $\eta$ ersetzt wurden.

```ad-example
title:Beispiel
collapse:
$$\begin{align}
&((&2& \oplus &X&) &\odot& (&Y& \ominus &X&))[X \rightarrow (Y \oplus 1), Y \rightarrow 0] \\\
=&((&2& \oplus &(Y \oplus 1)&)&\odot&(&0& \ominus &(Y \oplus 1)&))
\end{align}$$
```
## Links 
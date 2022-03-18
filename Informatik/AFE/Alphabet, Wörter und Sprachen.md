---
aliases: Alphabet, Alphabete, Alphabets, Wort, Wörter, Worts, Wörtern, Sprache, Sprachen
---
# Alphabet, Wörter und Sprachen
## Alphabet
Ein Alphabet ist eine endliche, nichtleere [[Mengen|Menge]] $\Sigma$. 
## Wörter
Aus diesem Alphabet können wir Wörter über Alphabet bilden, welche dann endliche Folgen von Buchstaben sind:
$$w=a_1\dotso a_n\ \ a_i\in \Sigma$$
### Länge
Jedes Wort hat eine bestimmte Länge, die mit Betragsstrichen gekennzeichnet ist:
$|w|$ ist also die Länge vom Wort $w$.
Wörter der Länge $n$ werden mit $n$-[[Tupel|Tupeln]] aus $\Sigma^n$ identifiziert.

### Menge aller Wörter über $\Sigma$
$$\Sigma^*:=\bigcup_{n\in\mathbb{N}}\Sigma^n$$
Das leere Wort $\epsilon$ ist immer Teil von $\Sigma^*$, also $\epsilon\in\Sigma^*$.
Wenn wir die Menge der nicht-leeren Wörter haben wollen schreiben wir:
$$\Sigma^+:=\Sigma^*\backslash\{\epsilon\}=\{w\in\Sigma^+:|w|\geq 1\}=\bigcup_{n\geq 1}\Sigma^n$$

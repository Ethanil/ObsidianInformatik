---
aliases: 
---
# Grammatik
Eine Grammatik ist eine Spezifikation einer Sprache durch Erzeugungsprozesse.
Diese Grammatik besteht aus einem Quatupel:
$$G=(\Sigma, V, P, X_0$$
- $\Sigma:=$ Terminalalphabet
- $V:=$ endliche Menge von Variablen, $V\cap \Sigma=\emptyset$
- $X_0 \in V:=$ Startvariable/Startsymbol
- $P:=$ endliche Menge von Produktionen, Regeln

$P\subseteq (V\cup\Sigma)^+ \times (V\cup\Sigma)^*$
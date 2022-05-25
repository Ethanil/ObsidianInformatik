---
aliases: 
---
# Terme 
Sei $S$ eine Signatur. Wir interessieren uns hier nur für die Funktions- und Konstantensymbole in $S$, also den funktionalen Anteil $S_{F}\subseteq S$. 
Terme sind korrekt geschachtelte Funktions-Ausdrücke aus Variablen, Konstanten und Funktionssymbolen, die Elemente von Strukturen beschreiben.
Variablensymbole sind vorübergehend vereinbarte Namen für diese Elemente.
```ad-abstract
title:Definition - $S$-Terme
Die Menge der *S-Terme*, $T(S)$ (mit Variablenmenge V) ist induktiv erzeugt wie folgt:
- $x \in T(S)$ für jede Variable $x \in V$
- $C \in T(S)$ für jedes Konstantensymbol $c \in S$
- ist $f \in S$ ein $n$-stelliges Funktionssymbol, und sind $t_{1},\dotso t_{n} \in T(S)$, so ist auch $ft_{1}\dotso t_{n} \in T(S)$
$T_{n}(S) \subseteq T(S):$ die Menge der Terme, in denen nur Variablensymbole aus $V_{n}=\{x_{1},\dotso c_{n}\}$ vorkommen.
```

## Links
[[Strukturen]]
[[Symbole]]
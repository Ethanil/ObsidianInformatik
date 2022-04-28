---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# offene Mengen 
In [[Normierte Räume|normierten Räumen]] spielen sogennante offene oder abgegeschlossene MEngen eine wichtige Rolle:
## Definitionen
```ad-abstract
title:Definition - offene Kugel
Es seien $x_{0}\in V$ und $r \in (0, \infty)$. Dann heißt die Menge

$$B_{r}(x_{0}):=\{x \in V: ||x-x_{0}||_{V}< r\}$$

(offene) Kugel um $x_{0}$ mit Radius $r$.
```

```ad-abstract
title:Definition - offene Menge
Eine Menge $M \subseteq V$ heißt offen, falls es für jeden Punkt $x_{0} \in M$ einen Radius $r>0$ gibt, so dass $B_{r}(x_{0})\subseteq M$ gilt.
```

```ad-abstract
title:Definition - abgeschlossene Menge
Eine Menge $M \subseteq V$ heißt abgeschlossen, wenn die Menge $M^{c}=V \backslash M$ offen ist.
```

```ad-abstract
title:Definition - innerer Punkt
Es sei $M \subseteq V$. Ein Punkt $x_{0}\in M$ heißt innerer Punkt von $M$, falls es ein $r>0$ gibt, so dass $B_{r}(x_{0})\subseteq M$ ist. Man nennt

$$M°:=\{x \in M: x \text{ innerer Punkt von }M\}$$

das Innere von M.
```

```ad-abstract
title:Definition
Eine Teilmenge $M$ von $V$ ist genau dann abgeschlossen, wenn für jede Folge in $M$, die in $V$ konvergiert, der Grenzwert ein Element aus $M$ ist.
```


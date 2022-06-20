---
aliases: 
---
# Konvexe Mengen, Schrankensatz 
```ad-abstract
title:Definition - konvexe Menge
Eine MEnge $M \subseteq \mathbb{R}^{d}$ heißt konvex, wenn für alle $a,b \in M$ auch $\overline{ab}\subseteq M$ gilt.
```
```ad-abstract
title:Definition - Schrankensatz
Es sei $G \subseteq \mathbb{R}^{d}$ offen und konvex, sowie $f: G \rightarrow \mathbb{R}$ total differenzierbar. Gibt es ein $L \geq 0$ mit $||\Delta f(x)||_{2}\leq L$ für alle $x \in G$, so gilt
$$\begin{align}
|f(x)-f(y)|\leq L|x-y|_{2}& &\text{für alle }x,y \in G
\end{align}$$
d.h. $f$ ist Lipschitz-stetig auf $G$
```

## Links
[[Mengen|Menge]]
[[Stetigkeit]]
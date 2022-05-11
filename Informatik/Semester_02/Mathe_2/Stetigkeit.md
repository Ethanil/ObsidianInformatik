---
aliases: 
---
# Stetigkeit 
```ad-abstract
title:Definition - Stetigkeit
Es sei $D \subseteq \mathbb{R}$ und $x_{0}in D$. Eine Funktion $f: D \rightarrow \mathbb{R}$ heißt stetig in $x_{0}$, falls für jede Folge $(a_{n})$ in $D$, die gegen $x_{0}$ konvergiert, auch die Folge $(f(a_{n}))$ konverigert und $\lim_{n\rightarrow \infty}f(a_{n})=f(x_{0})$ gilt.
Weiter heißt $f$ stetig auf $D$, wenn $f$ in jedem Punkt $x_{0}\in D$ stetig ist.
Schließlich setzen wir noch
$$\begin{align}
C(D):=\{f:D \rightarrow \mathbb{R}: f \text{ stetig auf }D\}
\end{align}$$
```
```ad-abstract
title:Definition
Es sei $D \subseteq \mathbb{R}$ und $f: D \rightarrow \mathbb{R}$ eine Funktion. Ist $x_{0} \in D$ ein Häufungspunkt von $D$, so ist $f$ in $x_{0}$ genau dann stetig, wenn
$$\begin{align}
\lim_{x\rightarrow x_{0}}f(x)=f(x_{0})
\end{align}$$
gilt.
```
````ad-abstract
title:Definition - Rechenregeln
collapse:
```ad-abstract
title:Definition - $+, \cdot, ||, /$
Es sei $D \subseteq \mathbb{R}$ und $f,g: D \rightarrow \mathbb{R}$ seien stetig in $x_{0} \in D$. Dann sind die Funktionen $f+g, fg$ und $|f|$ stetig in $x_{0}$
Ist $x_{0} \in D^{*:=\{x}\in D: g(x) \neq 0\}$, so ist die Funktion $\frac{f}{g:D^{*}\rightarrow}\mathbb{R}$ stetig in $x_{0}$
```
```ad-abstract
title:Definition - Verkettung von Funktionen
Es seien $D,E \subseteq \mathbb{R}$ und $f: D \rightarrow E$, sowie $g: E \rightarrow \mathbb{R}$ Funktionen. Ist $f$ stetig in $x_{0} \in D$ und $g$ stetig in $f(x_{0})$, so ist $g \circ f: D \rightarrow \mathbb{R}$ stetig in $x_{0}$
```
````


---
aliases: 
---
# Stetigkeit von Funktionen mehrerer Variablen 
````ad-abstract
title:Definition - Grenzwertbegriff für Funktionen zwischen [[Normierte Räume|normierten Räumen]]
Es seien $V$ und $W$ normierte $\mathbb{R}$-Vektorräume, $D \subseteq V$ und $f:D \rightarrow W$ eine Funktion.
```ad-abstract
title:
Wir nennen $x_{0} \in D$ Häufungspunkt von $D$, falls es eine Folge $(a_{n})$ in $D$ mit $a_{n}\neq x_{0}$ für alle $n \in \mathbb{N}$ gibt, die gegen $x_{0}$ konvergiert.
```
```ad-abstract
title:
Sei $x_{0}$ ein Häufungspunkt von $D$. Dann ist
$$\begin{align}
\lim_{x\rightarrow x_{0}} f(x) = y
\end{align}$$
falls für jede Folge $(a_{n})$ in $D$, die gegen $x_{0}$ konverigert und $a_{n}\neq x_{0}$ für alle $n \in \mathbb{N}$ erfüllt, die Folge $(f(a_{n}))$ gegen $y$ konvergiert.
```
````

```ad-abstract
title:Definition - Stetigkeit
Es seien $V,W$ zwei normierte $\mathbb{R}$-Vekotrräume $D \subseteq V$ und $x_{0}\in D$. Eine Funktion $f:D \rightarrow W$ heißt stetig in $x_{0}$, wenn für jede Folge $(a_{n})$ in $D$, die gegen $x_{0}$ konverigert, auch die Folge $(f(a_{n}))$ konvergiert und $\lim_{n\rightarrow \infty}f(a_{n})=f(x_{0})$ gilt.
Weiter heißt $f$ stetig auf $D$, wenn $f$ in jedem Punkt $x_{0}\in D$ stetig ist.
Außerdem setzen wir wieder
$$\begin{align}
C(D;W):=\{f:D \rightarrow W : f \text{ stetig auf }D\}
\end{align}$$
```
```ad-abstract
title:Definition - Stetigkeit aus der Stetigkeit einzelner Koordinaten
Es sei $D \subseteq \mathbb{R}^{d}$ und $x_{0} \in D$. Dann ist $f:D \rightarrow \mathbb{R}^{d}$ genau dann in $x_{0}$ stetig, wenn alle Koordinatenfunktionen $f_{1},f_{2},\dotso,f_{p}:D \rightarrow \mathbb{R}$ in $x_{0}$ stetig sind.
```
```ad-abstract
title:Definition - Rechenregeln
Es seien $D \subseteq \mathbb{R}^{d},x_{0} \in D$ und $f,g: D \rightarrow \mathbb{R}$ stetig in $x_{0}$, sowie $h:f(D) \rightarrow \mathbb{R}$ stetig in $f(x_{0}).$ Dann sind auch $f+g, fg, |f|$ und $h \circ f$ als Funktionen von $D$ nach $\mathbb{R}$ stetig in $x_{0}$
Ist außerdem $x_{0}\in D^{*}:=\{x \in D:g(x)\neq 0\}$, so ist auch $\frac{f}{g:D^{*}}\rightarrow \mathbb{R}$ stetig in $x_{0}$.
```

## Links
[[Normierte Räume]]
[[Vektorraum]]
[[Konvergenz in normierten Räumen]]
[[Stetigkeit]]

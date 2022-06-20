---
aliases: 
---
# Partielle Ableitungen 
Die direkte Definition über den [[Partielle Ableitungen|Differenzenqutienten]] ist nicht möglich, denn nun sind $x,x_{0}$ ja Vektoren und durch Vektoren kann man nicht teilen.
Wir versuchen den Differenzenquitienten zu retten, indem wir uns darauf beschränken mehrere eindimensionale Ableitungen zu berechnen, die zusammen das Verhalten der Funktion beschreiben sollen.
```ad-abstract
title:Definition - partielle Ableitung
Es sei $G \subseteq \mathbb{R}^{d}$ offen, $f: G \rightarrow \mathbb{R}^{p}$ eine Funktion, $x_{0}\in G$ und $v \in \mathbb{R}^{d}\backslash \{0\}$. Exisitert dann der Grenzwert
$$\begin{align}
(\partial_{v}f)(x_{0}):= \lim_{h\rightarrow 0}\frac{f(x_{0}+hv)-f(x_{0})}{h}
\end{align}$$
so heißt $f$ in $x_{0}$ in Richtung $v$ differenzierbar und $(\partial_{v}f)(x_{0})$ die Richtungsableitung von $f$ in Richtung $v$.
```
````ad-abstract
title:Definition - partielle Ableitung 2
Es seien $G \subseteq \mathbb{R}^{d}$ offen, $f:G \rightarrow \mathbb{R}^{p}$ eine Funktion und $\{e_{1},e_{2},\dotso,e_{d}\}$ die Standardbasis des $\mathbb{R}^{d}$
```ad-abstract
title:
Exisiteren in einem $x_{0}\in G$ die Richtungsableitungen von $f$ in alle Richtungen $e_{1},e_{2},\dotso,e_{d}$, so heißt $f$ in $x_{0}$ partiell differenzierbar. Man schreibt dann für $j=1,2,\dotso,d$ auch
$$\begin{align}
\partial_{j}f(x_{0}):=\frac{\partial f}{\partial x_{j}}(x_{0}):=f_{x_{j}}(x_{0}):=(\partial_{e_{j}}f)(x_{0})
\end{align}$$
für die partielle Ableitung von $f$ in $x_{0}$ nach der $j$-ten Koordinate
```
```ad-abstract
title:
Ist $f$ in allen $x_{0}\in G$ partiell differenzierbar, so sagt man $f$ ist in $G$ partiell differenzierbar und schreibt $\partial_{j}f=\frac{\partial f}{\partial x_{j}}=f_{x_{j}}:G \rightarrow \mathbb{R}^{p}$ fürn die partielle Ableitung(sfunktion)
```
```ad-abstract
title:
Ist $f$ in $G$ partiell differenzierbar und sind sämtliche partiellen Ableitungen $\partial_{1}f,\partial_{2}f,\dotso,\partial_{d}f:G \rightarrow \mathbb{R}^{p}$ stetig, so nennt man $f$ stetig partiell differenzierbar in $G$.
```
````
```ad-info
title:Bemerkung
Die praktische Berechnung der partiellen Ableitung ist einfach: Will man die $j$-te partielle Ableitung von $f$ bestimmen, so behandelnt man die anderen Variablen als konstante Parameter und leitet ganz wie gewohnt nach der einen Variablen ab.
```
```ad-abstract
title:Definition - Koordinatenfunktionen partiell diff & offen $\rightarrow$ $f$ in $x_{0}$ partiell diff
Ist $G \subseteq \mathbb{R}^{d}$ offen, $f: G \rightarrow \mathbb{R}^{p}$ eine Funktion und $x_{0} \in G$, so ist $f$ in $x_{0}$ genau dann partiell differenzierbar, wenn alle Koordinatenfunktionen $f_{1},f_{2},\dotso f_{p}:G \rightarrow \mathbb{R}$ in $x_{0}$ partiell differenzierbar sind. In diesem Fall gilt
$$\begin{align}
\partial_{j}f(x_{0})=(\partial_{j}f_{1}(x_{0}),\partial_{j}f_{2}(x_{0}),\dotso,\partial_{j}f_{p}(x_{0}))^{T}
\end{align}$$
```
## Links
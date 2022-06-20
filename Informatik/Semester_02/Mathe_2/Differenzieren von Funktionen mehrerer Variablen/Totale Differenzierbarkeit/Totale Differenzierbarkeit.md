---
aliases: 
---
# Totale Differenzierbarkeit 
Wir wollen das Differenziationsproblem im $\mathbb{R}^{d}$ noch mal ein weniger abstrakter betrachten.
```ad-abstract
title:Definition - Totale Differenzierbarkeit
Es sei $G \subseteq \mathbb{R}^{d}$ offen und $x_{0} \in G$. Eine Funktion $f: G \rightarrow \mathbb{R}^{p}$ heißt (total) differenzierbar in $x_{0}$, wenn es eine lineare Abbildung $\Phi: \mathbb{R}^{d}\rightarrow \mathbb{R}^{p}$ gibt, so dass gilt
$$\begin{align}
f(x)=f(x_{0})+\Phi(x-x_{0})+r(x),& &x \in G
\end{align}$$
mit einer Funktion $r: G \rightarrow \mathbb{R}^{p}$, die
$$\begin{align}
\lim_{x\rightarrow x_{0}}\frac{||r(x)||}{||x-x_{0}||}=0
\end{align}$$
erfüllt.
Die lineare Abbildung $Df(x_{0}):=\Phi$ heißt dann (totale) Ableitung von $f$ in $x_{0}$.
Ist $f$ in allen $x_{0}$ total differenzierbar, so nennt man die Funktion $Df:G \rightarrow \mathcal{L}(\mathbb{R}^{d},\mathbb{R}^{p})$ die Ableitung(sfunktion) von $f$
```
```ad-abstract
title:Definition - total differenzierbar und offen $\rightarrow$ stetig
Ist $G \subseteq \mathbb{R}^{d}$ offen und $f:G \rightarrow \mathbb{R}^{p}$ in $x_{0} \in G$ total differenzierbar, so ist $f$ auch stetig in $x_{0}$.
```
```ad-abstract
title:Definition - offen & total differenzierbar $\rightarrow$ Richtungsableitungen Exisiteren
Es sei $G \subseteq$ offen, $f: G \rightarrow \mathbb{R}^{p}$ eine in $x_{0} \in G$ total differenzierbare Funktion und $v \in \mathbb{R}^{d} \backslash \{0\}$. Dann exisitert in $x_{0}$ die Richtungsableitung von $f$ in Richtung $v$ und es gilt 
$$\begin{align}
(\partial_{v}f)(x_{0})=Df(x_{0})(v)
\end{align}$$
```
```ad-abstract
title:
Es sei $G \subseteq \mathbb{R}^{d}$ offen, $x_{0} in G$ und $f: G \rightarrow \mathbb{R}^{p}$ eine Funktion. Ist $f$ in $x_{0}$ total differenzierbar, so ist $f$ in $x_{0}$ auch partiell differenzierbar und die Abbildungsmatrix von $Df(x_{0})$ bezüglich der Standardbasen von $\mathbb{R}^{d}$ bzw. $\mathbb{R}^{p}$ ist die Jacobi-Matrix $J_{f}(x_{0})$
```
```ad-abstract
title:
Ist $G \subseteq math$
```
## Links
[[Jacobi-Matrix]]
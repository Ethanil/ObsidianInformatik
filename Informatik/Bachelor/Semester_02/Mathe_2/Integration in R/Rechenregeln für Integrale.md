---
aliases: 
---
# Rechenregeln für Integrale 
````ad-abstract
title:
Es seinen $a,b \in \mathbb{R}$ mit $a<b$ und integrierbare Funktionen $f,g: [a,b] \rightarrow \mathbb{R}$ gegeben. Dann gelten die folgenden Aussagen.
```ad-abstract
title:Definition - Monotonie
Ist $f(x)\leq g(x)$ für alle $x \in [a,b]$, so ist auch
$$\begin{align}
\int^{b}_{a}f(x)dx \leq \int^{b}_{a}g(x)dx
\end{align}$$
```
```ad-abstract
title:Definition - Homogenität
Ist $\alpha \in \mathbb{R}$, so ist auch $\alpha f$ integrierbar und es gilt
$$\begin{align}
\int^{b}_{a}\alpha f(x) dx=\alpha \int^{b}_{a}f(x) dx
\end{align}$$
```
```ad-abstract
title:Definition - Additivität
Auch die Funktion $f+g$ ist integrierbar und es gilt
$$\begin{align}
\int^{b}_{a}(f(x)+g(x))dx=\int^{b}_{a}f(x)dx+\int^{b}_{a}g(x)dx
\end{align}$$
```
```ad-abstract
title:Definition - Dreiecksungleichung
Die Funktion $|f|$ ist ebenfalls integrierbar und es gilt
$$\begin{align}
\left|\int^{b}_{a}f(x)dx\right|\leq \int^{b}_{a}|f(x)|dx
\end{align}$$
```
```ad-abstract
title:Definition - Aufteilung des Intervalls
Ist $c \in (a,b)$, so ist $f$ auch integrierbar auf $[a,b]$ und $[c,b]$ und es gilt
$$\begin{align}
\int^{b}_{a}f(x)dx=\int^{c}_{a}f(x)dx+\int^{b}_{c}f(x)dx
\end{align}$$
```
````
```ad-abstract
title:Definition - Standardabschätzung
Es seien $a,b \in \mathbb{R}$ mit $a<b$ und $f:[a,b]\rightarrow \mathbb{R}$ integrierbar. Dann ist
$$\begin{align}
\left|\int^{b}_{a}f(x)dx\right|\leq(b-a) \sup_{x \in [a,b]}|f(x)|=(b-a)||f||_{\infty}
\end{align}$$
```
```ad-abstract
title:
Es seien $a,b \in \mathbb{R}$ mit $a<b$ und $f:[a,b] \rightarrow \mathbb{R}$ sei integrierbar.
Dann setzt man für jedes $c \in [a,b]$
$$\begin{align}
\int^{c}_{c}f(x)dx:=0& &\text{und}& &\int^{a}_{b}f(x)dx:=-\int^{b}_{a}f(x)dx
\end{align}$$
```
```ad-abstract
title:
Es seien $a,b \in \mathbb{R}$ mit $a<b$. Jede stetige und jede monotone Funktion $f: [a,b] \rightarrow \mathbb{R}$ ist integrierbar.
```

## Links
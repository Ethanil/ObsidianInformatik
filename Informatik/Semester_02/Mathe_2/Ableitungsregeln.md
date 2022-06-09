---
aliases: 
---
# Ableitungsregeln 
Um kompliziertere Ableitungen zu berechnen, brauchen wir Rechenregeln:
```ad-abstract
title:Linearität
$\alpha f+\beta g$ ist in $x_{0}$ differenzierbar und
$$\begin{align}
(\alpha f +\beta g)'(x_{0})=\alpha f'(x_{0})+\beta g'(x_{0})
\end{align}$$
```
```ad-abstract
title:Produktregel
$fg$ ist differenzierbar in $x_{0}$ und
$$\begin{align}
(fg)'(x_{0})=f'(x_{0})g(x_{0})+f(x_{0})g'(x_{0})
\end{align}$$
```
```ad-abstract
title:Quotientenregel
Ist $g(x_{0})\neq 0$, so exisitert ein Intervall $J \subseteq I$ mit $x_{0} \in J$ und $g(x) \neq 0$ für alle $x \in J$. Außerdem ist die Funktion $\frac{f}{g:J}\rightarrow \mathbb{R}$ differenzierbar in $x_{0}$ und es gilt
$$\begin{align}
(\frac{f}{g})'(x_{0})=\frac{f'(x_{0})g(x_{0})-f(x_{0})g'(x_{0})}{(g(x_{0}))^{2}}
\end{align}$$
```
```ad-abstract
title:Kettenregel
Es seien $I,J \subseteq \mathbb{R}$ Intervalle und $g:I \rightarrow J$ sei differenzierbar in $x_{0} \in I$. Weiter sei $f: J \rightarrow \mathbb{R}$ differenzierbar in $y_{0}=g(x_{0})$. Dann ist auch die Funktion $f \circ g:I \rightarrow \mathbb{R}$ differenzierbar in $x_{0}$ und es gilt
$$\begin{align}
(f \circ g)'(x_{0})=f'(g(x_{0}))\cdot g'(x_{0})
\end{align}$$
```
```ad-abstract
title:Definition - Umkehrfunktion der Ableitung
Es sei $f \in C(I)$ streng monoton und in $x_{0} \in I$ differenzierbar mit $f'(x_{0}) \neq0$. Dann exisitert die Umkrehfunktion $f^{-1}:f(I)\rightarrow \mathbb{R}$, diese ist differenzierbar in $y_{0}=f(x_{0})$ und es gilt
$$\begin{align}
(f^{-1})(y_{0})=\frac{1}{f'(x_{0})}
\end{align}$$
```

## Links
[[Differenzierbarkeit von Funktionen in einer Variablen]]
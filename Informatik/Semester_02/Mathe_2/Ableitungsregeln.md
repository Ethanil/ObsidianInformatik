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
title:Definition - Ableitung von Polynomen
Es sei $f(x)=\sum^{\infty}_{n=0}a_{n}x^{n}$ eine Potenzreihe in $\mathbb{R}$ mit Konvergenzradius $r>0$. Dann hat auch die Potenzreihe $\sum^{\infty}_{n=1}na_{n}x^{n-1}$ den Konvergenzradius $r$, die Funktion $f$ ist in allen $x \in (-r,r)$ differenzierbar und es gilt
$$\begin{align}
f'(x)=\sum^{\infty}_{n=1}na_{n}x^{n-1},& &x \in (-r,r)
\end{align}$$
```
| Name               | Symbol    | Definitionsbereich                           | Bild                             | Ableitung                     |
| ------------------ | --------- | -------------------------------------------- | -------------------------------- | ----------------------------- |
| E-funktion         | $e$       | $\mathbb{R}$                                 | $(0,\infty)$                     | $e$                           |
| (nat.) Logarithmus | $\ln$     | $(0,\infty)$                                 | $\mathbb{R}$                     | $\frac{1}{x}$                 |
| Sinus              | $\sin$    | $\mathbb{R}$                                 | $[-1,1]$                         | $\cos$                        |
| Cosinus            | $\cos$    | $\mathbb{R}$                                 | $[-1,1]$                         | $-\sin$                       |
| Tangens            | $\tan$    | $\mathbb{R}\backslash\{(\frac{k+1}{2})\pi\}$ | $\mathbb{R}$                     | $\frac{1}{cos^{2}}=1+tan^{2}$ |
| Arcussinus         | $\arcsin$ | $[-1,1]$                                     | $[\frac{-\pi}{2},\frac{\pi}{2}]$ | $\frac{1}{\sqrt{1-x^{2}}}$    |
| Arcuscosinus       | $\arccos$ | $[-1,1]$                                     | $[0,\pi]$                        | $\frac{-1}{\sqrt{1-x^{2}}}$   |
| Arcustangens       | $\arctan$ | $\mathbb{R}$                                 | $(-\pi/2)$                                 |                               |
## Links
[[Differenzierbarkeit von Funktionen in einer Variablen]]
[[Potenzreihen]]
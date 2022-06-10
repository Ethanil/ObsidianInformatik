---
aliases: 
---
# Taylorreihe 
````ad-abstract
title:Definition - Taylorreihe
Es sei $I \subseteq \mathbb{R}$ ein offenes Intervall, $x_{0} \in I$ und $f \in C^{\infty}(I)$.
```ad-abstract
title:
Die Potenzreihe
$$\begin{align}
\sum^{\infty}_{n=0}\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}
\end{align}$$
heißt Taylorreihe von $f$ um $x_{0}$.
```
```ad-abstract
title:
Für jedes $k \in \mathbb{N}$ heißt das Polynom
$$\begin{align}
t_{k,f}(x;x_{0}):=\sum^{k}_{n=0}\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}
\end{align}$$
das Taylorpolynom $k$-ten Grades von $f$ in $x_{0}$.
```
````
````ad-abstract
title:Definition - Satz von Taylor
Es seien $I \subseteq \mathbb{R}$ ein offenes Intervall, $x,x_{0} \in I$ und für ein $k in \mathbb{N}_{0}$ sei $f: I \rightarrow \mathbb{R}$ eine $k+1$-mal differenzierbare Funktion. Dann gibt es ein $\xi$ zwischen $x$ und $x_{0}$, so dass gilt
$$ \begin{align}
f(x)=t_{k,f}(x;x_{0})+\frac{f^{(k+1)}(\xi)}{(k+1)!}(x-x_{0})^{k+1}
\end{align}$$
```ad-abstract
title:Definition - Fehlerterm/Restglied
Der Fehlerterm
$$\begin{align}
R_{k,f}(x;x_{0}):=\frac{f^{(k+1)}(\xi)}{(k+1)!}(x-x_{0})^{k+1}
\end{align}$$
der die Differenz zwischen $f(x)$ und der Näherung durch das Taylorpolynom $k$-ten Grades beschreibt, wird auch als Restglied bezeichnet.
```
````

## Links
[[Potenzreihen]]
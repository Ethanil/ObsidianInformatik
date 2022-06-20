---
aliases: 
---
# Jacobi-Matrix 
````ad-abstract
title:Definition - Jacobi-Matrix
Es sei $G \subseteq \mathbb{R}^{d}$ offen und $f: G \rightarrow \mathbb{R}^{p}$ in $x_{0} \in G$ partiell differenzierbar. Die $p \times d$-Matrix aller partiellen Ableitungen
$$J_{f}(x_{0}):=
\begin{pmatrix}
\partial_{1}f_{1}(x_{0}) & \partial_{2}f_{1}(x_{0}) & \dotso & \partial_{d}f_{1}(x_{0})\\
\partial_{1}f_{2}(x_{0}) & \partial_{2}f_{2}(x_{0}) & \dotso & \partial_{d}f_{2}(x_{0})\\
\vdots & \vdots & \vdots & \vdots\\
\partial_{1}f_{p}(x_{0}) & \partial_{2}f_{p}(x_{0}) & \dotso & \partial_{d}f_{p}(x_{0})\\
\end{pmatrix}$$
heißt Jacobi-Matrix von $f$
```ad-abstract
title:Gradient
Im Spezialfall $p=1$ nennt man die $1 \times d$-Matrix, d.h. den $\mathbb{R}^{d}$-Zeilenvektor
$$\Delta f(x_{0}):=J_{f}(x_{0})=(\partial_{1}f(x_{0}),\partial_{2}f(x_{0}),\dotso,\partial_{d}f(x_{0}))$$
den Gradient von $f$
```
````

## Links
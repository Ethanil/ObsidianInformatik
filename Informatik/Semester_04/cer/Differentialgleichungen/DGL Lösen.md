---
aliases: 
---
# DGL Lösen 
## Lösung im eindimensionalen Fall
```ad-example
title:Beispiel
$$\begin{align}
\dot{x}(t)=ax(t)\text{ mit }a \in \mathbb{R}, x \in \mathbb{R} \text{ und }x(t_{0})=x_{0}
\end{align}$$
```
### Lösungsansatz
$$\begin{align}
x(t)=xe^{\lambda t} \text{ gesucht: }c, \lambda \in \mathbb{R}
\end{align}$$
### Einsetzen
$$\begin{align}
\lambda c e^{\lambda t}=ace^{\lambda t} \stackrel{ce^{\lambda t}\neq 0}{\longrightarrow}\lambda = a
\end{align}$$
Die Konstante $c$ lässt sich über den Anfangswert $x_{0}$ bestimmen
## DGL 1.Ordnung mit höherer Dimension ($n > 1$)
```ad-example
title:Beispiel
$$\begin{align}
\dot{x}(t)=Ax(t)\text{ mit }A \in \mathbb{R}^{n times n} , x \in \mathbb{R} \text{ und }x^{n}(t_{0})=x_{0}
\end{align}$$
```
### Lösungsansatz
$$\begin{align}
x(t)=ve^{\lambda t} \text{ mit }v \in \mathbb{C}^{n}, \lambda \in \mathbb{C}
\end{align}$$
### Einsetzen
$$\begin{align}
\lambda v e^{\lambda t}=Ave^{\lambda t} \Leftrightarrow (\lambda I - A)ve^{\lambda t} = 0 \Leftrightarrow (\lambda I - A) v = 0
\end{align} $$
Die Konstante $c$ lässt sich über den Anfangswert $x_{0}$ bestimmen

## Links
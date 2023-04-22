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
\dot{x}(t)=Ax(t)\text{ mit }A \in \mathbb{R}^{n \times n} , x \in \mathbb{R} \text{ und }x^{n}(t_{0})=x_{0}
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
## Kochrezept
1. DGL in explizite Form bringen
> 	$\rightarrow c^{(p)}(t) = f(x^{(p-1)}(t),\dotso,x(t),t)=0$
1. Autonimisierung und Transformation auf 1. Ordnung
> $\dot{x}(t) = Ax(t) x \in \mathbb{R}^{n},A \in \mathbb{R}^{n \times n}$
4. Eigenwerte $\lambda_{i}$ von $A$ bestimmen
> $det(\lambda I-A)=0$
6. Eigenvektoren $v_{i}$ bestimmen
> $(\lambda_{i}I-A)v_{i}=0$
8. Allgemeine Lösung der DGL
> $x(t)=a_{1}v_{1}e^{\lambda_{1}t}+a_{2}v_{2}e^{\lambda_{2}t}+\dotso+a_{n}v_{n}e^{\lambda_{n}t}$
10. Spezielle Lösung der DGL
## Links
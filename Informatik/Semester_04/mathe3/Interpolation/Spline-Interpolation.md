---
aliases: 
---
# Spline-Interpolation 
Bei der Spline-Interpolation interpolieren wir die Funktion $f$ auf dem Intervall $[a,b]$, indem wir es stückweise so Interpolieren, dass die Stücke (also die Polynome) ineinander übergehen. Die Welligkeit der Interpolanten soll also möglichst klein sein. 
Sei $\Delta = \{x_{i}:a=x_{0}<x_{1}<\dotso<x_{n}=b\}$ eine Zerlegung des Intervalls $[a,b]$. $x_{i}$ nennen wir dann Knoten
```ad-abstract
title:Definition - Splinefunktion
Eine Splinefunktion der Ordnung $k$ zur Zerlegung $\Delta$ ist eine Funktion $s:[a,b] \rightarrow \mathbb{R}$ mit folgenden Eigenschaften
- Es gilt $s \in C^{k-1}([a,b]), s$ ist also stetig und $(k-1)$-mal stetig differenzierbar
- $s$ stimmt auf jedem Intervall $[x_{i},x_{i+1}]$ mit einem Polynom $s_{i}$ vom Grad $\leq k$ überein
```
Die Menge dieser Splinefunktionen bezeichnen wir mit $S_{\Delta,k}$.
```ad-abstract
title:Definition - Interpolationsbedingung
Zu einer Zerlegung $\Delta = \{x_{i}:a=x_{0}<x_{1}<\dotso<x_{n}=b\}$ und Werten $y_{i} \in \mathbb{R}, i=0,\dotso,n$ bestimme $s \in S_{\Delta,k}$ mit
$$\begin{align}
s(x_{i})=y_{i},&&i=0,\dotso,n
\end{align}$$
```
## Interpolation mit linearen Splines
Ein linearer Spline ist stetig und auf jedem Intervall ein Polynom vom Grad $\leq 1$. Die Interpolationsbedingung fordert daher $s_{i}(x_{i})=y_{i},s_{i}(x_{i+1})=y_{i+1}$ und legen $s_{i}$ somit eindeutig fest zu
$$\begin{align}
s(x)=s_{i}(x)=\frac{x_{i+1}-x}{x_{i+1}-x_{i}}y_{i}+\frac{x-x_{i}}{x_{i+1}-x_{i}}y_{i+1}&&\forall x \in [x_{i},x_{i+1}]
\end{align}$$
Wir definieren eine Dachfunktion, die für alle Werte links von dem Punkt links von uns (also ab $x_{i-2}$) und alle Werte rechts von dem Punkt rechts von uns (also ab $x_{i+2})$ den Wert $0$ festlegt
$$\begin{align}
\varphi_{i}(x)=\begin{cases}
0&&\text{falls }x<x_{i} \\
\frac{x-x_{i-1}}{x_{i}-x_{i-1}}&&\text{falls }x \in[x_{i-1},x_{i}] \\
\frac{x_{i+1}-x}{x_{i+1}-x_{i}}&&\text{falls }x \in[x_{i},x_{i+1}] \\
0&&\text{falls }x>x_{i+1}
\end{cases}
\end{align}$$
Damit erhalten wir dann folgende Darstellung
$$\begin{align}
s(x)=\sum^{n}_{i=0}y_{i}\varphi_{i}(x),&&x \in[a,b]
\end{align}$$

## Links
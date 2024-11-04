---
aliases: 
---
# Definition des bestimmten Integrals 
Wir wollen Flächen von krummlinig begrenzten Flächen berechnen, also unter eines Funktionsgraphen.
Die grundlegende Idee nach Riemann ist es, die Fläche unter dem Graphen durch Aufsummieren von Rechtecken anzunähern. Dabei können wir von oben (Obersumme) und von unten (Untersumme) annähern.
````ad-abstract
title:Definition - Zerlegung eines Intervalls
Es seien $a,b \in \mathbb{R}$ mit $a<b$. Eine endliche Menge $Z:=\{x_{0},x_{1},\dotso,x_{n}\} \subseteq [a,b]$ heißt Zerlegung des Intervalls $[a,b]$, wenn gilt
$$\begin{align}
a=x_{0}<x_{1}<x_{2}<\dotso <x_{n-1}< x_{n}=b
\end{align}$$
```ad-abstract
title:
Für eine solche Zerlegung und eine gegebene beschränkte Funktion $f:[a,b]\rightarrow \mathbb{R}$ setzen wir nun für jedes $j=1,\dotso,n$
$$\begin{align}
I_{j}:=[x_{j-1},x_{j}],& &|I_{j}|:=x_{j}-x_{j-1}& &m_{j}:=\inf f(I_{j})& &M_{j}:=\sup f(I_{j})
\end{align}$$
```
````
Mit Hilfe dieser Notation können wir nun die oben erwähnte Ober- und Untersumme definieren
```ad-abstract
title:Definition - Ober und Untersumme
Es seien $a,b \in \mathbb{R}$ mit $a<b, Z=\{x_{0},\dotso,x_{n}\}$ eine Zerlegung von $[a,b]$ und $f:[a,b]\rightarrow \mathbb{R}$ beschränkt. Dann heißt der Wert
$$\begin{align}
\underline{s}_{f}(Z):=\sum^{n}_{j=1}m_{j}|I_{j}|& &\text{die Untersumme von $f$ zu $Z$ und}\\
\overline{s}_{f}(Z):=\sum^{n}_{j=1}M_{j}|I_{j}|& &\text{die Obersumme von $f$ zu $Z$}
\end{align}$$
```
````ad-abstract
title:Definition - oberers und unteres Integral
Es seien $a,b \in \mathbb{R}$ mit $a<b$ und $f:[a,b] \rightarrow \mathbb{R}$ sei beschränkt.
Wir nennen
$$\begin{align}
\underline{\int^{b}_{a}}f(x)dx:=\sup\{\underline{s}_{f}(Z):Z \text{Zerlegung von }[a,b]\}
\end{align}$$
unteres Integral von $f$ auf $[a,b]$ und
$$\begin{align}
\overline{\int^{b}_{a}}f(x)dx:=\sup\{\overline{s}_{f}(Z):Z \text{Zerlegung von }[a,b]\}
\end{align}$$
oberes Integral von $f$ auf $[a,b]$
```ad-abstract
title:Definition - Riemann-Integral
Weiter heißt $f$ auf $[a,b]$ (Riemann-)integrierbar, wenn
$$\begin{align}
\underline{\int^{b}_{a}}f(x)dx=\overline{\int^{b}_{a}}f(x)dx
\end{align}$$
gilt. In diesem Fall nennen wir
$$\begin{align}
\int^{b}_{a}f(x)dx:=\underline{\int^{b}_{a}}f(x)dx
\end{align}$$
das (Riemann-)Integral von $f$ auf $[a,b]$
```
````

## Links
---
aliases: 
---
# Höhere Ableitungen 
Beispielsweise
$$\begin{align}
f(x):=
\begin{cases}
x^{\frac{3}{2}}\sin(\frac{1}{x}),& &\text{falls }x>0,\\
0,& &\text{falls }x=0
\end{cases}
\end{align}$$
![[Pasted image 20220609175035.png]]

```ad-abstract
title:Definition - Stetig differenzierbar
Ist $f:I \rightarrow \mathbb{R}$ eine in $I$ differenzierbare Funktion und ist $f'$ auf $I$ stetig, so nennt man $f$ stetig differenzierbar.
Man schreibt $C^{1}(I):=\{f:I \rightarrow \mathbb{R}: f \text{ stetig differenzierbar}\}$
```
````ad-abstract
title:Definition - n-te Ableitung
```ad-abstract
title:
Es sei $f: I \rightarrow \mathbb{R}$ differenzierbar auf $I, x_{0} \in I$ und $n \in \mathbb{N}$ mit $n \geq 2$. Dann heißt die Funktion $f$ in $x_{0}$ (bzw. auf $I$) $n$ mal differenzierbar, falls sie auf $I$ schon $(n-1)$ mal differenzierbar ist und die Funktion $f^{(n-1)}$ in $x_{0}$ (bzw. auf $I$) wieder differenzierbar ist.
In diesem Fall heißt $f^{(n)}(x_{0})=(f^{(n-1)})'(x_{0})$ die $n$-te Ableitung von $f$ in $x_{0}$ bzw. $x \mapsto f^{(n)}(x)$ die $n$-te Ableitungsfunktion von $f$ auf $I$. 
```
```ad-abstract
title:
Ist die $n$-te Ableitung von $f$ auf $I$ selbst sogar wieder stetig auf $I$, so sagt man $f$ sei $n$-mal stetig differenzierbar auf $I$. Man schreibt
$$\begin{align}
C^{n}(I):=\{f:I \rightarrow \mathbb{R}:f n-\text{mal stetig differenzierbar}\}
\end{align}$$
```
```ad-abstract
title:
Ist $f \in C^{n}(I)$ für alle $n \in \mathbb{N}$, so nennt man $f$ beliebig oft differenzierbar. Man verwendet dafür auch die Bezeichnung
$$\begin{align}
f \in C^{\infty}(I):=\bigcap_{n \in \mathbb{N}}C^{n}(I).
\end{align}$$
```
````

## Links
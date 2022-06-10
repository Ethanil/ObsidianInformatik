---
aliases: 
---
# Eigenschaften differenzierbarer Funktionen 
```ad-abstract
title:Definition - Mittelwertsatz der Differenzialrechnung
Es seien $a,b \in \mathbb{R}$ mit $a > b$ und $f \in C([a,b])$ sei differenzierbar in $(a,b)$. Dann gibt es ein $xi \in (a,b)$, so dass
$$\begin{align}
\frac{f(b)-f(a)}{b-a}=f'(\xi)& &\text{bzw. gleichbedeutend }& &f(b)-f(a)=f'(\xi)(b-a)
\end{align}$$
gilt.
Der Satz bedeutet, dass die Sekantensteigung der Funktion, die man anhand der beiden Punkte $a$ und $b$ erhält, irgendwann zwischen den beiden Punkten wirklich als Tangentensteigung angenommen wird.
```
````ad-abstract
title:Definition - Satz von Rolle
```ad-abstract
title:
Es seien $a,b \in \mathbb{R}$ mit $a<b$ und $f \in C([a,b])$. Ist $f$ auf $(a,b)$ differenzierbar und gilt $f(a)=f(b)$, so gibt es ein $\xi \in (a,b)$ mit $f'(\xi)=0$
```
```ad-abstract
title:
Es sei $f: I \rightarrow \mathbb{R}$ auf dem Intervall $I$ differenzierbar. Dann gilt
- Ist $f'=0$ auf $I$, so ist $f$ auf $I$ konstant.
- Ist $f'>0$ auf $I$, so ist $f$ auf $I$ streng monoton wachsend.
- Ist $f'<0$ auf $I$, so ist $f$ auf $I$ streng monoton fallend.
- Ist $f'\geq0$ auf $I$, so ist $f$ auf $I$ monoton wachsend.
- Ist $f'\leq0$ auf $I$, so ist $f$ auf $I$ monoton fallend.
```
```ad-abstract
title:
Sind $f,g: I \rightarrow \mathbb{R}$ differenzierbare Funktionen und gilt $f'=g'$ auf $I$, so gibt es eine Konstante $c \in \mathbb{R}$, so dass $f(x)=g(x)+c$ für alle $x \in I$ gilt.
```
````
```ad-abstract
title:Definition - Satz von de l'Hospital
Es sei $(a,b)$ ein offenes Intervall in $\mathbb{R}$ (dabei ist hier $a=- \infty$ oder $b=\infty$ zugelassen) und $f,g:(a,b) \rightarrow \mathbb{R}$ seien differenzierbar auf $(a,b)$ mit $g'(x) \neq 0$ für alle $x \in (a,b)$. Gitl dann
$$\begin{align}
\lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=0& &\text{oder}& &\lim_{x\rightarrow a}f(x)=\lim_{x\rightarrow a}g(x)=\pm \infty
\end{align}$$
und exisitert der Grenzwert
$$L:=\lim_{x\rightarrow a}f'\frac{x}{g'(x)}$$
(hierbei ist wieder $L=\pm \infty$ zugelassen), dann gilt
$$\lim_{x\rightarrow a}f\frac{x}{g(x)}=L$$
```
## Links
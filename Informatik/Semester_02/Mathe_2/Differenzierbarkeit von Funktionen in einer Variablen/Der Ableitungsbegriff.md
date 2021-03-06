Differenzierbarkeit von Funktionen in einer Variablen 
​￼## Der Ableitungsbegriff---
aliases: 
---
# Der Ableitungsbegriff
Die Ableitung beschreibt das Änderungsverhalten einer Funktion in einem Punkt, d.h. die Steigung des Fuinktionsgraphen.
`````ad-abstract
title:Definition - Differenzierbarkeit
````ad-abstract
title:
Es sei $x_{0} \in I$. Eine Funktion $f:I \rightarrow \mathbb{R}$ heißt differenzierbar in $x_{0}$, wenn der Grenzwert
$$\begin{align}
\lim_{x \rightarrow x_{0}}\frac{f(x)-f(x_{0})}{x-x_{0}}
\end{align}$$
in $\mathbb{R}$ exisitert. In diesem Fall heißt der Grenzwert die Ableitung von $f$ in $x_{0}$ und wird mit $f'(x_{0})$ bezeichnet.
```ad-abstract
title:
Der obige Grenzwert exisitert genau dann, wenn der Grenzwert
$$\begin{align}
\lim_{h \rightarrow 0} \frac{f(x_{0}+h)-f(x_{0})}{h}
\end{align}$$
exisitert. Die Werte der beiden stimmen dann überein.
```
````
````ad-abstract
title:
Eine Funktion $f: I \rightarrow \mathbb{R}$ heißt differenzierbar auf $I$, falls sie in allen Punkten $x_{0} \in I$ differenzierbar ist. In diesem Fall wird durch $x \mapsto f'(x)$ für $x \in I$ eine Funktion $f': I \rightarrow \mathbb{R}$ definiert. Diese Funktion heißt die Ableitung oder auch Ableitungsfunktion von $f$ auf $I$.
````
`````

```ad-abstract
title:Definition - Differenzierbarkeit $\rightarrow$ stetig
Es sei $f: I \rightarrow \mathbb{R}$ differenzierbar. Dann ist $f$ stetig in $x_{0}$.
```

```ad-abstract
title:Definition - Differenzierbarkeit 2.0
Eine Funktion $f: I \rightarrow \mathbb{R}$ ist in $x_{0} \in I$ genau dann differenzierbar mit $f'(x_{0})=a$, wenn
$$\begin{align}
f(x)=f(x_{0})+a(x-x_{0})+r(x),& &x \in I
\end{align}$$
ist und für die Funktion $r:I \rightarrow \mathbb{R}$ gilt
$$\begin{align}
\lim_{x\rightarrow x_{0}}\frac{|r(x)|}{|x-x_{0}|}=0
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
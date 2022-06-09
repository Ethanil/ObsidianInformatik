---
aliases: 
---
# Differenzierbarkeit von Funktionen in einer Variablen 
## Der Ableitungsbegriff
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

## Links
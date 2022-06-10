---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Cauchy-Produkt 
Das Cauchy-Produkt gilt für [[Absolute Konvergenz|absolut konvergierende]] [[Reihen]] und besagt:
```ad-abstract
title:$$\sum^\infty_{n=0}\sum^n_{k=0}a_kb_{n-k}=\left(\sum^\infty_{n=0}a_n\right)\left(\sum^\infty_{n=0}b_n\right)$$
```
Das Cauchy-Produkt von zwei [[Absolute Konvergenz|absolut konvergenten]] Reihen ist auch [[Absolute Konvergenz|absolut konvergent]]
## Funktionalgleichung der Exponentialfunktionen
```ad-example
title:Beweis
collapse:
Für alle $z,w \in \b{C}$ gilt $E(z+w)=E(z)E(w)$.
Da alle beteiligten [[Reihen]] [[Absolute Konvergenz|absolut konvergent]] sind gilt:
$$\begin{align}
E(z)E(w) &= \left(\sum^{\infty}_{n=0}\frac{z^n}{n!}\right)\left(\sum^{\infty}_{n=0}\frac{w^n}{n!}\right)
&&=\sum^{\infty}_{n=0}\sum^{n}_{k=0}\frac{z^k}{k!}\frac{w^{n-k}}{(n-k)!}\\
&=\sum^{\infty}_{n=0}\frac{1}{n!}\sum^{n}_{k=0}\frac{n!}{k!(n-k)!}z^kw^{n-k}&&=\sum^{\infty}_{n=0}\frac{1}{n!}\sum^{n}_{k=0}\begin{pmatrix}
n \\ k
\end{pmatrix}
z^kw^{n-k}
\end{align}$$
Nach der [[Binomialformel]] gilt:
$$\sum^{n}_{k=0}\begin{pmatrix}
n \\ k
\end{pmatrix}z^{k}w^{n-k}=(z+w)^n$$
also zusammengefasst:
$$E(z)E(w)=\sum^{\infty}_{n=0}\frac{(z+w)^{n}}{n!}=E(z+w)$$
```

```ad-abstract
title: Funktionalgleichung
$$\begin{align}
\text{Für alle }z\in\mathbb{C}\text{ ist}\\
e^z:=E(z)= \sum^{\infty}_{n=0}\frac{z^n}{n!}
\end{align}$$
```

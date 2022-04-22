---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Cauchy-Produkt 
Das Cauchy-Produkt gilt für [[Absolute Konvergenz|absolut konvergierende]] [[Reihen]] und besagt:
```ad-abstract
title:$$\sum^\infty_{n=0}\sum^n_{k=0}a_kb_{n-k}=\left(\sum^\infty_{n=0}a_n\right)\left(\sum^\infty_{n=0}b_n\right)$$
```

```ad-example
title:Anwendungsbeispiel
Für alle $z,w \in \b{C}$ gilt $E(z+w)=E(z)E(w)$.
Da alle beteiligten [[Reihen]] [[Absolute Konvergenz|absolut konvergent]] sind gilt:
$$\begin{align}
E(z)E(w) &= \left(\sum^{\infty}_{n=0}\frac{z^n}{n!}\right)\left(\sum^{\infty}_{n=0}\frac{w^n}{n!}\right)
&&=\sum^{\infty}_{n=0}\sum^{n}_{k=0}\frac{z^k}{k!}\frac{w^{n-k}}{(n-k)!}\\
&=\sum^{\infty}_{n=0}\frac{1}{n!}\sum^{n}_{k=0}\frac{n!}{k!(n-k)!}z^kw^{n-k}&&=\sum^{\infty}_{n=0}\frac{1}{n!}\sum^{n}_{k=0}
\end{align}$$
```

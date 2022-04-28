---
aliases: Reihe
---
# Reihen
## Definition
Es sei $(a_n)$ eine [[Folge]] in $\mathbb{K}$. Dann heißt
$$\sum^\infty_{n=0}a_n=a_0+a_1+a_2+a_3+\dotso$$
die Reihe über $(a_n)$.
Wenn die Folge nur bis $k$, anstatt $\infty$ geht, dann ist dies die $k$-te Teilsumme der Reihe.
## Konvergenzkriterien
```ad-abstract
title:Definition - 2 konvergente Reihen konvergieren
Seien $\sum^\infty_{n=0}a_n$ und $\sum^\infty_{n=0}b_n$ zwei **konvergente** Reihen in $\mathbb{K}$ und $\alpha,\beta\in \mathbb{K}$. Dann ist $\sum^\infty_{n=0}(\alpha a_n+\beta b_n)$ **konvergent** und es gilt:
$$\sum^\infty_{n=0}(\alpha a_n+\beta b_n)=\alpha \sum^\infty_{n=0}a_n+\beta \sum^\infty_{n=0}b_n$$
```

```ad-abstract
title:Definition - Folgen von konvergenten Reihen sind Nullfogen
Ist $\sum^\infty_{n=0}a_n$ eine konvergente Reihe in $\mathbb{K}$, so ist $(a_n)$ eine Nullfolge in $\mathbb{K}$.
```

```ad-abstract
title:Definition - Monotonie-Kriterium
Es seien $(a_n)$ eine Folge in $\mathbb{K}$ und $s_k:=\sum^k_{n=0}a_n,k\in \mathbb{N}$. Dann gilt
- Ist $a_n\geq 0$ für alle $n\in\mathbb{N}$ und $(s_k)_{k\in\mathbb{N}}$ nach oben beschränkt, so ist $\sum^\infty_{n=0}a_n$ konvergent. 
```

```ad-abstract
title:Definition - Cauchy-Kriterium
Es seien $(a_n)$ eine Folge in $\mathbb{K}$ und $s_k:=\sum^k_{n=0}a_n,k\in \mathbb{N}$. Dann gilt
- Die Reihe zur Folge ist genau dann konvergent, wenn für jedes $\epsilon > 0$ ein $n_0\in\mathbb{N}$ exisitert mit
$$\left|\sum^{k_{n=l+1}}a_n\right|<\epsilon\text{ für alle $k,l\in\mathbb{N}$ mit }k>l\geq n_0$$
```

```ad-abstract
title:Definition - Leibniz-Kriterium
Es sei $(a_n)$ eine monoton fallende Folge in $\mathbb{R}$ mit $lim_{n\rightarrow\infty}a_n=0$. Dann ist die Reihe $\sum^\infty_{n=0}(-1)^na_n$ konvergent.
```

````ad-abstract
title:Definition - Major- und Minorantenkriterium
Es seien $(a_n)$ und $(b_n)$ reelle [[Folge|Folgen]] und $n_0\in\mathbb{N}$.
```ad-abstract
title:Definition - Majorantenkriterium
Ist $|a_n|\leq b_n$ für alle $n\geq n_0$ und konvergiert die Reihe $\sum^\infty_{n=0}b_n$, so ist $\sum^\infty_{n=0}a_n$ absolut konvergent
```
```ad-abstract
title:Definition - Minorantenkriterium
Ist $a_n\geq b_n \geq 0$ für alle $n\geq n_0$ und divergiert die Reihe $\sum^\infty_{n=0}b_n$, so divergiert auch die Reihe $\sum^\infty_{n=0}a_n$.
```
````

```ad-abstract
title:Definition - Wurzelkriterium
Existiert der Grenzwert $lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}$ so ist die Reihe
- [[Absolute Konvergenz|absolut konvergent]], wenn $lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}<1$ ist
- divergent, wenn $lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}>1$ ist.
```

```ad-abstract
title:Definition - Quotientenkriterium
Ist $a_n\neq 0$ für alle $n\in\mathbb{N}$ und existiert der Grenzwert $lim_{n\rightarrow\infty}|a_{n+1}/a_n|$  so ist die Reihe
- [[Absolute Konvergenz|absolut konvergent]], wenn $lim_{n\rightarrow\infty}\frac{|a_{n+1}|}{|a_n|}<1$ ist
- divergent, wenn $lim_{n\rightarrow\infty}\frac{|a_{n+1}|}{|a_n|}>1$ ist
```

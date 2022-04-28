---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Konvergenz in normierten Räumen 
[[Folge|Folgen]] und [[Reihen]] können nicht nur in $\mathbb{R}$ oder $\mathbb{C}$, sondern auch in  $\mathbb{R}^d$ oder $\mathbb{C}^d$ für $d \in \mathbb{N}^*$ betrachtet werden.
Für den Begriff der Konvergenz benötigen wir eine Form Abstände messen zu können, was wir schon von den [[Normierte Räume|normierten Räumen]] kennen.
$V$ steht für einen normierten $\mathbb{R}$-Vektorraum
## Definitionen
```ad-abstract
title:Definition - konvergente Folgen
Eine [[Folge]] $(a_n)_{n\in \mathbb{N}}$ in $V$ heißt konvergent gegen ein $a \in V$, wenn für jedes $\epsilon > 0$ ein $n_{0}\in \mathbb{N}$ exisitert, so dass

$$||a_n-a||_V<\epsilon \text{ für alle }n \geq n_{0}$$
gilt.
Die Folge heißt divergent, wenn sie nicht konvergent ist.
```
```ad-abstract
title:Definition - Cauchy Folge
Eine Folge $(a_n)_{n \in \mathbb{N}}$ in $V$ heißt Cauchy-Folge, wenn es für jedes $\epsilon>0$ ein $n_{0}\in \mathbb{N}$ gibt mit

$$||a_n-a_m||_{V}<\epsilon \text{ für alle }n,m \geq n_0$$
```
```ad-abstract
title:Definition - konvergente Reihen
Eine Reihe $\sum^{\infty}_{n=0} a_n$ in $V$ heißt konvergent mit Reihenwert $s \in V$, wenn die Folge der Partialsummen $s_k:=\sum^{k}_{n=0}a_{n,}k \in \mathbb{N}$, in $V$ gegen $s$ konvergiert.
Konvergiert die Reihe $\sum^{\infty}_{n=0}||a_n||_V$ in $\mathbb{R}$, so heißt die Reihe $\sum^{\infty}_{n=0}a_n$ absolut konvergent.
Ist die Reihe nicht konvergent, so nennt man sie divergent.
```
```ad-abstract
title:Definition - beschränkte Mengen
Eine Menge $M \subseteq V$ heißt beschränkt, falls es ein $C \geq 0$ gibt, so dass $||x||_{V}\geq C$ für alle $x \in M$ gilt.
```
```ad-abstract
title:Definition - Konvergenz aller Koordinatenfolge $\Leftrightarrow$ Konvergenz der Folge
Es sei $(a_n)_{n \in \mathbb{N}}=((a_{n,1},a_{n,2},\dotso,a_{n,d})^{T)_{n}\in \mathbb{N}}$ eine Folge in $\mathbb{R}^d$ mit der [[Normierte Räume#2-Norm|2-Norm]] $||x||_2=\sqrt{x^2_1+x^2_2+\dotso+x^2_d}$. Dann ist $(a_n)$ in $\mathbb{R}^d$ genau dann konvergent, wenn für jedes $j \in \{1,2,\dotso,d\}$ die Kooradinatenfolge $(a_{n,j})_{n \in \mathbb{N}}$ in $\mathbb{R}$ konverget ist. In diesem Fall ist
$$lim_{n \rightarrow \infty}$$
```

---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Konvergenz in normierten Räumen 
[[Folge|Folgen]] und [[Reihen]] können nicht nur in $\mathbb{R}$ oder $\mathbb{C}$, sondern auch in  $\mathbb{R}^d$ oder $\mathbb{C}^d$ für $d \in \mathbb{N}^*$ betrachtet werden.
Für den Begriff der Konvergenz benötigen wir eine Form Abstände messen zu können, was wir schon von den [[Normierte Räume|normierten Räumen]] kennen.
$V$ steht für einen normierten $\mathbb{R}$-Vektorraum
```ad-abstract
title:Definition
Eine [[Folge]] $(a_n)_{n\in \mathbb{N}}$ in $V$ heißt konvergent gegen ein $a \in V$, wenn für jedes $\epsilon > 0$ ein $n_{0}\in \mathbb{N}$ exisitert, so dass

$$||a_n-a||_V<\epsilon \text{ für alle }n \geq n_{0}$$
gilt.
Die Folge heißt divergent, wenn sie nicht konvergent ist.
```
```ad-abstract
title:Definition
Eine Folge $(a_n)_{n \in \mathbb{N}}$ in $V$ heißt Cauchy-Folge, wenn es für jedes $\epsilon>0$ ein $n_{0}\in \mathbb{N}$ gibt mit

$$||a_n-a_m||_{V}<\epsilon \text{ für alle }n,m \geq n_0$$
```
```ad-abstract
title:Definition
Eine Reihe $\sum^{\infty}_{n=0} a_n$ in $V$ heißt konvergent mit Reihenwert $s \in V$, wenn die Folge der Partialsummen $s_k:=\sum^{k}_{n=0}a_{n,}k \in \mathbb{N}$, in $V$ gegen $s$ konvergiert.
Konvergiert die Reihe $\sum^{\infty}_{n=0}||a_n||_V$ in $\mathbb{R}$, so heißt die Reihe $\sum^{\infty}_{n=0}a_n$ absolut konvergent.
Ist die Reihe nicht konvergent, so nennt man sie divergent.
```

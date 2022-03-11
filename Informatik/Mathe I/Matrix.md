---
aliases: 
---
# Matrix
Eine $p\times n$-Matrix hat $p$ Zeilen und $n$ Spalten:
$$A=\begin{pmatrix}
\alpha_{11} & \alpha_{12} & \cdots & \alpha_{1n} \\
\alpha_{21} & \alpha_{22} & \cdots & \alpha_{2n} \\
\vdots & \vdots & \cdots & \vdots \\
\alpha_{p1} & \alpha_{p2} & \vdots & \alpha_{pn} \\
\end{pmatrix} = (\alpha_{jk})_{j=1,\dotso,p,k=1,\dotso,n}$$
## Addition
Matrizen werden komponentenweise addiert.

## Skalar-Multiplikation
Die Skalar-Multiplikation ist auch komponentenweise.

## Matrixmultiplikation
Zwei Matrizen, welche aus dem selben [[Körper]] sind, können wie folgt multipliziert werden:
$$A=(\alpha_{jl})_{j=1,\dotso,q,l=1,\dotso,p}\in 
K^{q\times p} $$
$$
B=(\beta {lk})_{l=1,\dotso,p,k=1,\dotso,n}\in 
K^{p\times n}
$$
$$AB:=\left(\sum^p_{l=1}\alpha_{jl}\beta_{lk}\right)_{j=1,\dotso,q,k=1,\dotso,n}$$
Also die erste Matrix(die linke) muss gleich viele Spalten haben wie die zweite Matrix(die rechte) Zeilen hat.

## Einheitsmatrix
Bei quadratischen Matrizen ist die Addition und Multiplikation ein [[Ring|Ring mit Eins]], der für $n\geq2$ nicht [[Ring|kommutativ]] ist.
Die Eins ist hierbei die sogenannte Einheitsmatrix $I$, die wie folgt aussieht:
$$I:=\begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{pmatrix}$$
## Transponierte Matrix
Eine an der Diagonalen gespiegelte Matrix heißt transponiert:
$$\begin{pmatrix}
3 & 2 & 5 \\
1 & 2 & 3 
\end{pmatrix}^T=
\begin{pmatrix}
3 & 1 \\
2 & 2 \\
5 & 3
\end{pmatrix}$$
- $(A+B)^T=A^T+B^T$
- $(A^T)^T=A$
- $(\lambda A)^T=\lambda A^T$
- Für alle $A\in K^{q\times p}$ und $B\in K^{p\times n}$ gilt $(AB)^T=B^TA^T$

## [[Abbildung|Abbildungs]]matrix
Eine Abbildungsmatrix $\phi$ bezüglich zwei [[Basis|Basen]] $B,C$ von zwei $K$-Vektorräumen $V\rightarrow W$  bezeichnen wir als
$$A=:M^B_C(\phi)$$
```ad-note
collapse:true
title: Merkregel
In den Spalten der Abbildungsmatrix stehen die Koordinaten der Bilder der Basisvektoren
```
Eine Abbildungsmatrix ist also nichts anderes als eine andere Art eine [[Lineare Abbildungen|Lineare Abbildung]] darzustellen. Alles was für das eine gilt, gilt also auch für das andere!
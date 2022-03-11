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
\vdots & \vdots & \ldots 
\end{pmatrix}$$
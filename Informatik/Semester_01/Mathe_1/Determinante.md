---
aliases: 
---
# Determinante
- Es seien $A\in K^{n\times n}$ und $j,k\in \{1,2,\dotso,n\}$. Dann bezeichne $A_{jk}\in K^{(n-1)\times (n-1)}$ die Matrix, die aus $A$ durch Streichen der $j$-ten Zeile under $k$-ten Spalte entsteht.
- Für $A=(\alpha)\in K^{1\times 1}$ definieren wir die Determinante durch $det(A):=\alpha$
- Für ein $A=(\alpha_{jk})^n_{j,k=1}\in K^{n\times n}$ mit $n>1$ erklären wir die Determinante als
$$det(A)=\sum^n_{k=1}(-1)^{1+k}\alpha_{1k}det(A_{1k}) \text{     (Entwicklung nach der ersten Zeile)}$$
- Für die Determinante einer Matrix $A=(\alpha_{jk})^n_{j,k=1} \in K^{n\times n}$ schreibt man auch 
$$det(A)=\begin{vmatrix}
\alpha_{11} & \alpha_{12} & \cdots & \alpha_{1n} \\
\alpha_{21} & \alpha_{22} & \cdots & \alpha_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\alpha_{n1} & \alpha_{n2} & \cdots & \alpha_{nn} \\
\end{vmatrix}$$

Im Fall $n=2$ gilt tatsächlich:
$$\begin{vmatrix}
a & b\\
c & d
\end{vmatrix}=(-1)^2a det((d))+(-1)^3bdet((c))=ad-bc$$
Schon für $n=3$ wird die Berechnung allerdings ein bisschen mühsamer.

Sehr hilfreich ist dabei dann folgende Beobachtung:
Es sei $A\in K^{n\times n}$ eine sogenannte *untere Dreiecksmatrix*, d.h. 
$$A=\begin{pmatrix}
\alpha_{11} & 0 & \cdots & 0 \\
* & \alpha_{22} & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0 \\
* & \cdots & *\cdots* & \alpha_{nn} \\
\end{pmatrix}$$
wobei anstelle der Sterne "$*$" irgendwelche Elemente aus $K$ stehen. Dann gilt nach der Definition der Determinante

$$det(A)=\alpha_{11}\begin{pmatrix}
\alpha_{22} & 0 & \cdots & 0 \\
* & \alpha_{33} & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0 \\
* & \cdots & *\cdots* & \alpha_{nn} \\
\end{pmatrix}=\alpha_{11}\alpha_{22}\begin{pmatrix}
\alpha_{33} & 0 & \cdots & 0 \\
* & \alpha_{44} & \ddots & \vdots \\
\vdots & \ddots & \ddots & 0 \\
* & \cdots & *\cdots* & \alpha_{nn} \\
\end{pmatrix}$$
$$=\cdots=\alpha_{11}\alpha_{22}\cdot\dotso\cdot\alpha_{nn}$$

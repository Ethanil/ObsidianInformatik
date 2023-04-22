---
aliases: 
---
# Polynominterpolation 
Hierfür verwenden wir als Ansatzfunktion Polynome vom Grad $\leq n$, also
$$\begin{align}
\text{I:}& &p_{n}(x)=\Phi(x;a_{o},\dotso,a_{n})=a_{0}+a_{1}x+\dotso+a_{n}x^{n}
\end{align}$$
Dieses Polynom können wir nun auf verschiedene Arten lösen:
## Naiver Lösungsansatz
Wir lösen die $n+1$ Koeffizienten $a_{0},\dotso,a_{n}$. In Matrixform sieht das Gleichungssystem wie folgt aus
$$\begin{pmatrix}
1&x_{0}&x_{0}^{2}&\cdots &x_{0}^{n} \\
1&x_{0}&x_{1}^{2}&\cdots &x_{1}^{n} \\
\vdots&\vdots&\vdots& &\vdots \\
1&x_{n}&x_{n}^{2}&\cdots &x_{n}^{n} \\
\end{pmatrix}
\begin{pmatrix}
a_{0} \\
a_{1} \\
\vdots \\
a_{n} \\
\end{pmatrix}=
\begin{pmatrix}
y_{0} \\
y_{1} \\
\vdots \\
y_{n} \\
\end{pmatrix}$$
Dieser Ansatz ist aber sehr langsam ($O(n^{3})$) und schlecht [[Kondition|konditioniert]].
## Interpolationsformel von Lagrange
Wir wählen folgendes Vorgehen:
$$\begin{align}
p_{n}(x)=\sum^{n}_{k=0}y_{k}L_{k,n}(x)&&\text{mit}&&L_{k,n}(x)=\prod^{n}_{\substack{j=0\\ j \neq k}}\frac{x-x_{j}}{x_{k}-x_{j}}
\end{align}$$
Die Polynome $L_{k,n}(x)$ sind so gewählt, dass gilt
$$\begin{align}
L_{k,n}(x_{i})\begin{cases}
1& &\text{falls }k=1 \\
0&&\text{sonst.}
\end{cases}&& =:\delta_{ki}
\end{align}$$
$\delta_{ki}$ ist das Kronecker-Symbol.
Es gilt also insgesamt:
$$\begin{align}
p_{n}(x_{i})=\sum^{n}_{k=0}y_{k}L_{k,n}(x_{i})=\sum^{n}_{k=0}y_{k}\delta_{ki}=y_{i}
\end{align}$$
Dies ist auch die einzige Lösung, denn
```ad-abstract
title:Definition - Satz 1.1.1
Es gibt genau ein Polynom $p(x)$ vom Grad $\leq n$, das die Interpolationsbedingungen erfüllt, nämlich $p_{n}(x)$
```
```ad-abstract
title:Beweis
collapse:
Sei $p_{n}(x)$ ein Polynom vom Grad $\leq n$, welches die Interpolationsbedingung erfüllt. Sei nun $\tilde{p}_{n}(x)$ mit Grad $\leq n$ ein weiteres Polynom, das die Interpolationsbedingung erfüllt. $p_{n}(x)-\tilde{p}_{n}(x)$ wäre dann ein Polynom vom Grad $\leq n$ mit $n+1$ verschiedenen Nullstellen. $\tilde{p_{n}}$
```
## Links
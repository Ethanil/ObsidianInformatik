---
aliases: 
---
# Polynominterpolation 
Hierfür verwenden wir als Ansatzfunktion Polynome vom Grad $\leq n$, also
$$\begin{align}
\text{I:}& &p_{n}(x)=\Phi(x;a_{o},\dotso,a_{n})=a_{0}+a_{1}x+\dotso+a_{n}x^{n}
\end{align}$$
```ad-abstract
title:Definition - Interpolationsbedingung
$$p_{n}(x_{i})=y_{i}, i=0,\dotso ,n$$
```
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
Sei $p_{n}(x)$ ein Polynom vom Grad $\leq n$, welches die Interpolationsbedingung erfüllt. Sei nun $\tilde{p}_{n}(x)$ mit Grad $\leq n$ ein weiteres Polynom, das die Interpolationsbedingung erfüllt. $p_{n}(x)-\tilde{p}_{n}(x)$ wäre dann ein Polynom vom Grad $\leq n$ mit $n+1$ verschiedenen Nullstellen. $\tilde{p}_{n}(x)$ muss also identisch 0 sein.
```
## Newtonsche Interpolationsformel
Wir wählen die Newtonsche Darstellung
```ad-abstract
title:Definition - Newtonsche Darstellung
$$p_{n}(x)=\gamma_{0}+\gamma_{1}(x-x_{o})+\gamma_{2}(x-x_{0})(x-x_{1})+\dotso+\gamma_{n}(x-x_{0})(x-x_{1})\dotso(x-x_{n-1})$$
```
mit Parametern $\gamma_{0},\dotso, \gamma_{n}$. Einsetzen in die Interpolationsbedingung ergibt nun
$$\begin{align}
&p_{n}(x_{0})=\gamma_{0}=y_{0}&&\Rightarrow \gamma_{0}=y_{0}\\
&p_{n}(x_{1})=\gamma_{0}+\gamma_{1}(x_{1}-x_{0})=y_{1}&&\Rightarrow \gamma_{1}=\frac{y_{1}-y_{0}}{x_{1}-x_{0}} \\
&p_{n}(x_{2})=\gamma_{0}+\gamma_{1}(x_{1}-x_{0})=y_{1}+\gamma_{2}(x-x_{0})(x-x_{1})&&\Rightarrow \gamma_{2}=\frac{\frac{y_{2}-y_{0}}{x_{2}-x_{0}}-\frac{y_{1}-y_{0}}{x_{1}-x_{0}}}{x_{2}-x_{1}}=\frac{\frac{y_{2}-y_{1}}{x_{2}-x_{1}}-\frac{y_{1}-y_{0}}{x_{1}-x_{0}}}{x_{2}-x_{0}}\\
&&&\vdots
\end{align}$$
Man bezeichnet $f_{[x_{0},\dotso,x_{i}]}:=\gamma_{i}$ als die $i$-te Differenz zu den Stützstellen $x_{0},\dotso,x_{i}$, wobei $f_{[x_{0}]}=\gamma_{0}=y_{0}$.
Die allgemeine Rekursion lautet
$$\begin{align}
j=0,\dotso,n:f_{[x_{j}]}=y_{j}\\
k=1,\dotso,n:j=0,\dotso,n-k:f_{[x_{j},\dotso,x_{j+k}]}=\frac{f_{[k_{j+1},\dotso,x_{j+k}]}-f_{[x_{j},\dotso,x_{j+k-1}]}}{x_{j+k}-x_{j}}
\end{align}$$
```ad-abstract
title:Definition - Newtonsches Interpolationspolynom
$$p_{n}(x)=\gamma_{0}+\sum^{n}_{i=1}\gamma_{i}(x-x_{0})\dotso(x-x_{i-1})=f_{[x_{0},\dotso,x_{i}]}$$
```

## Fehlerabschätzung
Wir wollen abschätzen wie gut unser Interpolationspolynom $p_{n}$ auf $[a,b]$ mit $f$ übereinstimmt.
Sei $f$ $(n+1)$-mal stetig differenzierbar, dann existiert zu jedem $x \in[a,b]$ ein $\xi_{x}\in[a,b]$ mit
$$f(x)-p_{n}(x)=f^{(n+1)}\frac{\xi_{x}}{(n+1)!}(x-x_{0})\dotso(x-x_{n})$$
Wir können also folgende Abschätzung machen:
$$\substack{max\\ x \in[a,b]}|f(x)-p_{n}(x)|\leq\substack{max\\ x \in[a,b]}\frac{|f^{(n+1)}(x)|}{(n+1)!}\substack{max\\ x \in[a,b]}|\prod^{n}_{i=0}(x-x_{i})|\leq \substack{max\\ x \in[a,b]}\frac{|f^{(n+1)}(x)|}{(n+1)!}(b-a)^{n+1}$$
Wir können den Fehler nicht minimieren, indem wir die Anzahl der Stützstellen erhöhen, aber indem wir als Stützstellen Tschebyschevsche-Abszissen wählen:
$$x_{i}=\frac{b-a}{2}\cos(\frac{2i+1}{n+1}\frac{\pi}{2})+ \frac{b+a}{2},i=0,\dotso,n$$
## Links
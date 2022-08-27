## sin und cos
|     | $0°$ | $30°$                | $45°$                | $60°$                | $90°$           | $135°$                | $180°$ | $225°$                | $270°$           | $315°$                |
| --- | ---- | -------------------- | -------------------- | -------------------- | --------------- | --------------------- | ------ | --------------------- | ---------------- | --------------------- |
|     | $0$  | $\frac{\pi}{6}$      | $\frac{\pi}{4}$      | $\frac{\pi}{3}$      | $\frac{\pi}{2}$ | $\frac{3}{4}\pi$      | $\pi$  | $\frac{5}{4}\pi$      | $\frac{3}{2}\pi$ | $\frac{7}{4}\pi$      |
| sin | $0$  | $\frac{1}{2}$        | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$             | $\frac{1}{\sqrt{2}}$  | $0$    | $-\frac{1}{\sqrt{2}}$ | $-1$             | $-\frac{1}{\sqrt{2}}$ |
| cos | $1$  | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$        | $0$             | $-\frac{1}{\sqrt{2}}$ | $-1$   | $-\frac{1}{\sqrt{2}}$ | $0$              | $\frac{1}{\sqrt{2}}$  |

$\sin^{2}+\cos^{2}=1$

## hyperbolische
$$\begin{align}
&\sinh(z):=\frac{e^{z}-e^{-z}}{2},& &z \in \mathbb{C}& &\text{(Sinus hyperbolicus)}\\
&\cosh(z):=\frac{e^{z}+e^{-z}}{2},& &z \in \mathbb{C}& &\text{(Cosinus hyperbolicus)}\\
&\tanh(z):=\frac{\sinh(z)}{\cosh(z)},& &z \in \mathbb{C}\backslash\left\{\left(k \pi \frac{+\pi}{2}\right)i: k \in \mathbb{Z}\right\}& &\text{(Tangens hyperbolicus)} 
\end{align}$$
## bes. Ableitungen

| Name               | Symbol    | Definitionsbereich                           | Bild                             | Ableitung                     |
| ------------------ | --------- | -------------------------------------------- | -------------------------------- | ----------------------------- |
| E-funktion         | $e$       | $\mathbb{R}$                                 | $(0,\infty)$                     | $e$                           |
| (nat.) Logarithmus | $\ln$     | $(0,\infty)$                                 | $\mathbb{R}$                     | $\frac{1}{x}$                 |
| Sinus              | $\sin$    | $\mathbb{R}$                                 | $[-1,1]$                         | $\cos$                        |
| Cosinus            | $\cos$    | $\mathbb{R}$                                 | $[-1,1]$                         | $-\sin$                       |
| Tangens            | $\tan$    | $\mathbb{R}\backslash\{(\frac{k+1}{2})\pi\}$ | $\mathbb{R}$                     | $\frac{1}{cos^{2}}=1+tan^{2}$ |
| Arcussinus         | $\arcsin$ | $[-1,1]$                                     | $[\frac{-\pi}{2},\frac{\pi}{2}]$ | $\frac{1}{\sqrt{1-x^{2}}}$    |
| Arcuscosinus       | $\arccos$ | $[-1,1]$                                     | $[0,\pi]$                        | $\frac{-1}{\sqrt{1-x^{2}}}$   |
| Arcustangens       | $\arctan$ | $\mathbb{R}$                                 | $(\frac{-\pi}{2},\frac{\pi}{2})$ | $\frac{1}{1+x^{2}}$           |
| Sinus hyperbolicus | $\sinh$   | $\mathbb{R}$                                 | $\mathbb{R}$                     | $\cosh$                       |
| Cosinus hyp.       | $\cosh$   | $\mathbb{R}$                                 | $[1,\infty)$                     | $\sinh$                       |
| Tangens hyp.       | $\tanh$   | $\mathbb{R}$                                 | $(-1,1)$                         | $\frac{1}{\cosh^{2}}=1-\tanh^{2}$                              |
## Quotientenregel:
$$(\frac{f}{g})'(x_{0})=\frac{f'(x_{0})g(x_{0})-f(x_{0})g'(x_{0})}{(g(x_{0}))^{2}}$$
## Produktregel
$$(fg)'(x_{0})=f'(x_{0})g(x_{0})+f(x_{0})g'(x_{0})$$
## Kettenregel:
$$(f \circ g)'(x_{0})=f'(g(x_{0}))\cdot g'(x_{0})$$
## part. Integration nach DI-Methode
$$\int^{1}_{0}x^{2}e^{x} dx = |x^{2}e^{x}-2xe^{x}+2e^{x}-\int0 \cdot e^{x} dx|_{0}^{1} = e^{1}(1^{2}-2+2)-e^{0}(0-0+2)=e-2$$


|     | D       | I       |
| --- | ------- | ------- |
| $+$ | $x^{2}$ | $e^{x}$ |
| $-$ | $2x$    | $e^{x}$ |
| $+$ | $2$     | $e^{x}$ |
| $-$ | $0$     | $e^{x}$ |


## Taylorreihe von $f$ um $x_{0}$.
$$\sum^{\infty}_{n=0}\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}$$

## Taylorpolynom
$$t_{k,f}(x;x_{0}):=\sum^{k}_{n=0}\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}$$
## Restglieds des Taylorpolynoms
$$R_{k,f}(x;x_{0}):=\frac{f^{(k+1)}(\xi)}{(k+1)!}(x-x_{0})^{k+1}$$

## Fourrierreihe
$$\begin{align}
\omega \text{ ist die Frequenz, meistens also }2 \pi \\
f \sim \frac{a_{0}}{2}+ \sum^{\infty}_{n=1}(a_{n} \cdot \cos(n \cdot \omega \cdot x) +b_{n} \cdot \sin(n \omega \cdot))\\
a_{0} = \frac{2}{\omega} \int f(x)dx \\
a_{n}=\frac{2}{\omega} \int f(x) \cdot \cos(n \cdot x)\\
b_{n}=\frac{2}{\omega} \int f(x) \cdot \sin(n \cdot x)
\end{align}$$
## i
$$(i+1)=\sqrt{2}e^{i \cdot \frac{\pi}{4}}$$
![[Pasted image 20220824195833.png]]
## Unterminoren
$$\begin{pmatrix}
a & b \\ c & d
\end{pmatrix} \Rightarrow ad -bc = \det$$
$$\begin{pmatrix}
a & b & c \\ d & e & f \\ g & h & i
\end{pmatrix} \Rightarrow aei+bfg+cdh-ceg-bdi-afh = det$$
Wir berechnen von $\begin{pmatrix}a & b & c \\ d & e & f \\ g & h & i\end{pmatrix}$ zuerst $\det(a)$, dann $det(\begin{pmatrix}a & b \\ d & e\end{pmatrix})$ und dann $det(\begin{pmatrix}a & b & c \\ d & e & f \\ g & h & i\end{pmatrix})$ (kann auch für größere Matrizen verwendet werden)
Bei einer Hesse Matrix darf man Spalten und Zeilen vertauschen, aber nur wenn man beides macht (also wenn man 2. und 3. Zeile vertauscht, dann auch 2. und 3. Spalte!)
Nun betrachten wir das vorzeichen von der ersten(von der kleinsten Matrix) bis zur letzten(größte Matrix) Determinante:
Wenn alle positiv sind, ist sie positiv definit, wenn die erste negativ ist und alle alternierend, dann neg. definit, wenn es konkret keins der beiden sein kann, ist sie indefinit, ansonsten kann man mit der Methode nichts über die definitheit aussagen.
positiv def -> Minimum
neg. def. -> Maximum
indefinit -> Sattelpunkt
## geometrische Reihe
$$\sum^{\infty}_{n=0}q^{n}=\frac{1}{1-q}\text{ für } |q|<1$$

## Cauchy-Produkt
$$\sum^\infty_{n=0}\sum^n_{k=0}a_kb_{n-k}=\left(\sum^\infty_{n=0}a_n\right)\left(\sum^\infty_{n=0}b_n\right)$$

## l'Hospital
Bedingungen: $\frac{f(x)}{g(x)}$, offenes Intervall, beide Funktionen müssen differenzierbar sein und $g'(x)$ darf nicht 0 sein und der Grenzwert beider Funktionen muss $0$ oder $\pm\infty$ sein
$$\lim_{x \rightarrow a}\frac{f'(x)}{g'(x)}=L=\lim_{x \rightarrow a}\frac{f(x)}{g(x)}$$
## allgemeine Potenz
$$a^{x}:=e^{x \cdot \ln(a)}$$
$$\left(1+\frac{1}{n}\right)^{n}=e$$
## Konvergenzkriterien
```ad-abstract
title:Definition - Quotientenkriterium
Ist $a_n\neq 0$ für alle $n\in\mathbb{N}$ und existiert der Grenzwert $lim_{n\rightarrow\infty}|a_{n+1}/a_n|$  so ist die Reihe
- [[Absolute Konvergenz|absolut konvergent]], wenn $lim_{n\rightarrow\infty}\frac{|a_{n+1}|}{|a_n|}<1$ ist
- divergent, wenn $lim_{n\rightarrow\infty}\frac{|a_{n+1}|}{|a_n|}>1$ ist
```
```ad-abstract
title:Definition - Wurzelkriterium
Existiert der Grenzwert $lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}$ so ist die Reihe
- [[Absolute Konvergenz|absolut konvergent]], wenn $lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}<1$ ist
- divergent, wenn $lim_{n\rightarrow\infty}\sqrt[n]{|a_n|}>1$ ist.
```
```ad-abstract
title:Definition - Majorantenkriterium
Ist $|a_n|\leq b_n$ für alle $n\geq n_0$ und konvergiert die Reihe $\sum^\infty_{n=0}b_n$, so ist $\sum^\infty_{n=0}a_n$ absolut konvergent
```
```ad-abstract
title:Definition - Minorantenkriterium
Ist $a_n\geq b_n \geq 0$ für alle $n\geq n_0$ und divergiert die Reihe $\sum^\infty_{n=0}b_n$, so divergiert auch die Reihe $\sum^\infty_{n=0}a_n$.
```
```ad-abstract
title:Definition - Leibniz-Kriterium
Es sei $(a_n)$ eine monoton fallende Folge in $\mathbb{R}$ mit $lim_{n\rightarrow\infty}a_n=0$. Dann ist die Reihe $\sum^\infty_{n=0}(-1)^na_n$ konvergent.
```

## Mittelwertsatz der Differenzialrechnung
$$\begin{align}
\frac{f(b)-f(a)}{b-a}=f'(\xi)& &\text{bzw. gleichbedeutend }& &f(b)-f(a)=f'(\xi)(b-a)
\end{align}$$

![[Pasted image 20220827103545.png]]
![[Pasted image 20220827103558.png]]

## Trennung der Variablen
$$\begin{align}
y=&H^{-1}(G(x)) \text{ mit }G(t):=\int^{t}_{t_{0}} g(b) db\text{ und }H(y):=\int^{y}_{y_{0}}\frac{1}{h(c)}dc\\
h(y)&\neq0 \\
y'(t)&=g(t)h(y(t))
\end{align}$$
## Konvergenzradius von Potenzreihe
$$\begin{align}
\varrho&:=\lim_{n \rightarrow \infty}\sqrt[n]{|a_{n}|}\\
r&:=
\begin{cases}
0,\text{ falls }\infty\\
\infty,\text{ falls 0,}\\
\frac{1}{\varrho},\text{ sonst,}
\end{cases}
\end{align}
$$

## Variation der Konstanten
$$\begin{align}
&\begin{cases}
y'(t)+a(t)y(t)=b(t)\\ \\
y(t_{0}) = y_{0}
\end{cases}\\
&A(t)= \int^{t}_{t_{0}}a(s)ds\\
&y(t) = e^{-A(t)}+e^{-A(t)}\int^{t}_{t_{0}}b(s)e^{A(s)}ds
\end{align}$$
## allgemeine binomiale Formel
$$\begin{align}
(a+b)^{n}=\sum^{n}_{k=0}\frac{n!}{k!(n-k)}
a^{n-k}b^{k}\end{align}$$

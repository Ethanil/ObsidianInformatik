---
aliases: 
---
# Trigonometrische Funktionen 
```ad-abstract
title:Definition - Sinus und Cosinus
$$
\begin{align}
&sin(z):=\sum^{\infty}_{n=0}\frac{(-1)^{n}}{(2n+1)!}z^{2n+1},& &z \in \mathbb{C},& &(Sinus)\\
&cos(z):=\sum^{\infty}_{n=0}\frac{(-1)^{n}}{(2n)!}z^{2n},& &z \in \mathbb{C},& &(Cosinus)\\
\end{align}
$$
```
|     | $0°$ | $30°$                | $45°$                | $60°$                | $90°$           | $135°$                | $180°$ | $225°$                | $270°$           | $315°$                      |
| --- | ---- | -------------------- | -------------------- | -------------------- | --------------- | --------------------- | ------ | --------------------- | ---------------- | --------------------- |
|     | $0$  | $\frac{\pi}{6}$      | $\frac{\pi}{4}$      | $\frac{\pi}{3}$      | $\frac{\pi}{2}$ | $\frac{3}{4}\pi$      | $\pi$  | $\frac{5}{4}\pi$      | $\frac{3}{2}\pi$ | $\frac{7}{4}\pi$      |
| sin | $0$  | $\frac{1}{2}$        | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$             | $\frac{1}{\sqrt{2}}$  | $0$    | $-\frac{1}{\sqrt{2}}$ | $-1$             | $-\frac{1}{\sqrt{2}}$ |
| cos | $1$  | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$        | $0$             | $-\frac{1}{\sqrt{2}}$ | $-1$   | $-\frac{1}{\sqrt{2}}$ | $0$              | $\frac{1}{\sqrt{2}}$  |

```ad-abstract
title:Definition - Trigonometrischer Pythagoras
$$\begin{align}
sin^{2}(x)+cos^{2}(x)=1& &\text{für alle }x \in \mathbb{R}
\end{align}$$
```
````ad-abstract
title:Definition - ungerade, gerade, periodisch
Eine Funktion $f: \mathbb{R} \rightarrow \mathbb{R}$ oder $f: \mathbb{C} \rightarrow \mathbb{C}$ heißt
- ungerade, falls $f(-x)=-f(x)$ für alle $x \in \mathbb{R}$, bzw. $\mathbb{C}$ gilt.
- gerade, falls $f(-x)=f(x)$ für alle $x \in \mathbb{R}$, bzw. $\mathbb{C}$ gilt.
- periodisch mit Periode $L \in \mathbb{R}$, bzw. $\mathbb{C}$, wenn $f(x+L)=f(x)$ für alle $x \in \mathbb{R}$, bzw. $\mathbb{C}$ gilt.
```ad-abstract
title:
Der Cosinus ist gerade und der Sinus ist ungerade.
```
````
```ad-abstract
title:Definition - Eulersche Formel
Für alle $z \in \mathbb{C}$ gilt
$$ \begin{align}
e^{iz}= cos(z)+sin(z) i.
\end{align}$$
Insbesondere gilt für alle $x \in \mathbb{R}$ damit
$$\begin{align}
Re(e^{ix})=cos(x)& &\text{und}& &Im(e^{ix})=sin(x)
\end{align}$$
```
````ad-abstract
title:Definition - Formeln für trinonometrische Funktionen
```ad-abstract
title:
$$|sin(x)\leq 1 \text{ und }|cos(x)|\leq 1$$
```
```ad-abstract
title: Additionstheoreme
$$\begin{align}
sin(x+y)&=sin(x)cos(y)+sin(y)cos(x)\\
cos(x+y)&=cos(x)cos(y)-sin(x)sin(y)
\end{align}$$
```
```ad-abstract
title:Rechenregeln für verschobene Funktionen
$$\begin{align}
sin(x+\frac{\pi}{2})&=cos(x),& cos(x+\frac{\pi}{2})&=-sin(x)\\
sin(x+\pi)&=-sin(x),& cos(x+\pi)&=-cos(x)\\
sin(x+2\pi)&=sin(x),& cos(x+2\pi)&=cos(x)\\
\end{align}$$
```
````
```ad-abstract
title:
$$\begin{align}
sin(z)=0&\Leftrightarrow z=k \pi \text{ für ein }k \in \mathbb{Z}\\
cos(z)=0&\Leftrightarrow z=\frac{\pi}{2} +k \pi \text{ für ein }k \in \mathbb{Z}\\
\end{align}$$
```
```ad-abstract
title:Definition - Tangens
Die Funktion $tan: \mathbb{C}\backslash \{\frac{\pi}{2}+k \pi: k \in \mathbb{Z}\}\rightarrow \mathbb{C}$ mit
$$tan(z)=\frac{sin(z)}{cos(z)}$$
heißt Tangens
```

## Links
## sin und cos
|     | $0°$ | $30°$                | $45°$                | $60°$                | $90°$           | $135°$                | $180°$ | $225°$                | $270°$           | $315°$                |
| --- | ---- | -------------------- | -------------------- | -------------------- | --------------- | --------------------- | ------ | --------------------- | ---------------- | --------------------- |
|     | $0$  | $\frac{\pi}{6}$      | $\frac{\pi}{4}$      | $\frac{\pi}{3}$      | $\frac{\pi}{2}$ | $\frac{3}{4}\pi$      | $\pi$  | $\frac{5}{4}\pi$      | $\frac{3}{2}\pi$ | $\frac{7}{4}\pi$      |
| sin | $0$  | $\frac{1}{2}$        | $\frac{1}{\sqrt{2}}$ | $\frac{\sqrt{3}}{2}$ | $1$             | $\frac{1}{\sqrt{2}}$  | $0$    | $-\frac{1}{\sqrt{2}}$ | $-1$             | $-\frac{1}{\sqrt{2}}$ |
| cos | $1$  | $\frac{\sqrt{3}}{2}$ | $\frac{1}{\sqrt{2}}$ | $\frac{1}{2}$        | $0$             | $-\frac{1}{\sqrt{2}}$ | $-1$   | $-\frac{1}{\sqrt{2}}$ | $0$              | $\frac{1}{\sqrt{2}}$  |

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
$$\begin{align}
(\frac{f}{g})'(x_{0})=\frac{f'(x_{0})g(x_{0})-f(x_{0})g'(x_{0})}{(g(x_{0}))^{2}}
\end{align}$$
## Kettenregel:
$$\begin{align}
(f \circ g)'(x_{0})=f'(g(x_{0}))\cdot g'(x_{0})
\end{align}$$

## Taylorreihe von $f$ um $x_{0}$.
$$\begin{align}
\sum^{\infty}_{n=0}\frac{f^{(n)}(x_{0})}{n!}(x-x_{0})^{n}
\end{align}$$

## Fourrierreihe
$$\begin{align}
f ~ a_0
\end{align}$$
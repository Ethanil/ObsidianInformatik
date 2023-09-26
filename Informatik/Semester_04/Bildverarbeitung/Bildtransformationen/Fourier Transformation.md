Die Fourier-Reihe ist die Zerlegung einer diskreten, periodischen Funktion in sinus und cosinus. 

$$\begin{align*}
f(t) &= a_{0}+\sum^{\infty}_{n = 1}(a_{n}\cos(n \omega t) + b_{n}\sin(n \omega t))& &\text{für }0<t<T \\
&= a_{0} + \sum^{\infty}_{n=1}d_{n}\sin(n \omega t + \varTheta_{n})\\
&= a_{0} + \sum^{\infty}_{n=1}c_{n}\cos(n \omega t + \varPhi_{n})\\
&= a_{0} + \sum^{+\infty}_{n=1}c_{n}e^{+jn \omega t}&&c_{n}=\frac{1}{T}\int^{T}_{0}f(t)e^{-in \omega t}\\
&&&e^{-i2 \pi \omega x}= \cos(2 \pi \omega x)- i \cdot \sin(2 \pi \omega x)\\
a_{0}&=\frac{1}{T} \int^{T}_{0}f(t)dt\\
a_{n}&=\frac{2}{T}\int^{T}_{0}f(t)\cos(n \omega t)dt&&\text{für }n \geq 1\\
b_{n}&= \frac{2}{T}\int^{T}_{0}f(t)\sin(n \omega t) dt&&\text{für }n \geq 1 
\end{align*}$$


Im Fourier Bereich werden alle Werte der Funktion $f(t)$ bei der Berechnung von den jeweiligen $a_{n}$ und $b_{n}$ einbezogen.
Im Ortsbereich ergibt sich an jeder Stelle der Funktionswert durch die Überlagerung aller sin und cos Wellen
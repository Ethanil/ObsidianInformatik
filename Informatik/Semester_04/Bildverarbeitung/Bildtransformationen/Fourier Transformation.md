## Fourier Reihe
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
## Fourier Transformation
Bei der Fourier Transformation wird die funktion $f(t)$ zu einer anderen Funktion $F(\omega)$ transformiert:
$$\begin{align*}
F(\omega) = \int^{\infty}_{-\infty}f(t) \cdot e^{-i 2 \pi \omega t} dt\\
f(t) =  \int^{\infty}_{-\infty}F(\omega) \cdot e^{i 2 \pi \omega t} dt\\
e^{-i2 \pi \omega t}= \cos(2 \pi \omega t)- i \cdot \sin(2 \pi \omega t)\\
\end{align*}$$

Daraus folgt dass $F(\omega)$ einen $Re$ und einen $Im$ teil hat. Dies kann man nun auf unterschiedliche Arten darstellen, entweder wir schreiben
$$F(\omega) = Re\{F(\omega)\} + i \cdot Im\{F(\omega\}$$
oder wir verwenden die Länge und den Winkel um den Punkt in der komplexen Ebene darzustellen:
$$\begin{align*}
F(\omega) &= |F(\omega)| \cdot e^{i \Phi(\omega)}|\\
|F(\omega)| &= \sqrt{Re\{F(\omega)\}^{2}+Im\{F(\omega)\}^{2}}&&\text{"Amplituden Spektrum"}\\
\varPhi(\omega) &= \arctan \left( \frac{Im\{F(\omega)\}}{Re\{F(\omega)\}}\right) &&\text{"Phasen Spektrum"}
\end{align*}$$

## Diskrete Fourier Transformation
Da wir mit digitalen Daten arbeiten und diese (idr) diskret sind, müssen wir auch nur eine diskrete Fourier Transformation durchführen
$$\begin{align*}
F[u] &= \frac{1}{\sqrt{N}} \sum^{N-1}_{n=0}f[n]\cdot e^{-i \frac{2\pi un}{N}}&&\Delta u=\frac{1}{N \Delta x}\\
f[n]  &= \frac{1}{\sqrt{N}} \sum^{N-1}_{n=0}F[u]\cdot e^{i \frac{2\pi un}{N}}&&n \in\{0,\dotso, N-1\}\\
\end{align*}$$

Für diese Transformation gilt:
1. Für jedes Bild $f[n]$ existiert eine Fourier-Transformation
2. Jedes Bild lässt sich verlustfrei transformieren (und vice versa)
3. Das Spektrum der Transformation einer diskreten Funktion $f[n]$ der Länge $n=N$ ist diskret mit der gleichen Anzahl von Stellen $N$
4. Obwohl sowohl $f[n]$ als auch Spektrum der Fourier-Transformation diskret sind, die Fourier Transformierte Funktion $F(u)$ ergibt eine 
	- unendlich lange
	- periodische
	- kontinuierliche
	Funktion mit der Periode $\frac{1}{N}$ 

## Fourier-Spektrum
Nach der Diskreten Fourier-Transformation erhalten wir eine Fourier-Spektrum für das folgendes gilt:

| N x M Pixel | N x M Frequenzen              |
| ----------- | ----------------------------- |
| real        | komplex                       |
| Bild        | Spektrum(Amplitude und Phase) |

Jeder Eintrag in dem Spektrum definiert eine Cosinus-Welle. Für diesen Eintrag gilt folgendes:

| Begriff                 | Bedeutung                                    |
| ----------------------- | ----------------------------------- |
| Amplitude               | Höhe einer Welle(="Wichtigkeit")    |
| Phase                   | Verschiebung der Welle zum Ursprung |
| Ausbreitung             | Verbindungsgerade zum Mittelpunkt   |
| Abstand zum Mittelpunkt | Frequenz der Welle                  |

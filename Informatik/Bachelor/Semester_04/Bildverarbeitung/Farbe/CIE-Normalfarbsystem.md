Da wir nicht alle Farben durch "reine" Addition mit unseren $RGB$-Farben darstellen können (Siehe [[Grassmansche Gesetze]]), wir aber gleichzeitig nicht mit negativen Farben arbeiten wollen, definieren wir virtuelle Primärvalenzen $XYZ$, mit denen wir mithilfe von ausnahmslos positive Koeffizienten jede reale Farbe darstellen können.
Die Primärvalenz $Y$ entspricht dabei der Helligkeitsempfindung.
Daraus ergeben sich die CIE-Farbmischkoeffizienten $\bar{x},\bar{y},\bar{z}$ 

```ad-attention
Es gibt zwei Normalfarbsysteme, einmal das für den Normbeobachter bei 2° und einmal bei 10°!
```

## Normfarbwertanteile xyz
Wir definieren weiterhin
$$\begin{align*}
x = \frac{X}{X+Y+Z}&&y=\frac{Y}{X+Y+Z}&&z=\frac{Z}{X+Y+Z}
\end{align*}$$
und geben eine Farbe dann mithilfe von 
$$Yxy$$
an, also $Y$ der Helligkeit und $x,y$ wie oben definiert.

Daraus können wir die anderen Werte wie folgt rückrechnen:
$$\begin{align*}
X=\frac{x}{y}Y&&Y=Y&&Z=\frac{1-x-y}{y}Y
\end{align*}$$
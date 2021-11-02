# Beweisprinzipien
## Direkter Beweis
Bei einem direkten Beweis beweisen wir eine Behauptung "normal":
### Beispiel
Vorraussetzung: $n,m \in\mathbb{N}$ gerade
Behauptung: $n+m$ ist auch gerade
Beweis: Wenn $n$ und $m$ gerade ist $\Rightarrow$ $\exists\  l\in\mathbb{N}:2*l=n$ und $\exists\  k\in\mathbb{N}:2*k=m$
$\Rightarrow 2*l+2*k=n+m$
$\Leftrightarrow 2*(l+k)=n+m$
$\Rightarrow \exists\ x\in\mathbb{N}:x=l+k$
$\Rightarrow 2*x=n+m\Rightarrow n+m$ ist gerade $\blacksquare$
## Beweis durch Kontraposition
Bei einem Beweis durch Kontraposition beweisen wir, dass wenn wir die Behauptung negieren die angenommene Aussage falsch ist, dadurch beweisen wir, dass wenn die Aussage wahr ist, die Behauptung wahr sein muss, da
$A\Rightarrow B\Leftrightarrow \neg B\Rightarrow\neg A$:
### Beispiel
Voraussetzung: Sei $n\in\mathbb{N}$ mit $n^2$ gerade
Behauptung: $n$ ist auch gerade
Beweis: Es gelte $n$ ist ungerade, also $\exists\ l\in\mathbb{N}:n=2*l+1$
$n^2 = n = (2l+1)^2$
$\Leftrightarrow n^2=4l^2+4l+1$
$\Leftrightarrow n^2=2*(2l^2+2l)+1$
$\exists\ k\in\mathbb{N}:2l^2+2l=k$
$n^2=2*k+1$ ist ungerade, da dies die negierte Voraussetzung ist, ist die Behauptung wahr $\blacksquare$ 
## Beweis durch Widerspruch
Bei einem Beweis durch Widerspruch nehmen wir an, dass die Behauptung falsch sei und erhalten so einen Widerspruch, dadurch muss die Behauptung wahr sein:
### Beispiel
Behauptung: $\sqrt{2}\notin\mathbb{Q}$
Beweis: Annahme: $\sqrt{2}\in\mathbb{Q}$
$\exists n,m\in\mathbb{Z}:\frac{n}{m}=\sqrt{2}$, wobei $n,m$ maximal gekürzt sind.
$\frac{n}{m}=\sqrt{2}$
$\Leftrightarrow (\frac{n}{m})^2=(\sqrt{2})^2$
$\Leftrightarrow \frac{n^2}{m^2}=2$
$\Leftrightarrow n^2=2m^2$
$\Rightarrow n^2$ ist also gerade, also gilt $n$ ist gerade, nach [[Beweisprinzipien#Beweis durch Kontraposition#Beispiel|1]]
## Beweis durch Induktion

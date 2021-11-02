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
$\Rightarrow \exists k\in\mathbb{N}:n=2k$
$\Rightarrow (2k)^2=2m^2$
$\Leftrightarrow 4k^2=2m^2$
$\Leftrightarrow 2k^2=m^2$
$\Rightarrow m^2$ ist also gerade, beide Zahlen waren also nicht maixmal gekürzt(außerdem können wir ewig so weiter machen), dies ist ein Widerspruch
$\Rightarrow \sqrt{2}\notin\mathbb{Q}$
$\blacksquare$
## Beweis durch Induktion
Bei einem Beweis durch Induktion, beweisen wir zuerst dass die Behauptung für ein Element gilt und danach dass es für alle folgenden auch gilt.
Dies ist v.a. praktisch bei Beweisen in $\mathbb{N}$, da wir dort erst für $0$ und dann für $n+1$ beweisen können.
### Beispiel
Behauptung: $\forall n\in\mathbb{N^*}:1+2+...+n=\frac{n(n+1)}{2}$
Beweis: Induktionsanfang: $1=\frac{1*(1+1)}{2}=\frac{2}{2}\checkmark$
Induktionsvoraussetzung: Für ein $n\in\mathbb{N^*}$ gilt 
$$1+2+...+n=\frac{n(n+1)}{2}$$
Induktionsschritt: ($n\leadsto n+1$)
Es ist $1+2+...+n+(n+1)\stackrel{I.V.}{=}\frac{n(n+1)}{2}+n+1$
$\Leftrightarrow \frac{n(n+1)+2(n+1)}{2}=\frac{((n+1)+1)(n+1)}{2}$
$=\frac{(n+1)((n+1)+1)}{2}$
$\blacksquare$
# Beweisprinzipien
## Direkter Beweis
Bei einem direkten Beweis beweisen wir eine Behauptung "normal":

---
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

---
Voraussetzung: Sei $n\in\mathbb{N}$ mit $n^2$ gerade
Behauptung: $n$ ist auch gerade
Beweis: Es gelte $n$ ist ungerade, also $\exists\ l\in\mathbb{N}:n=2*l+1$
$n^2 = n = (2*l+1)^2$
$\Leftrightarrow n^2=2*2*l^2+1$
$\Leftrightarrow n^2=2*(2*l^2)+1$
$\exists\ k\in\mathbb{N}:2*l^2=k$
$n^2=2*k+1$ ist ungerade
## Beweis durch Widerspruch
Bei einem Beweis durch Widerspruch nehmen wir an, dass die Behauptung falsch sei und erhalten so einen Widerspruch, dadurch muss die Behauptung wahr sein:

---
## Beweis durch Induktion
# Beweis durch Kontraposition
Bei einem Beweis durch Kontraposition beweisen wir, dass wenn wir die Behauptung negieren die angenommene Aussage falsch ist, dadurch beweisen wir, dass wenn die Aussage wahr ist, die Behauptung wahr sein muss, da
$A\Rightarrow B\Leftrightarrow \neg B\Rightarrow\neg A$:
## Beispiel
Voraussetzung: Sei $n\in\mathbb{N}$ mit $n^2$ gerade
Behauptung: $n$ ist auch gerade
Beweis: Es gelte $n$ ist ungerade, also $\exists\ l\in\mathbb{N}:n=2*l+1$
$n^2 = n = (2l+1)^2$
$\Leftrightarrow n^2=4l^2+4l+1$
$\Leftrightarrow n^2=2*(2l^2+2l)+1$
$\exists\ k\in\mathbb{N}:2l^2+2l=k$
$n^2=2*k+1$ ist ungerade, da dies die negierte Voraussetzung ist, ist die Behauptung wahr $\blacksquare$ 
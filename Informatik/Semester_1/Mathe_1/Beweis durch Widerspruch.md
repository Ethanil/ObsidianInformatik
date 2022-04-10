# Beweis durch Widerspruch
Bei einem Beweis durch Widerspruch nehmen wir an, dass die Behauptung falsch sei und erhalten so einen Widerspruch, dadurch muss die Behauptung wahr sein:
## Beispiel
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
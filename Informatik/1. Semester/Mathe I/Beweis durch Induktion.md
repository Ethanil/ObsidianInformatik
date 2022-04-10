# Beweis durch Induktion
Bei einem Beweis durch Induktion, beweisen wir zuerst dass die Behauptung für ein Element gilt und danach dass es für alle folgenden auch gilt.
Dies ist v.a. praktisch bei Beweisen in $\mathbb{N}$, da wir dort erst für $0$ und dann für $n+1$ beweisen können.
## Beispiel
Behauptung: $\forall\ n\in\mathbb{N^*}:1+2+...+n=\frac{n(n+1)}{2}$
Beweis: Induktionsanfang: $1=\frac{1*(1+1)}{2}=\frac{2}{2}\checkmark$
Induktionsvoraussetzung: Für ein $n\in\mathbb{N^*}$ gilt 
$$1+2+...+n=\frac{n(n+1)}{2}$$
Induktionsschritt: ($n\leadsto n+1$)
Es ist $1+2+...+n+(n+1)\stackrel{I.V.}{=}\frac{n(n+1)}{2}+n+1$
$\Leftrightarrow \frac{n(n+1)+2(n+1)}{2}=\frac{((n+1)+1)(n+1)}{2}$
$=\frac{(n+1)((n+1)+1)}{2}$
$\blacksquare$
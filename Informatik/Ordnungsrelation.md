# Ordnungsrelationen
Eine Relation ist eine Ordnungsrelation, wenn sie [[Relationen#Reflexiv|reflexiv]], [[Relationen#Antisymmetrisch|antisymmetrisch]] und [[Relationen#Transitiv|transitiv]] ist.
Wenn eine Relation eine Ordnungsrelation ist benutzt man
$$x\le y\text{ statt }xRy$$
Gibt es auf $X$ eine Ordnungsrelation, so heißt $X$ *partiell gerodnet*

```ad-example
title:Beispiele
collapse:true
a) $\le$ in $\mathbb{N,Z,Q,R}$
b) lexikographische Ordnung
c) Sei $M$ Menge dann $\subseteq$ Ordnungsrelation auf $P(M)$
denn:
- reflexiv: $\forall N\in P(M):N\subseteq N$
- antisym: Seien $N_1,N_2\in P(M)$ mit $N_1\subseteq N_2$ und $N_2\subseteq N_1$ Dann gilt $N_1=N_2$
- transitiv: Seien $N_1,N_2,N_3\in P(M)$ mit $N_1\subseteq N_2$ und $N_2\subseteq N_3$, dann gilt $N_1\subseteq N_3$
```
## Bemerkung:
a) Es kann unvergleichbare Elemente geben
-> d.g. $x,y\in X$mit weder $x\le y$ noch $y\le x$
z.B.: $M=\{0,1,2\}$ dann $\{0,1\}\nsubseteq\{0,2\}$ und $\{0,2\}\nsubseteq\{0,1\}$

---
Das ist auch der Unterschied zwischen **Teil**ordnung und **Total**ordnung:
Ist $\le$ Ordnungsrelation auf $X$ mit $$\forall x,y\in X:x\le y \vee y\le x$$
So heißt diese Totalordnung und $X$ total geordnet.

b) $(X,\le)$ partiell(total) geordnet, $Y\subseteq X$.
Dann ist $(Y,\subseteq)$ partiell(total) georndet.
```ad-example
title:Beispiel
collapse:true
Wenn wir ein Wörterbuch $X$ haben, welches total geordnet ist und wir daraus ein Teilwörterbuch $Y$ kopieren(bspw nur alle Wörter die mit "A" beginnen), dann ist dieses Teilwörterbuch genauso total geordnet wie $X$ auch.
```

c) Sei $(X\le)$ partiell geordnet. 
Schreibweise:
$$x\ge y\text{, falls }y\le x$$
$$x\textless y\text{, falls }x\le y\text{ und }x\neq y$$
$$x\textgreater y\text{, falls }y\textless x$$

## größtes/kleinstes Element
Sei $(X\le)$ partiell geordnet $Y\subseteq X$
- $g\in X$ heißt größtes Element von $X$, falls $\forall x\in X:x\le g$
- $k\in X$ heißt kleinstes Element von $X$, falls $\forall x\in X: k\le x$
- $s\in X$ heißt obere Schranke von $Y$, falls $\forall y\in Y:y\le s$
- $t \in X$ heißt untere Schranke von $Y$, falls $\forall y\in Y:y\ge t$
```ad-example
title:Beispiel
collapse:true
bei einer Menge $X:= \mathbb{N}$ ist $Y$ bspw. $\{1,2,3\}$
$g$ hat damit kein größtes Element
$k$ ist 0 (oder 1, je nachdem wie $\mathbb{N}$ definiert wird)
$s$ ist $\forall x\in X:x\ge 3$
$t$ ist 0
```
## Es gibt nur maximal ein größtes/kleinstes Element
Sei $(X,\le)$ partiell geordnet, dann hat $X$ höchstens ein größtes/kleinstes Element. Niemals mehr als 1.
Sei $g_1, g_2\in X$ größte Elemente von $X$
- $g_1$ ist ein größtes Element von $X$, also ist $\forall x\in X:x\le g_1$
- $g_2$ ist ein größtes Element von $X$, also ist  $\forall x\in X:x\le g_2$
- Antisymetrie: $g_1\le g_2\wedge g_2\le g_1\Rightarrow g_1=g_2$
Bei dem kleinsten Element ist dies Analog
## [[Supremum]] und [[Infimum]]
Sei $(X,\le)$ partiell gerodnet, $Y\subseteq X$
- Hat $S:=\{s\in X:s\text{ obere Schranken von Y}\}$
	- kleinstes Element $s_0$, so heißt dieses [[Supremum]] von $Y$
- Hat $T:=\{t\in X:t\text{ untere Schranken von Y}\}$
	- größtes Element $t_0$, so heißt dieses [[Infimum]] von $Y$
- Gilt $s_0=sup\text{ }Y\in Y$, so heißt $s_0$ Maximum von $Y$
	$$s_0=max\text{ }Y$$
- Gilt $t_0=inf\text{ }Y\in Y$, so heißt $t_0$ Minimum von $Y$
	$$s_0=min\text{ }Y$$
```ad-example
title:Beispiel:
collapse:true
$X=\mathbb{R}, Y=(-2,5]$
$S=\{x\in\mathbb{R}:x\le y\text{ für alle }y\in Y\}$
$=[5,\infty]$
$sup\text{ }Y=5=max\text{ }Y$
$T=\{x\in\mathbb{R}:x\le y\text{ für alle }y\in Y\}$
$=[-\infty,-2]$
$inf\text{ }Y=-2=min\text{ }Y$
Bei der Menge Y, die aus den Zahlen exklusiv -2 bis inklusiv 5 ([[Intervall]]) besteht, die Teil von der Reellen Zahlen ist, ist die untere Schranke 5 bis unendlich und das maximum 5(die kleinste obere Schranke). die unteren Schranken sind -Unendlich bis -2, wobei es kein minimum gibt, da $-2\notin Y$
```
```ad-example
title:Beispiel:
collapse:true
- $X=\mathbb{Q}, Y=\mathbb[Q_+]:=\{q\in\mathbb{Q}:q\textgreater 0\}$ mit üblichem $\le$
	- hat kein größtes Element(da es unendlich viele Zahlen gibt)
	- hat kein kleinstes Element(da wir die Zahlen größer 0 genommen haben, können wir uns unendlich klein an 0 annähern)
	- hat keine oberen Schranken
	- hat untere Schranken, da es in $\mathbb{Q}$ Zahlen $\le 0$ gibt.
		- $inf(\mathbb{Q_+})=0$
			- kein Minimum, da $0\notin\mathbb{Q_+}$
```
```ad-example
title:Beispiel:
collapse:true
- $X=\mathbb{Q}, Y:=\{x\in\mathbb{Q}:x^2\textless 2\}$
	- $Y$ beinhalten also alle Zahlen zwischen $-\sqrt{2}$ und $\sqrt{2}$
	- $Y$ hat viele obere Schranken
	- $Y$ hat aber *KEIN* Supremum, da es keine kleinste obere Schranke gibt, da  $\sqrt{2}$ irrational ist und dadurch ist $\sqrt{2}\notin\mathbb{Q}$.
	- $Y$ hat auch viele untere Schranken
	- $Y$ hat auch kein Infimum aus dem selben Grund
```
```ad-example
title:Beispiel:
collapse:true
- In $x\in\mathbb{N}$ mit üblichem $\le$ 
	- hat jede Teilmenge $\neq\emptyset$ ein Minimum
	- hat jede endliche Teilmenge $\neq\emptyset$ ein Maximum
```
```ad-example
title:Beispiel:
collapse:true
- Sei $X=(P(\{0,1,2\}),\subseteq),Y=\{\emptyset,\{0\}\}$
	- obere Schranken: $\{0\},\{0,1\},\{0,2\},\{0,1,2\}$
	- $sup(Y)=max(Y)=\{0\}$
	- nur $\emptyset$ ist die untere Schranke
	- $inf(Y)=min(Y)=\emptyset$
```

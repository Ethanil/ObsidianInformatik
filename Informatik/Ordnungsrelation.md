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
$g$ ist damit $\infty$
$k$ ist 0 (oder 1, je nachdem wie $\mathbb{N}$ definiert wird)
$s$ ist $\forall x\in X:x\ge 3$
$t$ ist 0
```
# [[Mathe I]] Hausübung 01
![[Uebung01-Aufgaben.pdf]]
## Gruppenübung
1. Überzeugen Sie sich mit Hilfe von Wahrheitstafeln von den folgenden Zusammenhängen:
	- Es gilt $\neg(A\wedge B)\Leftrightarrow(\neg A)\vee(\neg B)$ und $\neg(A\vee B)\Leftrightarrow(\neg A)\wedge(\neg B)$


	| $A$   | $B$   | $\neg A$ | $\neg B$ | $A\wedge B$ | $\neg (A\wedge B)$ | $(\neg A)\vee(\neg B)$ |
	| --- | --- | -------- | -------- | ----------- | ------------------ | ------------------ |
	| w   | w   | f        | f        | w           | f                  |             f       |
	| w   | f   | f        | w        | f           | w                  |              w      |
	| f   | w   | w        | f        | f           | w                  |                 w   |
	| f   | f   | w        | w        | f           | w                  |                    w|

	| $A$   | $B$   | $\neg A$ | $\neg B$ | $A\vee B$ | $\neg (A\vee B)$ | $(\neg A)\wedge(\neg B)$ |
	| --- | --- | -------- | -------- | --------- | ---------------- | ------------------------ |
	| w   | w   | f        | f        | w         | f                |            f              |
	| w   | f   | f        | w        | w        | f                |              f            |
	| f   | w   | w        | f        | w         | f                |          f               |
	| f   | f   | w        | w        | f         | w                |           w               |
	- Die Implikation $A\Rightarrow B$ ist äquivalent zu Implikation $\neg B\Rightarrow\neg A$

	| $A$ | $B$ | $\neg A$ | $\neg B$ | $\neg (A\vee B)$ | $\neg B\Rightarrow\neg A$ |
	| --- | --- | -------- | -------- | ---------------- | ----------------------- |
	| w   | w   | f        | f        | w                | w                      |
	| w   | f   | f        | w        | f                | f                       |
	| f   | w   | w        | f        | w                | w                       |
	| f   | f   | w        | w        | w                | w                       |
	- Aus der Implikation $A\Rightarrow B$ folgt im Allgemeinen *nicht* die Implikation $B\Rightarrow A$


	| $A$ | $B$ | $\neg (A\vee B)$ | $B\Rightarrow A$ |
	| --- | --- | ---------------- | ---------------- |
	| w   | w   | w                | w                |
	| w   | f   | f                | w                |
	| f   | w   | w                | f                |
	| f   | f   | w                | w                |
2. Es sei $W$ die Menge aller Wände in einem Haus. Wir betrachten die Aussageformen
$$F(x): x\text{ hat ein Fenster,}$$
$$T(x):x\text{ hat eine Tür}$$
Was drücken die folgenden Aussagen in natürlicher Sprache aus? Negieren Sie die Aussagen und drücken Sie die negierten Aussagen ebenfalls in natürlicher Sprache aus.
- 
	- $\forall x\in W:F(x)$
	- $\forall x\in W:(T(x)\Rightarrow(\neg F(x)))$
	- $(\forall x\in W:F(x))\Rightarrow(\exists x\in W:F(c))$
	
	
## H1.1
1.  
	- Es gibt eine kleinste natürliche Zahl 
		- Ist eine wahre Aussage (0 bzw 1 Siehe [[Natürlichen Zahlen]])
	- $\exists x\in\mathbb{Q}:x^2=2$
		- Ist eine falsche Aussage ($\sqrt{2}$ ist teil der [[Irrationalen Zahlen]], nicht der [[Rationalen Zahlen]])
	- Die Zahl 99 ist kleiner.
		- Ist Keine Aussage.
	- Zu Hilfe, zu Hilfe!
		- Ist Keine Aussage
	- $\forall x\in\mathbb{N}:x\textgreater 1$
		- Ist eine falsche Aussage (0, 1 sind Teil der [[Natürlichen Zahlen]])
	- $\exists y\in\mathbb{N}:x+y\le 3$
		- Ist eine wahre Aussage (bspw x=1, y=2)
2. Sei $A=\{\{1\},2\}$ und $P(A)$ ihre Potenzmenge. Welche der folgenden Aussagen sind wahr?
	- $P(A)=\{\emptyset,\{\{1\}\},\{2\},\{\{1\},2\}\}$, siehe [[Potenzmenge]]
		- $\{\{1\}\}\in P(A)$ : $\{\{1\}\}$ ist Teil von der Potenzmenge von A
		- $\{\{2\}\}\subseteq P(A)$, da $\{\{2\}\}$ eine [[Teilmengenbeziehungen|Teilmenge]] von $P(A)$ ist (Jedes (also das eine) Element kommt in $P(A)$ vor)).
		- $\{\{1\},2\}\in P(A)$, siehe oben
		- $A\cup\{2\}=A$, da die [[Vereinigung]] von $A$ und $\{2\}$ $A$ ist, da $\{2\}$ schon in $A$ vorkommt
		- $A\cap\{\{2\}\}=\emptyset$, da es keine [[Schnittmenge]] von $A$ und $\{\{2\}\}$ gibt.
		- $A\backslash\{\{1\}\}=\{2\}$, da die [[Mengendifferenz]] von $A$ und $\{\{1\}\}$ nur noch aus $\{2\}$ besteht.
	3. Wir betrachten im Folgenden Teilmengen der partiell geordneten Mengen $(\mathbb{R},\le)$ und $(P(\{0,1,2\}),\subseteq)$
	- $A=\{x\in\mathbb{R}:x\textless 0\}$
		- $A$ hat *kein* Supremum, da es keine [[Ordnungsrelation#größtes kleinstes Element|Obere Schranke]] hat
		- $A$ hat *kein* Maximum, da es kein Supremum hat
		- $A$ hat ein Infimum (0)
	- $B=\{ \frac{1}{n} :n\in\mathbb{N}\}$
		- $B$ hat ein Maximum (1)
		- $B$ hat *kein* Minimum (keine untere Schranke)
		- $B$ 100 ist ene obere Schranke ($100\textgreater1$)
	- $C=\{1,3,5,7,10\}$
		- $max(C)=10$ ist wahr, da 10 das Maximum von C ist
		- $C$ ist beschränkt (es gibt sowohl untere (0), als auch obere (100) Schranken)
		- $inf(C)=0$ ist falsch, da die größte untere Schranke 1 ist und somit $inf(C)=1$.
	- $D=\{\{2\},\{1,2\}\}$
		- $inf(D)=\{1\}$ ist falsch, da
		- $inf(D)=\{2\}$ das [[Infimum]] ist.
		- $D$ hat ein Maximum ($\{1,2\}$)
	- $E=\{\emptyset,\{0,1\},\{1,2\}\}$
		- $sup(E)=\{1,2\}$ ist wahr, da es die kleinste, obere Schranke ist.
		- $sup(E)=\{0,1,2\}$ ist falsch, da eine Menge aus 3 Elementen kein Supremum für eine Menge, bei der es kein Element mit 3 Elementen gibt sein kann.
		- $E$ hat ein Maximum, es ist $sup(E)=\{1,2\}$ 
	- $F=\{\{0\},\{1\},\{2\}\}$
		- $inf(F)=\emptyset$ ist falsch
		- $inf(F)=\{\emptyset\}$ ist falsch
		- $F$ hat ein Maximum, es ist $\{2\}$

## H1.2
1. Bestimmen Sie, ob die folgenden Relationen [[Reflexiv]], [[Symmetrisch]], [[antisymmetrisch]] bzw. [[transitiv]] sind. Welche der Relationen sind [[Äquivalenzrelation]]? Welche sind [[Ordnungsrelation]]
	- $R_1=\{(x,y)\in\mathbb{N}\times\mathbb{N}|x+y\text{ ist gerade}\}$
		- In dieser Relation sind nur Tupel enthalten, bei denen x und y entweder BEIDE gerade oder BEIDE ungerade sind.
		- Reflexiv: Die Relation ist reflexiv, da damit ein Tupel Teil der Relation ist, müssen beide Elemente des Tupels entweder gerade oder beide ungerade sein. Damit sind alle (x,x) in der Relation enthalten.
		- Symmetrisch: Die Relation ist symmetrisch, da wenn (x,y) enthalten ist x&y beide gerade bzw ungerade sind, dadurch gilt, dass (y,x) auch enthalten sein muss, da die Bedingung dort auch für beide Elemente gilt.
		- Antisymmetrisch: Wenn eine Relation symmetrisch ist, kann sie nicht antisymmetrisch sein.
		- Transitiv: Wenn (x,y) und (y,z) enthalten ist, dann ist auch (x,z) enthalten, da wenn x gerade ist, y gerade sein muss, dadurch muss auch z gerade sein. Wenn x und z gerade ist, dann ist (x,z) auch enthalten. Für ungerade gilt das selbe
		- Damit ist diese Relation eine Äquivalenzrelation: Sie teilt die Menge in 2 disjunkte Teilmengen auf (alle geraden Zahlen und alle ungeraden) (Sie ist Reflexiv, Symmetrisch und Transitiv)
		- Sie ist keine Ordnungsrelation, da Äquivalenzrelationen keine Ordnungsrelationen sein können.
	- $R_2=\{(x,y)\in\mathbb{N}\times\mathbb{N}|x+2\le y\}$
		- Dies ist eine modifizierte $textless$-Relation, bei der die erste Zahl des Tupels mindestens 2 kleiner sein muss, als die zweite, deshalb gelten alle Relationen wie für die $\textless$-Relation
		- Reflexiv: Diese Relation ist nicht reflexiv, da (x,x) nicht immer gilt; bspw $x=1: 1+2\le 1$ ist NICHT wahr
		- Symmetrisch: Diese Relation ist nicht symmetrisch, da wenn (x,y) enthalten ist (y,x) niemals enthalten ist: $(1,3): 1+2\le 3$ ist enthalten, aber $(3,1): 3+2\le 1$ ist NICHT enthalten
		- Antisymmetrisch: Diese Relation ist antisymmetrisch, da wie bei symmetrisch beschrieben, wenn (x,y) enthalten ist, ist (y,x niemals enthalten): Das zweite Element des Tupels muss immer mindestens 2 größer sein, als das erste, wenn dies gilt, kann das 1. nicht auch 2 größer sein als das 2., da $\textless$ und $\textgreater$ beides Antisymmetrische Relationen sind, muss diese auch Antisymmetrisch sein.
			- Anders gesagt: es gibt keine (y,x), wenn es (x,y) gibt, also ist die Aussage falsch, dadurch ist die Implikation x=y wahr.
		- Transitiv: Die Relation ist Transitiv, da wenn $x+2\le y$ und $y+2\le z$ dann gilt auch $x+2\le z$, da wenn y mindestens 2 größer ist als x und z mindestens 2 größer ist als y, dann ist z mindestens 4 größer als x und damit gilt die Relation.
		- Keine Äquivalenzrelation, da nicht Reflexiv und Symmetrisch
		- Keine Ordnungsrelation, da nicht nicht Reflexiv
	- $R_3=\{(A,B)\in P(\mathbb{N})\times P(\mathbb{N})|A\subseteq B\}$
		- [[Mathe I Hausübung 01 H1.2 (a)(iii)]]
2. 	
[[Mathe I Hausübung 01 H1.2 (b)]]
## H1.3
1. Formulieren Sie die folgenden Aussagen mit Hilfe von Quantoren. Geben Sie außerdem die NEgation der Aussagen an, und zwar sowohl mit Quantoren als auch in natürlicher Sprache (d.h. im Stil der Aufgabenstellung).
	- Die Menge der ganzen Zahlen besitzt ein größtes Element.
		- $\forall m\in\mathbb{Z}:\exists n\in\mathbb{Z}:n\ge m$
		- $\neg(\forall m\in\mathbb{Z}:\exists n\in\mathbb{Z}:n\ge m)$
		- $\exists m\in\mathbb{Z}:\neg(\exists n\in\mathbb{Z}:n\ge m)$
		- $\exists m\in\mathbb{Z}:\forall n\in\mathbb{Z}:\neg(n\ge m)$
		- $\exists m\in\mathbb{Z}\ \forall n\in\mathbb{Z}:n\textless m$
		- Es gibt ein $m$, so dass alle $n$ kleiner sind als $m$.
	- Jede natürliche Zahl ist gleich Null oder von der Form $n+1$ mit $n\in \mathbb{N}$
		- $\forall m\in\mathbb{N}\exists n\in\mathbb{N}:m=0\vee m=n+1$
		- $\neg(\forall n,m\in\mathbb{N}:m=0\vee m=n+1)$
		- $\exists m\in\mathbb{N}:\neg(m=0)\wedge \neg(m=n+1)$
		- Es gibt eine natürliche Zahl $m$, die nicht gleich Null und nicht von der Form $n+1$ ist.
	2. Der [[NOR]]-Operator $\downarrow$ ist durch die nachstehende Wahrheitstafel erklärt. Zeigen Sie, dass sich die folgenden logischen Verknüpfungen $\neg A,A\vee B$ und $A\Rightarrow B$ einzig mit Hilfe des NOR-Operators ausdrücken lassen! Verwenden Sie dazu Wahrheitstafeln	

| $A$ | $A$ | $\neg A$ | $A\downarrow A$ |
| --- | --- | -------- | --------------- |
| w   | w   | f        | f               |
| f   | f   | w        | w               |



| $A$ | $B$ | $A\vee B$ | $A\downarrow B$ | $(A\downarrow B)\downarrow(A\downarrow B)$ |
| --- | --- | --------- | --------------- | ------------------------------------------ |
| w   | w   | w         | f               | w                                          |
| w   | f   | w         | f               | w                                          |
| f   | w   | w         | f               | w                                          |
| f   | f   | f         | w               | f                                          |


| $A$ | $B$ | $A\Rightarrow B$ | $\neg A$ | $(A\downarrow A)\downarrow B$ | $((A\downarrow A)\downarrow B)\downarrow((A\downarrow A)\downarrow B)$ |
| --- | --- | ---------------- | -------- | ----------------------------- | ---------------------------------------------------------------------- |
| w   | w   | w                | f        | f                             | w                                                                      |
| w   | f   | f                | f        | w                             | f                                                                      |
| f   | w   | w                | w        | f                             | w                                                                      |
| f   | f   | w                | w        | f                             | w                                                                      |

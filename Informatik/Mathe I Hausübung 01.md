# [[Mathe I]] Hausübung 01
![[Uebung01-Aufgaben.pdf]]
## Gruppenübung
1. Überzeugen Sie sich mit Hilfe von Wahrheitstafeln von den folgenden Zusammenhängen:
	- Es gilt $\neg(A\wedge B)\Leftrightarrow(\neg A)\vee(\neg B)$ und $\neg(A\vee B)
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
		- $cup\{2\}=A$, da die [[Vereinigung]] von $A$ und $\{2\}$ $A$ ist, da $\{2\}$ schon in $A$ vorkommt
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
	- $R_2=\{(x,y)\in\mathbb{N}\times\mathbb{N}|x+2\le y\}$
	- $R_3=\{(A,B)\in P(\mathbb{N})\times P(\mathbb{N})|A\subseteq B\}$
2. 
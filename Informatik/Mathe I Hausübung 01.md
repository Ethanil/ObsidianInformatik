# [[Mathe I]] Hausübung 01
![[Uebung01-Aufgaben.pdf]]
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
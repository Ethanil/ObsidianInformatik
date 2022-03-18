---
aliases: 
---
# Uebung 01
## G1.1
Sei $M=\{1,2,3\}$. Welche der Folgenden Aussagen sind wahr?
- $\emptyset\in M$ 
- $\emptyset \subseteq M$
- $\{\emptyset\}\in M$
- $\emptyset\in P(M)$
```ad-check
collapse:true
title:Lösung
$\emptyset\subseteq M$ und $\emptyset\in P(M)$ sind wahr
```

Sei $\Sigma$ ein Alphabet. Welche der folgenden Aussagen sind wahr?
- $\Sigma^*=\{\Sigma^+,\epsilon\}$
- $\epsilon=\Sigma^*\backslash\Sigma^+$
- $\Sigma^*=\bigcup^\infty_{n=1}\Sigma^n$
- $\Sigma^*=\{v\cdot w:v,w\in\Sigma^*\}$

```ad-check
collapse:true
title:Lösung
$\Sigma^*=\{v\cdot w:v,w\in\Sigma^*\}$ ist wahr.
```
Sei $M$ eine Menge und $A,B\subseteq M$. Welche der folgenden Aussagen sind wahr?
- $M\backslash A\subseteq M$
- $A\times B\subseteq M\times M$
- $A\times B=B\times A$
- $A\times \emptyset=\emptyset$
```ad-check
collapse:true
title:Lösung
$M\backslash A\subseteq M$, $A\times B\subseteq M\times M$ und $A\times \emptyset=\emptyset$ sind wahr.
```
## G1.2 Mengen
Seien $A,B,C$ Mengen. Beweisen Sie die folgenden Gleichungen
$$(A\backslash(B\cap C))=(A\backslash B)\cup(A\backslash C)$$
```ad-check
collapse:true
title:Lösung
$(A\backslash(B\cap C))=A\cap\overline{(A\cap B)}=(A\cap\overline{B})\cup (A\cap\overline{C})=(A\backslash B)\cup(A\backslash C)$
```

## G1.3 Transitionssysteme
Modellieren Sie eine Vekrehrsampel als endliches Transistionssystem
```ad-check
collapse:true
title:Lösung
rot$\rightarrow$rot/gelb$\rightarrow$grün$\rightarrow$gelb$\rightarrow$rot 
```
## G1.4 [[Äquivalenzrelation]]
Für eine zweistellige Relation $R\subseteq\mathbb{N}\times\mathbb{N}$ über $\mathbb{N}$ definiere die zweistellige Relation $\sim_R$ über $\mathbb{N}$ als die Menge von Paaren  
$(a_1, a_2) \in\mathbb{N}\times\mathbb{N}$, für die ein $b\in \mathbb{N}$ existiert, so dass $(a_1, b), (a_2, b) \in R$. Für welche der folgenden Relationen $R_i$ ist $\sim_{R_i}$  
eine Äquivalenzrelation?  
(a) $R_1 := {(a, b) \in \mathbb{N} \times \mathbb{N} : a + b = 17}$
(b) $R_2 := {(a, b) \in \mathbb{Z} × \mathbb{Z} : a \leq b \leq 3a}$
(c) $R3 := {(a, ak) : a, k \in \mathbb{N}}$

```ad-check
collapse:true
title:Lösung
$R_1$ ist nicht Reflexiv
$R_2$ ist nicht Symmetrisch
$R_3$ ist Reflexiv, Symmetrisch und Transitiv, also eine [[Äquivalenzrelation]]
```
## H1.1 Mengenoperationen
Seien $A,B,C$ Mengen. Beweisen Sie die folgenden Gleichungen:
$$(A\cap B)\cup C=(A\cup C)\cap(B\cup C)$$
$$B\backslash(B\backslash A) = A\text{ falls }A\subseteq B\text{. Gilt die Gleichung, selbst wenn }A\nsubseteq B?$$
```ad-check
collapse:true
title:Lösung
$\subseteq$: $x$ ist in $A$ und $B$ oder $x\in C$. Wenn $x$ in $C$ ist ist es in $(A\cup C)\cap(B\cup C)$. Wenn $x$ in $A$ und $B$ und nicht in $C$ ist, dann ist es auch in $(A\cup C)\cap (B\cup C)$.
$\supseteq$: $x$ ist in $A$ oder $C$ und in $B$ oder $C$. Wenn $x$ in $C$ ist, ist es auch in $(A\cap B)\cup C$. Wenn $x$ in $A$ ist und nicht in $C$, ist es auch in $B$, daher ist es in $(A\cap B)\cup C$, für $B$ analog.
$B\backslash(B\backslash A)=B\cap \overline{(B\backslash A)}=B\cap \overline{B\cap \overline{A}}$
$\subseteq$: $x$ ist also in $B$ und nicht in $B$ ohne $A$. $x$ ist also auf jeden Fall in $B$ oder in $\emptyset$. $x$ ist nicht in $B$ ohne $A$, also genau dann in $A$, wenn $A\subseteq B$.
```
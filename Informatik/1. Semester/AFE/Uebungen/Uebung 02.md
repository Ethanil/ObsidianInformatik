---
aliases: 
---
# Uebung 02
## G2.1: Quiz
Sei $\sim$ eine Äquivalenzrelation auf der Menge $\{ a, b, c, d \}$, für die $a\sim b, c \sim b, a \nsim d$ gilt. Welchen Index hat diese Äquivalenzrelation?  

Auf einem Tisch liegen vier Karten, die auf einer Seite eine Zahl und auf der anderen einen Buchstaben zeigen.  
Jemand behauptet, dass alle Karten mit einem Vokal auf der Buchstabenseite eine gerade Zahl auf der Zahlenseite  
haben. Sie sehen „D“, „8“, „E“ und „9“. Welche Karten müssen Sie umdrehen, um die Behauptung zu überprüfen?  

Wird durch $uRu^′ :\Leftrightarrow u = u^′$ oder $u = (u^′)^{−1}$eine Äquivalenzrelation auf $\Sigma^*$ definiert?  
- ja/nein

Sei $(B, \cdot, +, ′, 0, 1)$ eine Boolesche Algebra. Welche der folgenden Aussagen sind wahr?  
- $(B, \cdot, 1)$ ist eine Gruppe 
- $(B, +, 0)$ ist eine Gruppe 
- $(B, +, 1)$ ist ein Monoid 
- $(B, +, 0)$ ist ein Monoid  

Seien $A$ und $B$ zwei Strukturen des selben Typs mit Trägermengen $A$ und $B$, sowie $F : A \rightarrow B$ ein bijektiver Homomorphismus von $A$ nach $B$. Welche der folgenden Aussagen sind wahr?  
- $F^{-1}$ ist bijektiv 
- $F^{-1}$ ist ein Homomorphismus von $B$ nach $A$
- $(F^{-1})^{-1} = F$

```ad-check
collapse:true
title:Lösung
- Die Äquivalenzrelation hat einen Index von 2: $\{a,b,c\},\{d\}$
- Wir müssen "E" und "9" umdrehen, damit wir sicher wissen, dass alle Karten mit einem Vokal eine gerade Zahl auf der Rückseite haben.
- Ja
- $(B, +, 0)$ ist ein Monoid  
- $F^{-1}$ ist bijektiv 
- $(F^{-1})^{-1} = F$
```

## G2.2: Homomorphismen
Sei $\Sigma = \{a, b\}$. Bestimmen Sie alle Homomorphismen  
- von $(\mathbb{R}, \cdot)$ nach $(\mathbb{R}, +)$.  
- von $(\mathbb{Z}, +)$ nach $(\Sigma^*, \cdot)$.  
- von $(\Sigma^*, \cdot)$ nach $(\mathbb{Z}, +)$.

```ad-check
collapse:true
title:Lösung
Nur trivial
Nur trivial
Über die Länge des Wortes
```

## G2.3: Induktion
Beweisen Sie durch Induktion, dass
$$\sum^n_{i=1}i^2=\frac{1}{6}n(n+1)(2n+1)$$
für alle $n\in \mathbb{N}$ gilt.
```ad-check
collapse:true
title:Lösung
Induktionsstart $n=1$
$$\sum^1_{i=1}i^2=1^2=\frac{1}{6}*6=\frac{1}{6}1(1+1)(2*1+1)\checkmark$$
Induktionsschritt: $n\rightarrow n+1$
i.V.: $$\sum^n_{i=1}i^2=\frac{1}{6}n(n+1)(2n+1)$$
$$\sum^n+1_{i=1}i^2$$
$$=(n+1)^2+\sum^n_{i=1}i^2$$
$$\stackrel{i.V.}{=}(n+1)^2+\frac{1}{6}n(n+1)(2n+1)$$
$$=n^2+2n+1+\frac{1}{6}n(n+1)(2n+1)$$
$$=\frac{1}{6}6(n^2+2n+1)+\frac{1}{6}n(n+1)(2n+1)$$
$$=\frac{1}{6}(6n^2+12n+6+(n^2+n)(2n+1))$$
$$=\frac{1}{6}(6n^2+12n+6+2n^3+n^2+2n^2+n)$$
$$=\frac{1}{6}(2n^3+9n^2+13n+6)$$
$$=\frac{1}{6}((n+1)(2n^2+7n^1+6))$$
$$=\frac{1}{6}((n+1)((n+2)(2n+3)))$$
$$=\frac{1}{6}(n+1)((n+1+1)(2(n+1)+1))$$
```
## G2.4: Landau-Notation
Sein $f, g : \mathbb{N} \rightarrow \mathbb{N}$ Funktionen. Wir sagen „$f$ ist in $O(g)$“ (kurz „$f \in O(g)$“), falls es Konstanten $K, n_0$ gibt, so dass  
$$f(n) \leq K \cdot g(n) \text{ für alle }n \geq n_0.$$ 
Wir schreiben $f \sim g$, falls $f \in O(g)$ und $g \in O(f )$. $f \sim g$ besagt, dass $f$ und $g$ dieselbe Wachstumsrate haben.  
Zeigen Sie, dass $f \sim g$ eine Äquivalenzrelation auf der Menge aller Funktionen $\mathbb{N} \rightarrow \mathbb{N}$ ist

## H2.1 Quantoren und Implikation
Sei $X$ eine nichtleere Menge und seien $A(x), B(x)$ Aussagen mit $x \in X$. Bestimmen Sie, ob die folgenden Aussagen  
wahr oder falsch sind, und geben Sie einen Beweis bzw. ein Gegenbeispiel an:  
- $(\forall x \in X)(A(x) \rightarrow B(x)) \rightarrow (\forall x \in X)(A(x) \land B(x) \leftrightarrow A(x))$ 
- $((\forall x \in X)A(x) \rightarrow (\forall x \in X)B(x)) \rightarrow (\forall x \in X)(A(x) \rightarrow B(x))$ 
- $(\exists x \in X)(A(x) \rightarrow (\forall y \in X)A(y))$.  
Hinweis. Teilen Sie das Problem in zwei Fälle auf, nämlich $(\forall y \in X)A(y)$ gilt bzw. $(\forall y \in X)A(y)$ gilt nicht.
## H2.2: Graphen-Homomorphismen
Ein *gerichteter Graph* $G = (V, E)$ besteht aus einer endlichen Menge $V$ von Knoten und einer Teilmenge $E \subseteq V \times V$ von  
Kanten; wir nennen $E$ die Kantenrelation des Graphen $G$. Betrachten Sie die folgenden fünf gerichteten Graphen:
![[Pasted image 20220318163918.png]]
Der Graph $G_1 = (V_1, E_1)$ ist beispielsweise wie folgt formal gegeben:  
$V_1 = \{a, b, c, d\}$ 
$E_1 = \{(d, a), (d, b), (b, c), (c, d)\}$  
Geben Sie an, zwischen welchen Paaren von Graphen Homomorphismen existieren und zwischen welchen nicht. Falls  
ein Homomorphismus existiert, geben Sie einen an, und begründen Sie im anderen Fall, warum es keinen gibt.

## H2.3: Induktion
- Beweisen Sie die folgenden Aussagen jeweils per Induktion oder geben Sie ein Gegenbeispiel an.  
	- Es gilt $2^n > 2n$ für alle $n \geq 3$.  
	- Die Zahl $n^2 + n + 41$.  
- Sei $\Sigma$ ein beliebiges Alphabet. Die Funktion $f : \Sigma^* \rightarrow \mathbb{N}$ wird induktiv definiert durch  
$$f (\epsilon) = 1,$$
$$f (aw) = 1 + f (w), a \in \Sigma, w \in \Sigma^*. $$ 
Zeigen Sie mittels struktureller Induktion, dass  
$$f (v · w) = f (v) + f (w) − 1\text{, für alle }v, w \in \Sigma^*.$$

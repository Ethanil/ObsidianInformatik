---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}$$\newcommand{\F}[1]{\mathfrak{#1}}$$\newcommand{\b}[1]{\mathbb{#1}}$
# Syntax und Semantik der AL 
## Symbole
- $0,1 / F,W / \perp T$ - Wahrheitswerte, aussagenlogische Konstanten
- $p,q,r,\dotso p_1,p_2,\dotso$ - Aussagenvariablen
- $\neg$ - Junktor für [[Negation(nicht)]]
- $\land, \lor$ - Junktoren für [[Konjunktion(und)]], [[Disjunktion(oder)]]
- $\rightarrow, \leftrightarrow ,\dotso$ - weitere, definierte Junktoren

## Syntax
Zu einer Menge $V$ an aussagenlogischen Variablen ist die Menge der *aussagenlogischen Formeln* über Variablen aus $V$ ($AL(V)$), induktiv erzeugt mit:
- $0, 1, p$ (für $p\in V$)
- Wenn $\varphi\in AL(V)$, dann ist auch $\neg\varphi \in AL(V)$
- Wenn $\varphi, \psi \in AL(V)$, dann sind auch $(\varphi\land \psi), (\varphi\lor\psi) \in AL(V)$
### Standardvariablenmenge
Für $V=\{p_i:i\geq 1\}$ bzw $V_n=\{p_1,\dotso,p_n\}$ für $n\in \mathbb{N}$ sei
$$AL:=AL(V)$$
$$AL_n:=AL(V_n)$$
## Interpretation (Belegung)
Eine $\mathcal{V}$-Interpretation ist eine Funktion
$$\begin{align}
	\F{I}:V\rightarrow&\ \mathbb{B}\\ 
	p \rightarrow&\ \F{I}(p)
\end{align}$$
$\F{I}$ interpretiert $p$ als
- "wahr", wenn $\F{I}(p)=1$
- "falsch", wenn $\F{I}(p)=0$

Jeder Formel $\varphi\in AL(\f{V})$ wird zu einer gegebenen $\f{V}$-Interpretation ein Wahrheitswert $\varphi^\F{I}\in\b{B}$ zugeordnet:
$$\begin{align}
^\F{I}:AL(\f{V})\rightarrow&\ \b{B} \\
\varphi\rightarrow&\ \varphi^\F{I}
\end{align}$$
Diese Funktion wird induktiv über den Aufbau der Formel $\varphi$ definiert:
- $0^\F{I}:=0; 1^\F{I}:=1; p^\F{I}:=\F{I}(p)$
- $(\neg \varphi)^\F{I}:=1-\varphi^\F{I}$
- $(\varphi\land\psi)^\F{I}:=min(\varphi^\F{I},\psi^\F{I}) (=\varphi^\F{I}\cdot\psi^\F{I})$
- $(\varphi\lor\psi)^\F{I}:=max(\varphi^\F{I},\psi^\F{I})(=\varphi^\F{I}+\psi^\F{I}-\varphi^\F{I}\cdot\psi^\F{I})$

## Semantik
Wir sagen $\F{I}$ erfüllt $\varphi$ und schreiben $\F{I}\vDash\varphi$  genau dann wenn $\varphi^\F{I}=1$. Das gleiche gilt auch für Formelmengen $\Phi\subseteq AL(\f{V})$ genau dann wenn $\F{I}\vDash\varphi \ \forall \varphi\in\Phi$
Andere Sprechweisen für "$\F{I}$ erfüllt $\varphi$":
- $\F{I}$ ist Modell von $\varphi$
- $\varphi$ ist wahr unter $\F{I}$
Die Relation $\vDash$ nennen wir Modellbeziehung.
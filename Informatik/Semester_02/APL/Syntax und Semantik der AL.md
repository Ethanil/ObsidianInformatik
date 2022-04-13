---
aliases: 
---
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
	I:V\rightarrow \mathbb{B}\\ 
	p \rightarrow \F{I}(p)
\end{align}$$
$\F{I}$ interpretiert $p$ als
- "wahr", wenn $\F{I}(p)=1$
- "falsch", wenn $\F{I}(p)=0$

---
aliases: Interpretation, Belegung, Interpretationen, Belegungen
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Interpretation (Belegung) 
Eine $\mathcal{V}$-Interpretation ist eine Funktion
$$\begin{align}
	\F{I}:V\rightarrow&\ \mathbb{B}\\ 
	p \rightarrow&\ \F{I}(p)
\end{align}$$
$\F{I}$ interpretiert $p$ als
- "wahr", wenn $\F{I}(p)=1$
- "falsch", wenn $\F{I}(p)=0$

Jeder [[Syntax und Semantik der AL|Formel]] $\varphi\in AL(\f{V})$ wird zu einer gegebenen $\f{V}$-Interpretation ein Wahrheitswert $\varphi^\F{I}\in\b{B}$ zugeordnet:
$$\begin{align}
^\F{I}:AL(\f{V})\rightarrow&\ \b{B} \\
\varphi\rightarrow&\ \varphi^\F{I}
\end{align}$$
Diese Funktion wird induktiv über den Aufbau der Formel $\varphi$ definiert:
- $0^\F{I}:=0; 1^\F{I}:=1; p^\F{I}:=\F{I}(p)$
- $(\neg \varphi)^\F{I}:=1-\varphi^\F{I}$
- $(\varphi\land\psi)^\F{I}:=min(\varphi^\F{I},\psi^\F{I}) (=\varphi^\F{I}\cdot\psi^\F{I})$
- $(\varphi\lor\psi)^\F{I}:=max(\varphi^\F{I},\psi^\F{I})(=\varphi^\F{I}+\psi^\F{I}-\varphi^\F{I}\cdot\psi^\F{I})$

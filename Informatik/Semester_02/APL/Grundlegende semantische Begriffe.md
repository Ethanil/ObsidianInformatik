---
aliases: Tautologie, Allgemeingültigkeit, allgemeingültig, allgemeingültige
---
$\newcommand{\f}[1]{\mathcal{#1}}$$\newcommand{\F}[1]{\mathfrak{#1}}$$\newcommand{\b}[1]{\mathbb{#1}}$
# Grundlegende semantische Begriffe 
## Folgerungsbeziehung
$\varphi \vDash \psi$ bzw. $\Phi \vDash \psi$ für $\varphi,\psi\in AL(\f{V})$ und $\Phi\subseteq AL(\f{V})$ bedeutet für alle $\f{V}$-[[Interpretation (Belegung)|Interpretationen]] $\F{I}$:
$$\begin{align}
\F{I}\vDash \varphi &\Rightarrow \F{I}\vDash \psi \\
&\text{bzw.} \\
\F{I}\vDash \Phi &\Rightarrow \F{I}\vDash \psi
\end{align}$$
### Allgemeingültigkeit
Wenn eine Formel allgemeingültig ist, heißt dies, dass sie für jede [[Interpretation (Belegung)|Interpretation]] gültig ist. Man nennt dies auch Tautologie.
Schreiben tut man dies mit $\vDash \varphi$ 
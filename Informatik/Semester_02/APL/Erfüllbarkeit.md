---
aliases: erfüllbar, erfüllbaren, erfüllbare
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Erfüllbarkeit 
Eine Formel $\varphi\in AL(\f{V})$ oder Formelmenge $\Phi\subseteq AL(\f{V})$ heißt erfüllbar genau dann wenn eine [[Interpretation (Belegung)|Interpretation]] $\F{I}$ exisitert mit $\F{I}\vDash\varphi$ bzw. $\F{I}\vDash\varphi \ \forall\ \varphi\in\Phi$.
## Menge der erfüllbaren Formeln
Die Menge der erfüllbaren Formeln schreiben wir mittels $SAT$ (satisfiability), genauer bspw.  $SAT(AL)$. 
### Allgemeingültigkeit
Die [[Grundlegende semantische Begriffe|Allgemeingültigkeit]] kann auch definiert werden durch
```ad-note
title:Definition
$$\varphi\text{ ist genau dann allgemeingültig, wenn }\neg\varphi\text{ nicht erfüllbar ist.}$$
```

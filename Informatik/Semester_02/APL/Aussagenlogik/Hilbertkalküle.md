---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Hilbertkalküle 
## Syntax
Eine In einem Hilbertkalkül wird neben Aussagenvariablen(Formeln) und Konstanten ($0,1$) auch $\vdash$ verwendet. $A \vdash B$ bedeutet, $B$ ist aus $A$ herleitbar oder $A$ beweist $B$.
Eine alternative Schreibweise das metasprachliche Zeichen $\vdash$ zu notieren ist mittels eines Bruchstriches:
$$\{A,A \rightarrow B\}\vdash B \Leftrightarrow \frac{A, A \rightarrow B}{B}$$


## Aufbau
Ein Hilbertkalkül benutzt ein Axiomschemata aus [[Grundlegende semantische Begriffe|Tautologien]] worauf eine Hypothese mittels des [[Modus Ponens]] zurückführbar ist.

```ad-example
title:Beispiel
collapse:
$$\begin{align}
&\varphi \rightarrow (\phi \rightarrow \varphi) \\
&(\varphi \rightarrow (\phi \rightarrow \chi)) \rightarrow ((\varphi \rightarrow \psi) \rightarrow (\varphi \rightarrow \chi)) \\
&\varphi \rightarrow \varphi \lor \psi \\
&\psi \rightarrow \varphi \lor \psi \\
&(\varphi \rightarrow \chi) \rightarrow ((\psi \rightarrow \chi) \rightarrow(\varphi \lor \psi \rightarrow \chi)) \\
&\varphi \land psi \rightarrow \varphi \\
&\varphi \land psi \rightarrow \psi \\
&\varphi \rightarrow (\psi \rightarrow \varphi \land \psi) \\
&0 \rightarrow \varphi \\
&\neg \neg \varphi \rightarrow \varphi
\end{align}$$
Hypothese:
$$\varphi \rightarrow \varphi$$
Herleitungsschritte:
$$\begin{align}

\end{align}$$
```

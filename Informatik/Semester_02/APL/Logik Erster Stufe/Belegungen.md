---
aliases: 
---
# Belegungen 
Variablenfreie $S$-[[Terme]] haben in jeder $S$-[[Strukturen|Struktur]] $\mathcal{A}$ eine eindeutige Interpretation.
Für Terme mit Variablen braucht man auch eine Interpretation der Variablen, die Belegung der Variablen.
```ad-abstract
title:Definition - Belegungen und Interpretationen
Eine Funktion $\beta:V \rightarrow A$ heißt Belegung (für die $x \in V$) in der $S$-Struktur $\mathcal{A}=(A,\dotso)$.
Eine $S$-Struktur $\mathcal{A}$ und Belegung $\beta$ zusammen bilden eine $S$-Interpretation $\mathfrak{I}=(\mathcal{A},\beta)$
```
## Semantik
Für jede $S$-Interpretation $\mathfrak{I}=(\mathcal{A},\beta)$ können wir induktiv als Interpretation von $t \in T(S)$ das von $t$ bezeichnete Element $t^{\mathfrak{I}}\in A$ definieren:
- Für $t=x(x \in V$ Variable$): t^{\mathfrak{I}}:=\beta(x)$
- Für $t=c(c \in S \text{Konstantensymbol}): t^{\mathfrak{I}}:=c^{\mathcal{A}}$
- Für $t=ft_{1}\dotso t_{n},$ mit $n$-stelligem Funktionssymbol $f \in S: t^{\mathfrak{I}}:=f^{\mathcal{A}}(t^{\mathfrak{I}}_{1},\dotso,t^{\mathfrak{I}}_{n})$

## Schreibweisen für Belegungen und Interpretationen
Zu $\beta: V \rightarrow A$ bezeichnet $\beta[x \mapsto a]$ die abgeänderte Belegung $\beta'$ mit
$$\begin{align}
\beta'(y)=
\begin{cases}
a& &\text{für }y=x\\
\beta(y)& &\text{sonst.}
\end{cases}
\end{align}$$
Analog bei Interpretationen $\mathfrak{I}=(\mathcal{A},\beta): \mathfrak{I}[x \mapsto a]$ steht für die Variante $(\mathcal{A},\beta[x \mapsto a])$.
## Links
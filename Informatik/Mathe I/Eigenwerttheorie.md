---
aliases: Eigenwert, Eigenwerte, Eigenvektor, Eigenvektoren
---
# Eigenwerttheorie
Es sei $V$ ein $K$-[[Vektorraum]] und $\phi: V\rightarrow V$ eine [[Lineare Abbildungen|Lineare Abbildung]]. Ein $\lambda \in K$ heißt Eigenwert von $\phi$, falls es einen Vektor $v \in V$ gibt mit $v\neq 0$ und $\phi(v)=\lambda v$. Ein solches $v$ heißt dann Eigenvektor von $\phi$ zum Eigenwert $\lambda$.

```ad-example
collapse:true
title: Beispiel: Spiegelung an der $x_2$-Achse im $\mathbb{R}^2$
Ist $\phi: \mathbb{R}^2 \rightarrow\mathbb{R}^2$ die Spiegelung an der $x_2$-Achse, so gilt für den ersten [[Basis|Standardbasisvektor]] $e_1=\begin{pmatrix}
1 \\ 0
\end{pmatrix}$ die Beziehung $\phi(e_1)=-e_1$, dieser ist also ein Eigenvektor von $\phi$ zum Eigenwert $-1$. Weiter ist der zweite [[Basis|Standardbasisvektor]] $e_2=\begin{pmatrix}
0 \\ 1
\end{pmatrix}$ ein Eigenvektor zum Eigenwert $1$, denn $\phi(e_2)=e_2$
```

---
aliases: Eigenwert, Eigenwerte, Eigenvektor, Eigenvektoren, Eigenraum, Eigenräume
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
## Eigentwert berechnen
Die Eigenwerte einer [[Lineare Abbildungen|Lineare Abbildung]] berechnen wir durch
$$det(A-\lambda I)=0$$
Siehe [[Determinante]].

## Eigenraum
Für jedes $\lambda \in K$ ist der Eigenraum von $\phi$ zum Eigenwert $\lambda$
$$E(\phi,\lambda):=\{v\in V:\phi(v)=\lambda v\}$$
ein Untervektorraum von $V$ und der Eigenraum von $A$ zum Eigenwert $\lambda$
$$E(A,\lambda):=\{x\in K^n:(A-\lambda I)x=0\}=ker(A-\lambda I)$$
ein Untervektorraum von $K^n$
Eigenvektoren zu verschiedenen Eigenwerten von $\phi$(bzw $A$) sind [[Lineare Unabhängigkeit|linear unabhängig]].
Sind $\lambda_1,\lambda_2,\dotso,\lambda_r$ verschiedene Eigenwerte von $\phi$(bzw $A$) und $B_1, B_2, \dotso, B_r$ Basen von $E(\phi,\lambda_1), E(\phi,\lambda_2), \dotso,E(\phi,\lambda_3)$ (bzw von $E(A,\lambda_1), E(A,\lambda_2), \dotso,E(A,\lambda_3)$ ), so ist die Menge $B:=B_1\cup B_2 \cup\dotso\cup B_r$ [[Lineare Unabhängigkeit|linear unabhängig]].
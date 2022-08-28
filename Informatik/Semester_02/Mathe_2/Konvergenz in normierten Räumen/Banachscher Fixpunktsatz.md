---
aliases: 
---
# Banachscher Fixpunktsatz 
```ad-abstract
title:Definition - Banach'scher Fixpunktsatz
Es sei $(V,||\cdot||_{V})$ ein [[vollständiger Vektorraum|Banachraum]], $M \subseteq V$ [[offen abgeschlossen beschränkt|abgeschlossen]] und $f: M \rightarrow M$ eine Funktion. Weiter exisitere ein $q \in (0,1)$, so dass
$$
\begin{align}
&||f(x)-f(y)||_{V} \leq q ||x-y||_{V} &&\text{für alle }x,y \in M
\end{align}$$
gilt. Dann gelten die folgenden Aussagen:
- Es gibt genau ein $v \in M$ mit $f(v)=v$ (D.h. $f$ hat genau einen Fixpunkt in $M$.)
- Für jedes $x_{0} \in M$ konvergiert die Folge $(x_n)$ mit $x_{n+1}=f(x_{n}), n \in \mathbb{N}$ gegen $v$ und es gelten die folgenden Fehlerabschätzungen für jedes $n \in \mathbb{N}^*:$
$$\begin{align}
&||x_n-v||_{V}\leq \frac{q^{n}}{1-q}||x_{1}-x_{0}||_{V} &&\text{(A-priori-Abschätzung)} \\
&||x_n-v||_{V}\leq \frac{q^{n}}{1-q}||x_{n}-x_{n-1}||_{V} &&\text{(A-posteriori-Abschätzung)}
\end{align}$$
```

## Links
[[vollständiger Vektorraum|Banachraum]]
[[offen abgeschlossen beschränkt|abgeschlossen]]

---
aliases: Reliability
---
# Zuverlässigkeit 

```ad-abstract
title:Definition - Variablendefinition
$T$ - reelle Zuvallsvariable, die die "Lebenszeit des Systems" darstellt

$F$ - Verteilungsfunktion dieser Zuvallsvariable

$f$ - Die zu $F$ gehörige Dichtefunktion

$t$ - Ein beliebiger Zeitpunkt

$R(t)$ - Überlebensfunktion bzw Zuverlässigkeitsfunktion
```

```ad-abstract
title:Definition - Verteilungsfunktion
$F(t) = P(T \leq t)$
```

```ad-abstract
title:Definition - Überlebensfunktion $R(t)$
$R(t) = P(T>t) = 1 - F(t)$
```

## Exponentielles Modell
Wir bezeichnen die Fehlerrate, also die durchschnittliche Zahl der Fehler pro Zeiteinheit mit $\lambda$ und erhalten damit

$$\begin{align}
f(x) &= &\begin{cases}
\lambda e^{-\lambda x} & &x \geq 0 \\
0& &x < 0
\end{cases}\\
F(t) &= \int^{t}_{-\infty}f(x) dx &= \begin{cases}
1-e^{-\lambda t}& &t \geq 0 \\
0& &t < 0
\end{cases}\\
R(t) &= 1-F(t) &= \begin{cases}
e^{-\lambda t}& &t \geq 0 \\
1& &t < 0
\end{cases}
\end{align}
$$
damit können wir auch die Mean Time to Failure(MTTF) der [[Verfügbarkeit]] als Erwartungswert bis zu einem Ausfall bestimmen:

$$MTTF = E[T] = \int^{\infty}_{0}1- F(t) dt - \int^{0}_{-\infty}F(t) dt = \int^{\infty}_{0} R(t)dt $$
und konkret für unser exponentielles Modell dann
$$MTTF = \int^{\infty}_{0}e^{-\lambda t} dt = \frac{1}{\lambda}$$
## Systeme mit mehreren Komponenten
### Reihenschaltung
Bei in Reihe geschalteten, unabhängigen Komponenten müssen die Wahrscheinlichkeit für ein Failure für jede Komponente multipliziert werden
### Parallelschaltung
Bei einer Parallelschaltung müssen alle Komponenten ausfallen, damit das ganze System ausfällt, wodurch wir die Gegenwahrscheinlich
## Links
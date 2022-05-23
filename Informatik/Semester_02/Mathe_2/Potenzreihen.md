---
aliases: 
---
# Potenzreihen 
```ad-abstract
title:Definition - Potenzreihe
Es sei $(a_{n})$ eine Folge in $\mathbb{K}$. Eine Reihe der Form
$$\begin{align}
\sum^{\infty}_{n=0}a_{n}x^{n}=a_{0}+a_{1}x+a_{2}x^{2}+a_{3}x^{3}+\dotso
\end{align}$$
heißt Potenzreihe
```
```ad-abstract
title:Definition - Satz von Hadamard
Es sei $(a_{n})$ eine Folge in $\mathbb{K}$, so dass der Grenzwert $\varrho:=\lim_{n\rightarrow \infty}\sqrt[n]{|a_{n}|}$ exisitert oder die Folge $(\sqrt[n]{|a_{n}|})$ unbeschränkt ist. Dann gelten die folgenden Konvergenzaussagen für die Potenzreihe $\sum^{\infty}_{n=0}a_{n}x^{n}:$
- Ist die Folge $(\sqrt[n]{|a_{n}|})$ unbeschränkt, so konvergiert die Potenzreihe nur für $x=0$
- Ist $\varrho=0$, so konvergiert die Potenzreihe für alle $x \in \mathbb{K}$ absolut.
- Ist $\varrho \in (0, \infty)$, so ist die Potenzreihe für alle $x \in \mathbb{K}$ mit $|x|<\frac{1}{\varrho}$ absolut konvergent und für alle $x \in \mathbb{K}$ mit $|x|> \frac{1}{\varrho}$ divergent.
```
```ad-abstract
title:Definition - Quotientenkriterium für Potenzreihen
Es sei $(a_{n})$ eine Folge in $\mathbb{K}$ mit $a_{n}\neq 0$ für alle $n \in \mathbb{N}$, so dass $\sigma:=\lim_{n\rightarrow \infty}\left|\frac{a_{n+1}}{a_{n}}\right|$ existiert. Dann gilt für den Konvergenzradius $r$ von $\sum^{\infty}_{n=0}a_{n}x^{n}$
$$\begin{align}
r=\begin{cases}
\frac{1}{\sigma}\text{, falls }\sigma \in (0, \infty) \\
\infty \text{, falls }\sigma=0.
\end{cases}
\end{align}$$
```

```ad-abstract
title:Definition - Erweiterung des Potenzreihen Begriffs.
Es sei $(a_{n})$ eine Folge in $\mathbb{K}, n_{0} \in \mathbb{N}$ und $x_{0}\in \mathbb{K}$. Dann nennt man eine Reihe der Form
$$\begin{align}
\sum^{\infty}_{n=n_{0}}a_{n}(x-x_{0})^{n}
\end{align}$$
Potenzreihe. der Punkt $x_{0}$ wird Entwicklungspunkt der Potenzreihe genannt.
```
```ad-abstract
title:Definition - Reihe mit Konvergenzradius als Funktion
Es sei $\sum^{\infty}_{n=0}a_{n}x^{n}$ eine Potenzreihe in $\mathbb{K}$ mit Konvergenzradius $r>0$. Dann ist die dadurch gegebene Funktion $f: \{x \in \mathbb{K}:|x|<r\}\rightarrow \mathbb{K}$ mit $f(x)=\sum^{\infty}_{n=0}a_{n}x^{n}$ stetig auf $\{x \in \mathbb{K}: |x|<r\}$
```

## Links
[[Reihen|Reihe]]
[[offen abgeschlossen beschränkt|beschränkt]]
[[Folge]]


---
aliases: 
---
# Grenzwertbegriff für Funktionen 
````ad-abstract
title:Definition - Grenzwertbegriffe für Funktionen
collapse:
Es sei $D \subseteq \mathbb{R}$ eine Menge, $f: D \rightarrow \mathbb{R}$ eine Funktion und $x_{0} \in \mathbb{R}$
```ad-abstract
title:Definition - Häufungspunkt von $D$
Wir nennen $x_{0}$ einen Häufungspunkt von $D$, falls es eine Folge $(a_{n})$ in $D$ mit $a_{n} \neq x_{0}$ für alle $n \in \mathbb{N}$ gibt, die gegen $x_{0}$ konvergiert.
```
```ad-abstract
title:Definition - Grenzwert von $f$
Ist $x_{0}$ ein Häufungspunkt von $D$, so sagen wir, dass $f$ für $x$ gegen $x_{0}$ den Grenzwert $y$ hat, wenn für jede Folge $(a_{n})$ in $D$, die gegen $x_{0}$ konverigert und für die $a_{n} \neq x_{0}$ für alle $n \in \mathbb{N}$ gilt, die Folge $(f(a_{n}))$ gegen $y$ konvergiert. Wir schreiben dafür
$$\lim_{x \rightarrow x_{0}}f(x)=y$$
```
```ad-abstract
title:Definition - rechtsseitiger Grenzwert von $f$
Ist $x_{0}$ ein Häufungspunkt von $D_{+}:=\{x \in D : x > x_{0}\}$, so hat $f$ für $x$ gegen $x_{0}$ den rechtsseitigen Grenzwert $y$, wenn für jede Folge $(a_{n})$ in $D_{+}$, die gegen $x_{0}$ konvergiert, die Folge $(f(a_{n}))$ gegen $y$ konvergiert. Wir schreiben dafür
$$\lim_{x \rightarrow x_{0}+}f(x)=y$$
```
```ad-abstract
title:Definition - linksseitiger Grenzwert von $f$
Ist $x_{0}$ ein Häufungspunkt von $D_{-}:=\{x \in D : x < x_{0}\}$, so hat $f$ für $x$ gegen $x_{0}$ den linksseitigen Grenzwert $y$, wenn für jede Folge $(a_{n})$ in $D_{-}$, die gegen $x_{0}$ konvergiert, die Folge $(f(a_{n}))$ gegen $y$ konvergiert. Wir schreiben dafür
$$\lim_{x \rightarrow x_{0}-}f(x)=y$$
```
````

```ad-abstract
title:Definition - rechts und linksseitiger zu allgemeinem Grenzwert
collapse:
Es sei $D \subseteq \mathbb{R}, f: D \rightarrow \mathbb{R}$ eine Funktion und $x_{0} \in \mathbb{R}$. Exisiteren $\lim_{x \rightarrow x_{0}-}f(x)$ *und* $\lim_{x \rightarrow x_{0}+}f(x)$ und sind die beiden Werte gleich, so exisitert auch $\lim_{x \rightarrow x_{0}}f(x)$ und es gilt
$$\lim_{x \rightarrow x_{0}}f(x)=\lim_{x \rightarrow x_{0}-}f(x)=\lim_{x \rightarrow x_{0}+}f(x)$$
```

````ad-abstract
title:Definition - Rechenregeln
collapse:
Es sei $D \subseteq \mathbb{R}$ und $x_{0}$ ein H#ufungspunkt von $D$. Desweiteren seien drei Funktionen $f,g,h:D \rightarrow \mathbb{R}$ gegeben, so dass die Grenzwerte $\lim_{x \rightarrow x_{0}}f(x)$ und $\lim_{x \rightarrow x_{0}}g(x)$ exisiteren. Dann gilt:
```ad-abstract
title: $+,\cdot, ||$
Die Grenzwerte für $x$ gegen $x_{0}$ von $f+g, fg$ und $|f|$ existieren und es gilt
$$\begin{align}
\lim_{x \rightarrow x_{0}}(f(x)+g(x)) &= \lim_{x \rightarrow x_{0}}f(x) + \lim_{x \rightarrow x_{0}} g(x) \\
\lim_{x \rightarrow x_{0}}(f(x)g(x)) &= \lim_{x \rightarrow x_{0}}f(x) \cdot \lim_{x \rightarrow x_{0}} g(x) \\
\lim_{x \rightarrow x_{0}}|f(x)| &= |\lim_{x \rightarrow x_{0}}f(x)|\\
\end{align}$$
```
```ad-abstract
title:$leq$
Gilt $f(x) \leq g(x)$ für alle $x \in D \backslash \{x_{0}\}$, so ist $\lim_{x\rightarrow x_{0}}f(x) \leq \lim_{x\rightarrow x_{0}}g(x)$
```
```ad-abstract
title:$=$
Ist $\lim_{x\rightarrow x_{0}}f(x)=\lim_{x\rightarrow x_{0}}g(x)$ und gilt
$$\begin{align}
f(x)\leq h(x) \leq g(x)& &\text{für alle }x \in D \backslash \{x_{0}\}
\end{align}$$
so gilt auch $\lim_{x\rightarrow x_{0}}h(x)=\lim_{x\rightarrow x_{0}}f(x)=\lim_{x\rightarrow x_{0}}g(x)$
```
```ad-abstract
title: /
Ist $y:=\lim_{x\rightarrow x_{0}}g(x) \neq 0$, so exisitert ein $\delta>0$, so dass $|g(x)|\geq |y|/2$ für alle $x \in (D \cap(x_{0}-\delta,x_{0}+\delta))\backslash \{x_{0}\}$ ist. Wir können also die Funktion
$$\begin{align}
\frac{f}{g}:(D \cap(x_{0}-\delta,x_{0}+\delta))\backslash \{x_{0}\} \rightarrow \mathbb{R}& &\text{ mit } &\frac{f}{g}(x):=\frac{f(x)}{g(x)}
\end{align}$$
definieren. Für diese exisitert dann der Limes für $x$ gegen $x_{0}$ mit
$$\begin{align}
\lim_{x\rightarrow x_{0}}\frac{f(x)}{g(x)}=\frac{\lim_{x\rightarrow x_{0}}f(x)}{\lim_{x\rightarrow x_{0}}g(x)}
\end{align}$$
```
````

````ad-abstract
title:Definition - unendliche Grenzwerte und Grenzwerte für $x_{0}$ gegen unendlich
collapse:
```ad-abstract
title:Definition - Grenzwert gegen $\infty$
Es seien $D \subseteq \mathbb{R}, f: D \rightarrow \mathbb{R}$ eine Funktion und $x_{0}$ ein Häufungspunkt von $D$. Wir schreiben
$$\begin{align}
\lim_{x\rightarrow x_{0}}f(x) = \infty& &\text{(bzw. }\lim_{x\rightarrow x_{0}}f(x)=-\infty)
\end{align}$$
wenn für jede Folge $(a_{n})$ in $D$, die gegen $x_{0}$ konvergiert und für die $a_{n}\neq x_{0}$ für alle $n \in \mathbb{N}$ gilt, die Folge $(f(a_{n}))$ bestimmt gegen $\infty$ (bzw. $-\infty$) divergiert.
```
```ad-abstract
title:Definition - Grenzwert für $x_{0}$ gegen $\infty$
Es sei $D \subseteq \mathbb{R}$ nicht nach oben (bzw. unten) beschränkt, $f: D \rightarrow \mathbb{R}$ eine Funktion und $y \in \mathbb{R}\cup \{\infty,-\infty\}$. Wir sagen
$$\begin{align}
\lim_{x\rightarrow \infty}f(x)=y& &\text{(bzw. }\lim_{x\rightarrow -\infty}f(x)=y)
\end{align}$$
wenn für jede Folge $(a_{n})$ in $D$, die bestimmt gegen $\infty$ (bzw. $-\infty$) divergiert, $\lim_{n\rightarrow \infty}f(a_{n})=y$ gilt.
```
````

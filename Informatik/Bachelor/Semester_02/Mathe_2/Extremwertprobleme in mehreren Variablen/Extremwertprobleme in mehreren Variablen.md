---
aliases: 
---
# Extremwertprobleme in mehreren Variablen 
Im Prinzip gleich wie [[Extremwerte]], aber komplizierter und wir suchen nur welche in $\mathbb{R}$, nicht $\mathbb{R}^{p}$, da Vektoren darin nicht vergleichbar sind
````ad-abstract
title:Definition - Extrema
Es sei $G \subseteq \mathbb{R}^{d}$ und $f: G \rightarrow \mathbb{R}$ eine Funktion
```ad-abstract
title:
Man sagt, dass $f$ in $x_{0} \in G$ ein globales Maximum (bzw. globales Minimum) hat, falls $f(x) \leq f(x_{0})$ (bzw $f(x) \geq f(x_{0})$) für alle $x \in G$ gilt
```
```ad-abstract
title:
$f$ hat in $x_{0} \in G$ ein relatives Maximum (bzw. relatives Minimum), falls ein $\delta > 0$ existiert, so dass $f(x) \leq f(x_{0})$ (bzw. $f(x) \geq f(x_{0})$) für alle $x \in G$ mit $||x-x_{0}||< \delta$ gilt.
```
```ad-abstract
title:
Allgemein spricht man von einem globalen bzw. relativen Extremum in $x_{0}$, wenn $f$ dort ein entsprechendes Maximum oder Minimum hat.
```
````
```ad-abstract
title:
Es sei $G \subseteq \mathbb{R}^{d}$ und $x_{0}$ ein innerer Punkt von $G$, sowie $f: G \rightarrow \mathbb{R}$ total differenzierbar in $x_{0}$. Hat $f$ in $x_{0}$ ein relatives Extremum, so gilt $\Delta f(x_{0})=0$
```
````ad-abstract
title:
Es sei $G \subseteq \mathbb{R}^{d}$ offen, $f: G \rightarrow \mathbb{R}$ zweimal stetig partiell differenzierbar und für $x_{0} \in G$ gelte $\Delta f(x_{0})=0$. Ist dann die Hesse-Matrix $H_{f}(x_{0})$
```ad-abstract
title:
positiv definit, so hat $f$ in $x_{0}$ ein relatives Minimum
```
```ad-abstract
title:
negativ definit, so hat $f$ in $x_{0}$ ein relatives Maximum
```
```ad-abstract
title:
indefinit, so hat $f$ in $x_{0}$ kein relatives Extremum
```
````

## Links
[[Definitheit]]
[[offen abgeschlossen beschränkt]]
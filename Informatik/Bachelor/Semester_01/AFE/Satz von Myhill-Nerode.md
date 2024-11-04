---
aliases: 
---
# Satz von Myhill-Nerode
Wenn eine Sprache $L$ einen endlichen Index hat, dann ist sie [[Reguläre Sprache|regulär]]. 

Damit können wir Sprachen die nicht regulär sind erkennen:
Wenn wir beweisen können, dass wir unendlich nicht äquivalente Wörter erzeugen können, dann ist die Sprache nicht regulär.
Das ist möglich, indem wir unendlich viele unterschiedliche Paare erzeugen und an diese dann jeweils ein Wort konkatinieren, sodass eines der beiden akzeptiert wird und das andere nicht:
```ad-example
title:Beispiel
$$L=\{a^nb^n:n\in\mathbb{N}\}\subset\{a,b\}*$$
Betrachte $w_n=a^n$ und $m\neq n$ mit $m,n\in\mathbb{N}$
$w_n\nsim_L w_m$, da wir an beide $b^n$ dranhängen können und $w_n$ ist dann in $L: w_n\cdot b^n=a^nb^n\in L$ aber wenn wir das selbe an $w_m$ anhängen ist das Wort nicht in $L$, da $n\neq m: w_m\cdot b^n=a^mb^n$
```

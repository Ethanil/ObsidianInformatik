# Untergruppen
Eine [[Teilmengenbeziehungen|Teilmenge]] $U$ einer [[Gruppen|Gruppe]] $(G,*)$ heißt Untergruppe von $G$, falls auch $(U,*)$ eine Gruppe ist. 

## triviale Untergruppen
Die Teilmengen $G$ und $\{n\}$ sind immer Untergruppen einer Gruppe, man nennt sie deshalb auch triviale Untergruppen von $G$.

## Kriterien
Eine Teilmenge $U$ einer Gruppe $(G,*)$  ist genau dann eine Untergruppe von $G$, wenn
1. $U\neq \emptyset$
2. $\forall a,b\in U: a*\overline{b}\in U$

Diese Kriterien gelten nach folgendem Beweis:
```ad-note
title:Beweis
collapse:false
"$\Rightarrow$": Ist $U$ eine Untergruppe, so muss $U$ eine Gruppe sein und damit nach [[Gruppen#Existenz eines neutralen Elements|(n)]] zumindest ein neutrales Element enthalten, also ist $U$ nicht leer und wir haben 1. beweisen.
Wir müssen als nächstes zeigen, dass das neutrale Element $n_u\in U$ das selbe ist wie das neutrale Element $n_g\in G$. Dazu bezeichnen wir das Inverse von $n_u\in G$(nicht in $U$!) als $\overline{n_u}$. Dann gilt $n_u=n_u*n_u$
$$n_g=$$
```
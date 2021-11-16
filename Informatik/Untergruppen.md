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
collapse:true
"$\Rightarrow$": Ist $U$ eine Untergruppe, so muss $U$ eine Gruppe sein und damit nach [[Gruppen#Existenz eines neutralen Elements|(n)]] zumindest ein neutrales Element enthalten, also ist $U$ nicht leer und wir haben 1. beweisen.
Wir müssen als nächstes zeigen, dass das neutrale Element $n_u\in U$ das selbe ist wie das neutrale Element $n_g\in G$. Dazu bezeichnen wir das Inverse von $n_u\in G$(nicht in $U$!) als $\overline{n_u}$. Dann gilt $n_u=n_u*n_u$
$$n_g=n_u*\overline{n_u}=(n_u*n_u)*\overline{n_u}=n_u*(n_u*\overline{n_u})=n_u*n_g=n_u$$
Seien nun $a,b\in U$ und sei $\overline{b}$ das inverse Element von $b\in G$. Da $U$ eine Gruppe ist, hat $b$ auch ein inverses Element $b^\#\in U$. Wir haben wegen [[Gruppen#Existenz des inversen Elements|(i)]] und dem vorausgehden Beweis außerdem $b*b^\#=b^\#*b*=n_u=n_g$, also ist $b^\#=\overline{b}$. Da $a$ und $\overline{b}$ also in $U$ sind und $U$ eine Gruppe ist, muss $a*\overline{b}$ auch in $U$ vorhanden sein.
"$\Leftarrow$" Sei $U\subseteq G$ so, dass 1. und 2. gelten. Wir müssen zeigen, dass $U$ dann eine Gruppe ist, d.h. dass $*:U\times U\rightarrow U$gilt und die Axiome [[Gruppen#Assoziativität|(a)]], [[Gruppen#Existenz eines neutralen Elements|(n)]] und [[Gruppen#Existenz des inversen Elements|(i)]] erfüllt sind.
Zunächst ist $*$ auf $U$ assoziativ, da dies auf $G$ gilt. Wir haben also [[Gruppen#Assoziativität|(a)]].
Weiter gibt es wegen 1. auf jeden Fall irgendein $a\in U$. Wegen 2. ist dann auch $a*\overline{a}=n\in U$. Nun ist jedes Element $b\in U$ auch in $G$ und daort gilt $n*b=b$ und $b*n=b$, also gilt das auch in $U$ und wir haben [[Gruppen#Existenz eines neutralen Elements|(n)]] gezeigt.
Zum Nachweis von [[Gruppen#Existenz des inversen Elements|(i)]] sei nun $a\in U$ gegeben. Da nach obigen Überlegungen das neutrale Element $n$ von $H$ ebenfalls in $U$ liegen muss, gilt wiederum nach 2. nun $n*\overline{a}=\overline{a}\in U$.
Es bleibt zu zeigen, dass $*$ eine vernünftige Verknüpfung auf $U$ ist, die Elemente aus $U$ zu Elementen aus $U$ verknüpft. Seien dazu $a,b\in U$. Wie wir oben schon gezeigt haben, ist dann auch $\overline{b}\in U$ und wegen 2. und dem Resultat von [[Mathe Übung 3.4]] haben wir $a*\overline{(\overline{b})}=a*b\in U$
```
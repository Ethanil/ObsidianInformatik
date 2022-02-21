# Gruppen
Eine Gruppe $G$ ist eine spezielle [[Mengen|Menge]] mit einer [[Abbildung]](Verknüpfung) $*$ und folgenden Eigenschaften:

## Eigenschaften
### Assoziativität: 
$$a,b,c \in G: a*(b*c)=(a*b)*c$$
### Existenz eines neutralen Elements: 
$$\exists n\in G:\forall a\in G: n*a=a \land a*n=a$$
Es existiert auch immer nur exakt 1 neutrales Element in jeder Gruppe.
### Existenz des inversen Elements: 
$$\forall a \in G \ \exists \overline{a} \in G:\overline{a}*a=n\land a*\overline{a}=n$$
Es exisitert auch immer nur exakt 1 inverses Element für jedes Element in G.
### Kommutativität: 
Eine Gruppe heißt [[abelsch]] wenn sie folgende Eigenschaft zusätzlich besitzt:
$$\forall a,b \in G:a*b=b*a$$
### Lösbarkeit nach $x$
Wir können Gleichungen der Form von
$$a,b,c,d\in G:=a*x_1=b\land x_2*c=d$$
eindeutig nach $x$ auflösen. 
$$(x_1=\overline{a}*b;x_2=d*\overline{c})$$
### Inverse Verknüpfung
$$\forall g,h\in G:\overline{(g*h)}=\overline{h}*\overline{g}$$

## [[Untergruppen]]
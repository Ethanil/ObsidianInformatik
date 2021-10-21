# Relationen
Eine Relation beschreibt eine Teilmenge von 2 Mengen(die auch gleich sein können), für deren Tupel eine Relation("Regel") besteht.
$$R\subseteq X\times X$$
Man schreibt $xRy$ falls das Tupel $(x,y)\in R$ liegt und sagt "x steht in Relation zu y"

## Reflexiv
Eine Relation ist reflexiv, wenn 
$$xRx\text{ für jedes }x\in X\text{ gilt}$$
```ad-note
title:Anders gesagt
collapse: true
Also wenn für jedes x in der Menge die Relation zu allen x aus der selben Menge besteht
```

## Symmetrisch
Eine Relation ist symmetrisch, wenn 
$$\forall x,y\in X:xRy\Rightarrow yRx$$
```ad-note
title:Anders gesagt
collapse: true
Gilt für alle x und y in X, dass die Relation in beide Richtungen gilt.
```

## Antisymmetrisch
Eine Relation ist antisymmetrisch, wenn 
$$\forall x,y\in X:xRy:yRx\wedge x=y$$
```ad-note
title:Anders gesagt
collapse: true
Gilt die Relation nur in beide Richtungen, wenn x gleich y ist, also für keine Unterschiedlichen x und y.
```

## Transitiv
Eine Relation ist transitiv, wenn 
$$\forall x,y,z\in X:xRy\wedge yRz\Rightarrow xRz$$
```ad-note
title:Anders gesagt
collapse: true
Kann die Relation mit und ohne "Zwischenschritt" gelten, beispielsweise bei Zahlen die kleiner sind 1<2 ; 2<3 ; 1<3
```

## Äquivalenzrelation
Eine Relation ist eine Äquivalentrelation, wenn sie [[Relationen#Reflexiv|reflexiv]], [[Relationen#Symmetrisch|symmetrisch]] und [[Relationen#Transitiv|transitiv]] ist.
Wenn eine Relation eine Äquivalenzrelation ist benutzt man
$$x\sim y\text{ statt }xRy$$

## [[Ordnungsrelation]]
Eine Relation ist eine Ordnungsrelation, wenn sie [[Relationen#Reflexiv|reflexiv]], [[Relationen#Antisymmetrisch|antisymmetrisch]] und [[Relationen#Transitiv|transitiv]] ist.
Wenn eine Relation eine Ordnungsrelation ist benutzt man
$$x\le y\text{ statt }xRy$$
Gibt es auf $X$ eine Ordnungsrelation, so heißt $X$ *partiell gerodnet*
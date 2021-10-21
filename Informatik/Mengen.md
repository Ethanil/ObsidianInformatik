# Mengen
## Beispiele
- $\mathbb{N:}$Die Menge der natürlichen Zahlen
- $\mathbb{Z:}$Die Menge der ganzen Zahlen
- $\mathbb{Q:}$Die Menge der rationalen Zahlen
- $\mathbb{R:}$Die Menge der reellen Zahlen

## Mengen definieren
Bei kleinen Mengen können wir Mengen definieren, indem wir ihre Elemente einfach aufzählen:
$$M_1={0,1,2,3,4,5}$$
häufig ist es aber angenehmer eine definierende Eigenschaft für die Elemente der Menge zu schreiben, für die diese Eigenschaft wahr ist. Die Menge $M_1$ können wir also beispielsweise wie folgt definieren:
$$M_1={x\in\mathbb{N}:x\textless 6}$$
Allgemein kann man dies so schreiben:
$$M=\{x\in G:E(x)\}$$
$G$ ist die Grundmenge aus der die Elemente der Menge $M$ ausgesondert werden sollen, die die Eigenschaft $E$ haben.

## Teilmengenbeziehungen
$$N\subseteq M$$ 
Heißt N ist eine Teilmenge von M, also dass jedes Element, welches in N vorkommt auch in M vorkommt. 
$$M\supseteq N$$ 
Heißt M ist die Obermenge von N und bedeuted das selbe.
$$\emptyset$$
Ist die leere Menge, also eine Menge, die kein Element enthält
Wenn
$$N\subseteq M\wedge M\subseteq N$$
Dann gilt
$$N = M$$
## Verhältnis von Mengen untereinander
### Vereinigung
$$M\cup N$$
Bedeutet die Vereinigung von M und N, also alle Elemente die in M oder in N vorkommen
$$\{x\in G:x\in M\vee x\in N\}$$
### Schnitt
$$M\cap N$$
Bedeutet der Schnitt von M und N, also alle Elemente die in M und in N vorkommen
$$\{x\in G:x\in M\wedge x\in N\}$$
### Komplement
$$M^c$$
Bedeutet Komplement von M in G, also alle Elemente, die nicht in G vorkommen
$$\{x\in G:x\notin M\}$$
### Mengendifferenz
$$M\backslash N$$
Bedeutet die Mengendifferenz von M und N, also die Elemente die in M, aber nicht in N vorkommen
$$\{x\in M:x\notin N\}$$
### kartesisches Produkt
$$M\times N$$
Bedeutet kartesisches Produkt von M und N, also [[Tupel]] von Elementen, wobei der erste Teil des Tupels ein Element von M und der zweite Teil des Tupels ein Element von N ist.
$$\{(x,y):x\in M,y\in N\}$$
## Mengengesetze
### Kommutativgesetz
$$A\cup B=B\cup A\text{ und }A\cap B=B\cap A$$
### Assoziativgesetze
$$(A\cup B)\cup C=A\cup (B\cup C)\text{ und }(A\cap B)\cap C=A\cap(B\cap C)$$
### Distributivgesetze
$$A\cup(B\cap C) = (A\cup B)\cap(A\cup C)\text{ und }A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$$
### Regeln von De Morgan
$$(A\cup B)^c=A^c\cap B^c\text{ und }(A\cap B)^c=A^c\cup B^c$$
## Mächtigkeit von Mengen
$$|M|$$
Beschreibt die Mächtigkeit der Menge M, also wieviele Elemente M besitzt.
Mengen sind endlich, wenn sie endlich viele Elemente besitzen
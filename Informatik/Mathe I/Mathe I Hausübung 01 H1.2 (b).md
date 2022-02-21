# Mathe I Hausübung 01 H1.2 (b)
Wir betrachten zwei Ordnungsrelationene $R_1,R_2\subseteq\mathbb{N}\times\mathbb{N}$ sowie deren Durchschnitt $R:=R_1\cap R_2\subseteq\mathbb{N}\times\mathbb{N}$.
Beweisen Sie: Ist $R$ eine [[Ordnungsrelation|totale Ordnung]], so gilt $R_1=R_2$.
$$R_1=\{(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)\}$$
$$R_2=\{(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)\}$$
$$R_1\cap R_2=\{(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)\}$$
$$R_1\cap R_2=\{(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)\}$$

Durch die [[Totalität]] einer totalen Ordnung gibt es jedes [[Tupel]] entweder in der Form $(a,b)$ oder $(b,a)$.
Durch die geltende [[Antisymmetrisch|Antisymetrie]] dürfen die Elemente des Tupels nicht in "umgekehrter" Relation zueinander stehen, also nicht $a\sim b$, wenn $b\sim a$ schon gilt.
Durch die geltende [[Transitiv|Transitivität]] muss die Relation "in eine Richtung" verlaufen, also bei Zahlen beispielsweise immer größer werdend oder kleiner werdend, damit eine Relation als Ordnungsrelation gilt.
Damit die Schnittmenge von $R_1$ und $R_2$ eine totale Ordnung bilden können und gleichzeitig beide Ordnungsrelationen sind, müssen beide die Totalordnung enthalten:
$$R\subseteq R_1$$
$$R\subseteq R_2$$
Wenn wir nur weitere Tupel den Mengen $R_1$ oder $R_2$ hinzufügen würden, würden diese gegen die [[Antisymmetrisch|Antisymetrie]] verstoßen, da es keine 2 Elemente gibt, die nicht schon in eine Richtung in Relation zueinander stehen. 
Das bedeutet, dass
$$R_1\subseteq R$$
$$R_2\subseteq R$$
<center>und damit</center>

$$R_1=R$$
$$R_2=R$$
<center>und damit</center>

$$R_1=R_2$$
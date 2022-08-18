---
aliases: 
---
# Quicksort bzw Pivot Partinioning
## Abstrakt
- $m_{1}$: Ein konstanter Pointer auf eine Position in $S$.
- $m_{2}$: Ein konstanter Pointer auf eine Position in $S$.
- $i_{1}$:  Ein Pointer, der auf ein Element unter $m_{1}$ zeigt, was größer ist als $p$ oder gleich $m_{1}$ ist.
- $i_{2}$: Ein Pointer, der auf ein Element zeigt, was ungleich $p$ ist, oder gleich $m_{2}$ ist.
- $i_{3}$: Ein Pointer, der auf ein Element zeigt, was kleiner als $p$ ist, oder gleich $n+1$ ist.
- $p$: Der Pivot-Punkt.
- $S$: Die zu sortierende Liste.
- $n$: Die Länge von $S$.
### Invariante
Zuerst werden $m_{1}$ und $m_{2}$ festgelegt. Für $m_{1}$ zählen wir die Anzahl an Elementen in $S$, die kleiner sind als $p$ und ziehen eins davon ab. Für $m_{2}$ addieren wir die Anzahl der Elemente die gleich sind wie $p$ auf $m_{1}$ drauf. Insgesamt haben wir dann noch $n-m_{2}+1$ Elemente, die größer sind als $p$.
Vor und nach jeder iteration gilt:
- $1 \leq i_{1} \leq m_{1} \leq i_{2} \leq m_{2} \leq i_{3} \leq n+1$, die Pointer $i_{1}, i_{2}, i_{3}$ bewegen sich also zwischen den Grenzen von $m_{1}$ bzw der Länge von $S$
- Alle Werte in $S$, an einer Position unter $i_{1}$ sind kleiner als $p$, das Element an der Stelle $i_{1}$ ist $\geq p$, wenn $i_{1}$ kleiner ist als $m_{1}$
- Die Werte von $m_{1}$ bis unter $i_{2}$ sind gleich $p$. Das Element an der Stelle $i_{2}$ ist ungleich $p$, wenn $i_{2}$ noch kleiner als $m_{2}$ ist.
- Die Werte von $m_{2}$ bis unter $i_{3}$ sind größer als $p$. Das Element an der Stelle $i_{3}$ ist $\leq p$, wenn $i_{3}$ noch nicht am Listenende angekommen ist.
### Variante
Jede Iteration wird mindestens einer der drei "$i$"-Pointer um eins erhöht. Sie werden niemals kleiner gemacht.
### Abbruchbedingung
Wenn $i_{1} = m_{1}$,  $i_{2} = m_{2}$ und $i_{3} = n+1$
## Ablauf
- Wenn $i_{1}$ noch kleiner ist als $m_{1}$ und 
	- das Element an der Stelle $i_{1}$ gleich $p$ ist, 
		- tauschen wir dieses mit dem Element an Stelle $i_{2}$ 
		- erhöhen $i_{2}$ solange, bis es entweder gleich $m_{2}$ ist, oder wir ein Element gefunden haben was ungleich $p$ ist. 
	- Wenn das Element an der Stelle $i_{1}$ nicht gleich $p$ ist (es muss dann größer als $p$ sein!), dann 
		- tauschen wir es mit dem Element an der Stelle $i_{3}$ 
		- erhöhen danach $i_{3}$ solange bis es am Ende der Liste angekommen ist ($n+1$), oder wir ein Element gefunden haben, was nicht größer ist als $p$ (also $S[i_{3}]\leq p$).
	- Wir erhöhen in beiden Fällen $i_{1}$ solange, bis wir $m_{1}$ erreichen, oder ein Element finden, was größer oder gleich $p$ ist.
- Wenn $i_{1}$ schon gleich $m_{1}$ ist, dann 
	- tauschen wir die Elemente an Stelle $i_{2}$ und $i_{3}$ miteinander.
	- Erhöhen $i_{2}$ solange, bis wir $m_{2}$ erreichen, oder ein Element ungleich $p$ gefunden haben
	- Erhöhen $i_{3}$ solange, bis wir am Ende der Liste sind ($n+1$) oder wir ein Element gefunden haben, was nicht größer ist als $p$ (also $S[i_{3}]\leq p$).

## Komplexität


## Links
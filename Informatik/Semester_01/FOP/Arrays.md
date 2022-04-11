# Arrays
Arrays sind Listen von Referenzen, die zu [[Objekt|Objekten]] bzw [[Primitive Datentypen]] zeigen. Sie haben eine gewisse Länge, die in [[Java]] nicht veränderbar ist.
## Initialisierung
```java
Robot[] robots = new Robot[3]; //Initialisiert ein Array der Klasse Robot mit der Länge 3
robots[0] = new Robot(0, 0, RIGHT, 4); //Erzeugt an der Stelle 0 des Arrays robot ein neues Robot Objekt
robots[1] = new Robot(2, 5, DOWN, 4); /
robots[2] = new Robot(6, 2, UP, 4) ;
```
## Indizes
Die einzelnen Elemente eines Arrays können mithilfe eines Indize angesprochen werden. In Java fangen die Indizes immer bei 0 an und hören bei `Array.length-1` auf.
## Handhabung
Das Handling von Arrays funktioniert genau gleich wie bei [[Variable|Variablen]].
```java
robots[0].putCoin();
robots[0].move();
robots[1].putCoin();
robots[1].move();
robots[2].putCoin();
robots[2].move();
```
Das Schöne an arrays ist, dass wir durch eine [[For-Schleife]] einfach alle Elemente des Arrays nacheinander ansprechen können. Dabei benutzen wir die Länge des Arrays als Schleifenbedingung:
```java
for(int i 0; i<robots.length;i++){
	robots[i].putCoin();
	robots[i].move();
}
```
Die beiden Code-snippets führen die selben Anweisungen aus.
Wenn wir allerdings bspw. die Länge des Arrays ändern, funktioniert der untere Code immer noch für alle Robots, der obere müsste allerdings jedes mal um 2 weitere Zeilen angepasst werden.
### [[For-Schleife#for-each-Schleife|For-each-Schleife]]
### Fallstricke
#### Unmögliche Indizes
Wir müssen bei der Verwendung von Arrays darauf achten, dass wir weder negative, noch zu große Arrays ansprechen.
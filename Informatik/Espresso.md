---
aliases: 
---
# Espresso
Espresso ist ein heuristischer Algorithmus zur [[Algorithmische Logikminimierung|Logikminimierung]].
## Aufbau einer Espresso-Datei:
```Java
.i		2	//Anzahl Eingänge
.i		1	//Anzahl Ausgänge
.lbb	A B	//Namen der Eingänge (optional)
.ob		Y	//Namen der Ausgänge (optional)
//Logik in Form von
//Eingänge Ausgang:
00 0		//0-er Ausgänge sind optional
01 1		//~A&B=1
10 1		//A&~B=1
11 0		//dieser hier also Auch
.e			//Ende (optional)
```
## Don't Cares
Wir können sowohl bei den Eingängen, als auch bei den Ausgängen don't Cares (`-`) benutzen.
## Ausgabedatei lesen
Wir erhalten eine Ausgabedatei die zum Beispiel wie folgt aussieht:
```
.i 4
.o 3
.p 8
11-- 110
1-10 110
0-11 010
-110 100
01-1 011
1000 101
10-1 001
-001 001
.e
```
Wir schauen nun bei welchen Aussagen auf der linken Seite eine bestimmte Variable 1 ist.
Wenn wir die Ausgänge $S_0-S_2$ von links nach rechts nennen und die Eingänge $A,B,C,D$, dann gilt für $S_0$ also:
$S_0=AB+AC\overline{D}+BC\overline{D}+A\overline{B}\overline{C}\overline{D}$
## Weitere Einsatzmöglichkeiten
[[Mehrwertige Logik]]
[[Zustandsautomaten]]
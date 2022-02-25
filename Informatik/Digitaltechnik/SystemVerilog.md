---
aliases: 
---
# SystemVerilog
SystemVerilog hat keine [[Methode|Methoden]] oder Funktionen, sondern Module. In den Modulen wird beschrieben wie eine Aufgabe durchgeführt wird. Jedes Modul hat Eingänge, Ausgänge und eventuell Parameter.
## Für [[Kombinatorische Logik]]
Für [[Kombinatorische Logik]] reicht es der Output-Variable einen Booleschen Ausdruck zuzuweisen.
```ad-example 
collapse:true
```SystemVerilog
module example(input logic a,b,c, output logic y);
	assign y=~a & ~b & ~c | a & ~b & ~c | a & ~b & c;
endmodule
```
Hierbei ist `assign` eine (kombinatorische) Signalzuweisung
## Modulhierarchie
Wie in normalen Programmiersprachen wie [[Java]] auch kann man in SystemVerilog Module in anderen Modulen verwenden um übersichtlicher zu arbeiten (und das [[Kombinatorische Logik#Blackbox-Eigenschaften|Blackbox]]-Prinzip zu wahren). So kann ein 3-Input [[Konjunktion(und)|And-Gate]] zusammen mit einem [[Negation(nicht)|Negation-Gate]] verwendet werden um ein [[NAND|3-Input Nand Gate]] zu erstellen.
## Operatoren
### Bitweise
```ad-note
collapse:true
```SystemVerilog
&		//AND
|       //OR
^		//XOR
~(a&b)	//NAND
~(a|b)	//NOR
```
### Reduktionsoperator (unär)
Wenn wir einen Vektor haben, bei dem wir alle einzelnen Elemente mit einem der Bitweise-verknüpfenden Operatoren verknüpfen wollen können wir dies auch machen.
```ad-example
collapse:true
```SystemVerilog
assign y=&a;
```
### Bedingte Zuweisung (ternär)
Wenn man eine Bedingte Zuweisung verwenden möchte, tut man das wie in [[Java]]
```ad-example
collapse:true
```SystemVerilog
y= s ? a : b;
```
### Präzedenz
```ad-note
collapse:true
![[Pasted image 20220225113533.png]]
```
## Syntax für numerishce Literale
Um Zahlen darzustellen verwenden wir folgende Syntax
```SystemVerilog
<N>'<B><wert>
```
- `N` =  Bitbreite
- `B` = Basis (d,b,o,h)
- `wert` = Wert
Werte werden zur Bitbreite mit 0en aufgefüllt.
`N` und `B` sind optional, default ist `32'd`, also eine 32 bit breite dezimalzahl.
## Verzögerungen
Nachdem wir die Zeiteinheit und Präzision für die Rundung (`timescale`) festgelegt haben, können wir `#X` verwenden um jeweils `X` Zeiteinheiten zu warten
```ad-example
collapse:true
```SystemVerilog
`timescale 1ns / 10 ps	//jede Zeiteinheit ist 1 ns lang und wird auf 10ps gerundet.
module example_delay(input logic a,b,c, output logic y);
	logic ab,bb,cb,n1,n2,n3;
	assign #1 {ab,bb,cb} = ~{a,b,c};
	assign #2 n1 = ab & bb & cb;
	assign #2 n2 = a &bb & cb;
	assign #2 n3 ? a & bb & c;
	assign #4 y = n1 | n2 | n3 ;
```
## Datentypen
- bit: zweiwertig -> 0 , 1
- logic: vierwertig -> 0 , 1 , x , z
- int: bit signed \[31:0] -> $[-2^{31},2^{31}-1]$
- integer: logic signed ->  $[-2^{31},2^{31}-1]$
	- wenn wir logic verwenden, sollten wir auch integer verwenden
- enum: Aufzählung symbolischer Werte
- time, real, typedef, sturct, ...
- Vektoren und Arrays
	- Vektoren sind mehrere bit Breite Variablen bei denen man etwas auf alle Elemente gleichzeitig anwenden kann (Siehe[[SystemVerilog#Reduktionsoperator unär|hier]]), wohingegen Arrays sich verhalten wie [[Arrays]] in bspw [[Java]]
## sequentielle Logik
## parametrisierte Module
## Testumgebungen
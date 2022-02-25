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
### Reduktionsoperator
Wenn wir einen Vektor haben, bei dem wir alle einzelnen Elemente mit einem der Bitweise-verknüpfenden Operatoren verknüpfen wollen können wir dies auch machen.
```ad-example
collapse:true
```SystemVerilog
assign y=&a;
```

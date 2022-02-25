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
Wie in normalen Programmiersprachen wie [[Java]] auch kann man in SystemVerilo
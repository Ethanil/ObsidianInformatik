---
aliases: 
---
# Bluespec 
## interface
In einem Interface beschreiben wir die Schnittstelle nach außen, welche dann mittels eines `moduls` implementiert wird. bpsw
```Bluespec
interface Mult_ifc;
	method Action                   put_x(int xx);
	method Action                   put_y(int yy);
	method ActionValue   #(int)     get_w();
endinterface: Mult_ifc
```
Hierbei werden 3 methoden beschrieben, mit denen wir mit dem Modul dann interagieren können, 2 `Action` methods, bei denen ein Wert übergeben wird und es keinen Rückgabewert gibt und eine `ActionValue` Methode bei der ein `int` zurückgegeben wird.

## module
Ein Modul beschreibt quasi die "Klasse" die wir beschreiben, sie heißen `mk...` bspw. `mkMult` für einen Multiplizierer.
Jedes Modul beschreibt immer ein `interface`. Am Anfang des Moduls beschreiben wir zuerst die Register, also unsere Variablen. bspw:
```bluespec
module mkMult (Mult_ifc);
	Reg #(int)     w         <- mkRegU;
	Reg #(int)     x         <- mkRegU;
	Reg #(int)     y         <- mkRegU;
	Reg #(Bool)    got_x     <- mkReg (False);
	Reg #(Bool)    got_y     <- mkReg ();
	



## Li
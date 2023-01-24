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
	Reg #(Bool)    got_y     <- mkReg (False);
```
Hierbei werden 5 Variablen deklariert, die ersten 3 bleiben uninitialisiert (`mkRegU`) und 2 werden mit `False` initialisiert (`mkReg (False)`)

## Arten von Methoden
### Wert-Methoden
Value Methods sind äquivalent zu mathematischen Funktionen, können also den Zustand der Schaltung nicht ändern sondern nur lokale Zwischenwerte via `=` berechnen. Das heißt `<=` oder `<-` ist hier **verboten**. Sie haben einen Rückgabewert. (zum Beispiel um die Summe aller Werte zu berechnen)
### Aktions-Methoden
Action Methods dürfen den Zustand der Schaltung ändern, haben aber keinen Rückgabewert
### Aktionswert Methoden
Action Value Methods können den Zustand der Schaltung ändern und haben einen Rückgabewert an Aufrufer.

## Links
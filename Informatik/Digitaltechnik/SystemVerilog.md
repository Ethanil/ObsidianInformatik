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
## Syntax für numerische Literale
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
### always-Blöcke
`always`-Blöcke führen ihre Instruktionen (meist mit `begin ... end` zusammengefasst) endlos aus. Alle `always`-Blöcke werden parallel ausgeführt, wobei Verzögerungen nur die Ausführung des *umgebenen* `always`-Blockes verzögert. 
#### Warten auf Ereignisse
Mithilfe von `@` nach dem `always` wartet der Block auf eine Änderung des nach dem `@` folgenden kombinatorischen Ausdrucks(Kommata können verwendet werden um auf mehrere Ausdrücke zu "horchen"). Auch `posedge` und  `negedge` können nach dem `@` verwendet werden um auf eine steigende bzw. fallende Flanke zu warten.
```ad-example
collapse:true
![[Pasted image 20220225124610.png]]
```
####  Zuweisungssequenzen
##### blockierende Zuweisungen
Das normale `=` blockiert die Ausführung des Blockes, das heißt die Zuweisung wird vollständig ausgeführt bevor die nächste Zuweisung behandelt wird, sie werden also in gegebener Reihenfolge (sequentiell) abgehandelt
##### nicht-blockierende Zuweisungen
`<=` Anweisungen werden ausgewertet, aber noch nicht zugewiesen, sondern nur vorgemerkt und werden erst beim Fortschreiten der Systemzeit (`#` oder `@`) zugewiesen, sie werden also parallel abgehandelt.
```ad-example
collapse:true
![[Pasted image 20220225125017.png]]
```
### initial
`initial` enstpricht `always begin <instruction> @(0); end` und kann für die Initialisierung in der Simulation verwendet werden
### always_comb
Der `always_comb` Block wird ausgeführt nachdem alle `initial` und  `always` Blöcke gestartet sind und immer wenn sich einer der Werte ändert.
In einem `always_comb` Block können wir  `case` Statements benutzen, die wie switch-case in [[Java]] funktionieren.
```ad-example
collapse:true
![[Pasted image 20220225122944.png]]
```
Wenn wir [[Don't Care|Don't Cares]] verwenden möchten, nehmen wir `casez` anstatt `case`.
### always_latch und always_ff
`always_latch` ist äquivalent zu einem [[D-Latch]] und `always_ff` zu einem [[D-Flip-Flop]]. In diesen Blöcken sollten keine blockierenden Zuweisung verwendet werden!

```ad-example
collapse:true
![[Pasted image 20220225130549.png]]
```
Wir können `always_ff` asynchron oder synchron zurücksetzbar machen, indem wir entweder das $reset$ Signal in den `@` Teil schreiben(asynchron) oder innerhalb des Blockes eine if-Bedinung mit dem $reset$ Signal benutzen(synchron). Mit dem gleichen System wie für das synchrone rücksetzen können wir ein [[Flip-Flop mit Taktfreigabe]] erstellen, welcher in der else-Bedingung das $enable$ Signal als Bedinung beinhaltet.
## parametrisierte Module
Neben Ein- und Ausgaben kann die Modulschnittstelle auch parameter definieren, die dann bei der Instanziierung durch konkrete Werte ersetzt werden, die während der Laufzeit nicht änderbar sind, vergleichbar mit [[Generics]]. Typischerweise werden dabei die Port-Breite oder Speichertiefe festgelegt.
```ad-example
collapse:true
```SystemVerilog
module muix2xW
   #(parameter WIDTH=8)
	(input logic [WIDTH-1:0] A,B,
	 input logic S,
	 output logic [WIDTH-1:0]Y);
		assign Y= S ? A : B;
endmodule
```
## Testumgebungen
Eine Testumgebung oder testbench ist ein [[Hardwarebeschreibungssprachen|HDL]]-Programm zum Testen eines andere [[Hardwarebeschreibungssprachen|HDL]]-Moduls. Dies ist im [[Hardware]]-Entwurf schon lange üblich und erst seit einigen Jahren auch im [[Software]]-Bereich eingesetzt bspw [[JUnit]]-Tests.
Das getestete Modul wird dabei Device under test(DUT) oder Unit under test(UUT) genannt.
Logischerweise werden die Tests nicht synthetisiert sondern nur für die Simulation benutzt.
Allgemein kann man 3 Arten von Testrahmen festlegen: einfach (bei dem man die Ausgaben händisch prüfen muss), selbstprüfend (bei dem die Ausgaben auf Korrektheit überprüft werden) und selbstprüfend mit Testvektoren (bei dem es variable Testdaten gibt die bspw aus einer Datei gelesen werden).
### typischer Test
- Modul ohne Ports
- Stimuli erzeugen (Takt, Reset, Eingabedaten)
- UUT instantiieren
- Ausgabedaten und Timing verifizieren
- wird nicht synthetisiert
```ad-example
collapse:true
![[Pasted image 20220225133148.png]]
```
### Ausgabe von Statusmeldungen
Zur Ausgabe von Meldungen benutzen wir `$display(<format>,<values>*);`. In der Nachricht können wir Platzhalter verwenden, die dann aufgefüllt werden
- `%d, %b, %h` für dezimal-, binär- oder hexadezimalzahlen
- `%m` für einen Modulnamen
- `%t` für Zeit
Ein Zeitformat kann mit `$timeformat(-9,1,"ns",8);` erstellt werden, was eine Skalierung auf $10^{-9}$, 1 Nachkommastelle, den Suffix(hier "ns") und die Anzahl der anzuzeigenden Zeichen(hier 8) heißt.
## Zustandsautomaten

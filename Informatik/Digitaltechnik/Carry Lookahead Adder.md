---
aliases: 
---
# Carry Lookahead Adder
Für den Carry Lookahead Adder machen wir für den Übertrag eine Fallunterscheidung:
$A_i,B_i$ sind die zu addierenden Werte, $C_i$ der Übertrag des zu betrachtenden Moduls
- Wenn $A_i$ und $B_i$ 1 sind, dann haben wir auf jedenfall einen Übertrag (Generate)
- Wenn $A_i$ oder $B_i$ 1 sind, dann haben wir einen Übertrag, wenn $C_{i-1}$ 1 ist (Propagate)
- Wenn $A_i$ und $B_i$ 0 sind, dann haben wir auf keinen Fall einen Übertrag
-> $C_i=A_i\cdot B_i+(A_i+B_i)\cdot C_{i-1}$
## Der Vorteil
Das an sich würde noch gar nichts bringen, da der Weg für den Übertrag exakt gleich wie bei einem [[Ripple-Carry-Adder]] wäre, wenn wir allerdings unsere Zahl in Spalten aufteilen und dann $k>1$ Spalten gleichzeitig berechnen.
Dadurch können wir den Übertrag $k$ Spalten nach vorne springen lassen, da der großteil der Berechnung nicht mehr vom Übertrag selbst abhängig ist, sondern von den Inputs
-> Wir können vorrechnen um, sobald wir den vorherigen Übertrag erhalten haben den nächsten zu berechnen.
### Beispiel für $k=4$
Jeder Block aus 4 Spalten erzeugt einen Übertrag, wenn entweder:
- die höchstwertige Spalte(3) einen übertrag generiert
- die höchstwertige Spalte propagiert und die 2. Spalte generiert
- die 3. und 2. Spalte propagiert und die 1. Spalte generiert
- die 3.-1. Spalte propagiert und die 0. Spalte generiert
#### VS [[Ripple-Carry-Adder]]
Ein RCA, der 8 Bits addieren soll, benötigt $8\cdot (t_{pd,AND}+t_{pd,OR})$, wobei ein CLA nur $4\cdot (t_{pd,AND}+t_{pd,OR})+1\cdot (t_{pd,AND}+t_{pd,OR})=5\cdot  (t_{pd,AND}+t_{pd,OR})$
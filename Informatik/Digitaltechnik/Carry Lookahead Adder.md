---
aliases: 
---
# Carry Lookahead Adder
Für den Carry Lookahead Adder machen wir für den Übertrag eine Fallunterscheidung:
$A_i,B_i$ sind die zu addierenden Werte, $C_i$ der Übertrag des zu betrachtenden Moduls
- Wenn $A_i$ und $B_i$ 1 sind, dann haben wir auf jedenfall einen Übertrag
- Wenn $A_i$ oder $B_i$ 1 sind, dann haben wir einen Übertrag, wenn $C_{i-1}$ 1 ist
- Wenn $A_i$ und $B_i$ 0 sind, dann haben wir auf keinen Fall einen Übertrag
-> $C_i=A_i\cdot B_i+(A_i+B_i)\cdot C_{i-1}$
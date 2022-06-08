# Ausdruckauswertung und effiziente Register-Allokation
## Extraktion eines Ausdrucks aus C Quelltext
```C
1 #include <stdio.h>  
2  
3 int main() {  
4   int a, b, c, d, e, f;  
5   int g = a & b;  
6   int h = g ^ ~c * d;  
7   int i = h - (e | f);  
8  
9   printf("%d\n", i);  
10  return 0;
11 }
```
```C
i=((a & b) ^ ~c * d) - (e | f)
```
## Baumdarstellung arithmetischer Ausdrücke und die Ershov-Zahl
![[Praxistestat 01 08.06.2022 15-02-28.excalidraw]]

- Den Blattknoten `a`, `b`, `c`, `d`, `e`, `f` wird jeweils der Wert **1** zugewiesen.
- Da der Knoten `~` nur ein Kind hat, hat er denselben Wert wie sein Kind. `~` wird also **1** zugewiesen.
- Da die Kinder der Knoten `*`, `&` und `|` jeweils denselben Wert haben (1), wird den Knoten selbst der Wert eines beliebigen Kindes + 1 zugewiesen.  `*`, `&` und `|` wird also jeweils **2** zugewiesen.
- Da die Kinder des Knotens `^` jeweils denselben Wert haben (2), wird dem Knoten selbst der Wert eines  beliebigen Kindes + 1 zugewiesen. `^` wird also **3** zugewiesen.
- Da die Kinder des Knotens `-` unterschiedliche Werte haben (2,3), wird dem Knoten selbst der höhere der Beiden zugeordnet. `-` wird also **3** zugewiesen.
- Da `-` der Wurzelknoten des Baumes ist, terminiert der Algorithmus und die Ershov-Zahl für den  gegebenen Baum bzw. Ausdruck lautet **3**.

```assembly
.data
mystring: .asciz "%d \n"
a: .word 1337
b: .word 69
c: .word 420
d: .word 42
e: .word 11
f: .word 41
.text
.global main
main:
	ldr r0, =a
	ldr r1, =b
	AND r0, r0, r1
	ldr r1, =c
	MVN r1, r1
	
```

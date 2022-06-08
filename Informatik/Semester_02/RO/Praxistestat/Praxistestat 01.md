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
mystring: .asciz "%d \n"     //Output string
a: .word 1337                //variable a
b: .word 69                  //variable b
c: .word 420                 //variable c
d: .word 42                  //variable d
e: .word 11                  //variable e
f: .word 41                  //variable f
.text
.global main
main:
	push {lr}                //save return adress
	ldr r0, =c               //load c into r0
	MVN r2, r0               //negate r0 and save into r2: ~ c
	ldr r1, =d               //load d into r1
	MUL r0, r2, r1           //multiply r1 and r2 and save into r1: ~ c * d
	ldr r1, =a               //load a into r1
	ldr r2, =b               //load b into r2
	AND r1, r1, r2           //use AND with r1 and r2 and save into r1: a & b
	EOR r0, r0, r1           //use exclusive or with r0 and r1 and save into r0: ~ c * d ^ (a & b)
	ldr r1, =e               //load e into r1
	ldr r2, =f               //load f into r2
	ORR r1, r1, r2           //use or with r1 and r2 and save into r1: e | f
	SUB r1, r0, r1           //subtract r1 from r0 and save into r1 (~c * d ^ (a & b)) - (e | f)
	ldr r0, =mystring
	bl printf                //calls printf
	pop {lr}                 //get return adress back
	bx lr                    //return or exit
```

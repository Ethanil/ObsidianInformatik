---
aliases: 
---
# Pointer und Arrays 
Ein Pointer zeigt auf eine Variable und hat den Typ `<Variablentyp>*`, wobei das Sternchen das ganze zum Pointer macht. Um einen Pointer zu einer Variable zu erzeugen verwenden wir `&`

```C
int a = 4;
int *p = &a;
```
Wir haben nun also einen `int` a, welcher den Wert 4 hat und den `int*`-Pointer p, welcher auf die Variable a zeigt.
Um den Wert der Variable eines Pointers zu ändern, verwenden wir ein Sternchen vor dem Pointer:
```C
int a = 4;
int *p = &a;
*p = 42;
```
Am Ende dieses Codes hat a also den Wert 42.
## Links
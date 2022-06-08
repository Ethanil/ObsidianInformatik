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
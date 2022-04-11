# double
Double ist ein gebrochenzahliger, [[Primitive Datentypen|primitiver Datentyp]] 
## Bereich
Maximalwerte:
>±1.797...\*10³⁰⁸

### Konstanten
Bei den gebrochenen Datentypen steht der MIN_VALUE und MAX_VALUE für etwas anderes als bei den [[Primitive Datentypen#Ganze Zahlen|ganzzahligen Datentypen]]. Der MAX_VALUE ist äquivalent, allerdings ist der MIN_VALUE die kleinste, positive, darstellbare Zahl.
```java
Double.MAX_VALUE
und
Double.MIN_VALUE
```
erhalten
Einen symbolischen Unendlichwert können wir mithilfe von
```java
Double.POSITIVE_INFINITY
und
Double.NEGATIVE_INFINITY
```
erhalten
#### Ergebnis Division 0.0 durch 0.0
Bei der Division von `0.0` durch `0.0` erhalten wir Double.NaN (Not a Number).
## Genauigkeit
Float ist 1 zu 4,5 Billiarde genau.
Dies ist sehr viel genauer als ein [[float]]
## Literale
Beispiele
```java
double d1 = 12.34
double d2 = .1234
double d3 = 1.2E34		| Dies entsprricht 1,2*10³⁴
```
Wie alle anderen Literale werden diese auch Variablen [[Operatoren#Zuweisungen|zugewiesen]].
# float
Float ist ein gebrochenzahliger, [[Primitive Datentypen|primitiver Datentyp]] 
## Bereich
Maximalwerte:
>±3.402...\*10³⁸

### Konstanten
Bei den gebrochenen Datentypen steht der MIN_VALUE und MAX_VALUE für etwas anderes als bei den [[Primitive Datentypen#Ganze Zahlen|ganzzahligen Datentypen]]. Der MAX_VALUE ist äquivalent, allerdings ist der MIN_VALUE die kleinste, positive, darstellbare Zahl.
```java
Float.MAX_VALUE
und
Float.MIN_VALUE
```
erhalten
Einen symbolischen Unendlichwert können wir mithilfe von
```java
Float.POSITIVE_INFINITY
und
Float.NEGATIVE_INFINITY
```
erhalten
#### Ergebnis Division 0.0 durch 0.0
Bei der Division von `0.0` durch `0.0` erhalten wir Float.NaN (Not a Number).
## Genauigkeit
Float ist 1 zu 8,388,608 genau.
Anders ausgedrückt könnte man sagen, dass die Zahlen 1- 8,388,608 genau dargestellt werden können, wir uns ab 8,388,609 aber nicht mehr sicher sein können, mit welcher Zahl wir genau rechnen.
Das klingt nicht nach viel, aber nach vielen Rechenoperationen akkumuliert diese Ungenauigkeit.
[[double]] ist sehr viel genauer als float!
## Literale
Beispiele
```java
float f1 = 12.34
float f2 = .1234
float f3 = 1.2E34		| Dies entsprricht 1,2*10³⁴
```
Wie alle anderen Literale werden diese auch Variablen [[Operatoren#Zuweisungen|zugewiesen]].
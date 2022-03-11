# [[Mathe I]] Treffpunkt 01
## Aussagen
Aussagen sind formalisierte Sätze, die wahr oder falsch sind.
```ad-example
collapse:true
$5>3$
Wenn es regnet, ist die Straße nass
```
## Quantoren
### [[Allquantor]]
### [[Existenzquantor]]
### modifizierter Existenzquantor
$\exists!x\in X$ bedeutet, dass es genau 1 $x$ in $X$ gibt, für die diese Aussage wahr ist.
## Übung 1
$D:=(\neg A\leftrightarrow B)\wedge(\neg A\wedge C)$

| $A$ | $\neg A$ | $B$ | $C$ | $\neg A\wedge C$ | $\neg A\leftrightarrow B$ | $D$ |
| --- | -------- | --- | --- | ---------------- | ------------------------- | ------ |
| f   | f        | w   | w   | f                | f                         |  f      |
| w   | f        | w   | f   | f                | f                         |   f     |
| w   | f        | f   | w   | f                | w                         |    f    |
| w   | f        | f   | f   | f                | w                         |     f   |
| f   | w        | w   | w   | w                | w                         |      w  |
| f   | w        | w   | f   | f                | w                         |       f |
| f   | w        | f   | w   | w                | f                         |        f|
| f   | w        | f   | f   | f                | f                         |        f|

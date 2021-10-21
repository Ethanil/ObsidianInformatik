# Arithmetische Ergebnistypen
Bei [[Operatoren#Arithmetische Operationen]] mit den [[Primitive Datentypen]] erhalten wir unterschiedliche Ergebnistypen:
## Ergebnistyp int
Wir erhalten immer den Datentyp [[integer]] wenn wir mit folgenden Datentypen rechnen:
- [[byte]]
- [[char]]
- [[short]]
- [[integer|int]]

## Ergebnistyp long
Wir erhalten immer den Datentyp [[long]], sobald wir einen der vorherigen Datentypen mit einem long verknüpfen.

## Ergebnistyp float
Wir erhalten immer den Datentyp [[float]], sobald wir einen der vorherigen Datentypen mit einem float verknüpfen.

## Ergebnistyp double
Wir erhalten immer den Datentyp [[double]], sobald wir irgendeinen der Datentypen mit einem double verknüpfen.

## "Wertigkeitstabelle"
|Ursprungstyp|Minimales Ergebnis|
|---|---|
|[[byte]]|[[integer]]
|[[char]]|[[integer]]
|[[short]]|[[integer]]
|[[integer]]|[[integer]]
|[[long]]|[[long]]
|[[float]]|[[float]]
|[[double]]|[[double]]
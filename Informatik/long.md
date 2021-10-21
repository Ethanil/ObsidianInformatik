# long
Long ist ein ganzzahliger, [[Primitive Datentypen|primitiver Datentyp]] 
## Bereich
Kleinster möglicher Wert der in einem long gespeichert werden kann:
>-9,223,372,036,854,775,808

Größter möglicher Wert, der in einem long gespeichert werden kann:
>+9,223,372,036,854,775,807
### Konstanten
Die maximal- und minimalwerte des Bereiches kann man als Konstante mithilfe von
```java
Long.MAX_VALUE
und
Long.MIN_VALUE
```
erhalten
## Literale
Long haben ein eigenes Literal, welches benutzt wird um Werte die in ihrem Bereich fallen der Variable [[Operatoren#Zuweisungen|zuzuweisen]].
```java
long l = 123L
```
> Es ist möglich anstatt dem großen `L` auch ein kleingeschriebenes `l` zu nehmen, dies kann man aber einfach mit einer `1` verwechseln 

Dies ist wichtig bei Zahlenwerten, die außerhalb des Bereiches von integern liegen können

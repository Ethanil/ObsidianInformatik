# Konversionen
## implizite Konversionen
Bei impliziten Konversionen wird ein Wert in eine Variable von "höherer" Stufe gespeichert
```java
byte b = 12
int i = b
```
Bei impliziten Konversionen kommt es meistens[^1] zu keinem Datenverlust
## explizite Konversionen
>Gefährliche Konversionen

Bei expliziten Konversionen wird ein Wert in eine Variable von "niedriger" Stufe gespeichert
```java
int i = 12
byte b = (byte)i
```
Dabei ist es möglich, dass es zu keinem Datenverlust kommt, aber die gefahr bestet:
```java
int i = 12345
byte b = (byte)i	|der Variable b ist nun der Wert 57 zugewiesen, nicht 12345
```

[^1]: Bei der Konversion von int zu float, long zu float und long zu double kann es zu minmalen Abweichungen kommen
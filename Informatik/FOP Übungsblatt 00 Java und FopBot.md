# Übungsblatt 00 von [[FOP]]:
![[uebung00.pdf]]
## Passende Videos:
- [Video](https://www.youtube.com/watch?v=uQPV1q8VwPQ&list=PLM5vsAQgDiIvZtAPsxhzTq0u62ZIKfY1u&index=4)

## Die leere World 
`Robot myRobot = new Robot(3,1,UP,0);`
-> Erschafft einen [[FopBot]] auf dem vierten Feld von links und dem zweiten Feld von unten

## Mögliche "Befehle" für den Roboter 
- `myRobot.move();`
- `myRobot.turnLeft();`
- `myRobot.putCoin();`
- etc
## kurzes Intermezzo 
### Programme und Prozesse
- Ein [[Programm]] ist ein [[Quellcode]] und der übersetzte [[Code]]
- Quelltext ist beispielsweise das unter [[FOP Übungsblatt 00 Java und FopBot#Mögliche Befehle für den Roboter]] geschriebene
- [[Java]] Quelltext wird ind Java Bytecode übersetzt
- Die Ausführung des übersetzten Programms nennt man Prozess
	- Mehrere Prozesse können zeitgleich vom selben Programm ausgeführt werden
	- das ist möglich durch mehrere Prozessorkerne
## Vorwärtsschritte in Schleifen 
>Siehe [[For-Schleife]]

>Siehe [[While-Schleife]]
## [[Operatoren ]]

## [[Schlüsselwörter]]
- das sind reservierte Wörter, die man nur in diesem reservierten Zusammenhang benutzten darf und kann. Beispiele sind:
	- [[For-Schleife]]
	- [[While-Schleife]]
	- [[new]]
	- [[integer|int]]
## [[Identifier]] (Bezeichner)
Namen von
- [[Klasse|Klassen]] wie Robot
- [[Variable|Variablen]] wie MyRobot, myRobot2, ari und i
- [[Methode|Methoden]] wie move, turnLeft und hasAnyCoins
Diese dürfen nur aus folgendem bestehen:
- a-z
- A-Z
- 0-9
- "\_" und "$"
- **BEACHTE**: Das erste Zeichen darf keine Ziffer sein!
- **BEACHTE**: nicht verwendbar sind, wie in [[FOP Übungsblatt 00 Java und FopBot#Schlüsselwörter]] schon gesagt, diese Begriffe und
	- false
	- true
	- null
- Wir benutzen [[camelCase]] für
	- Variablen
	- [[Attribut|Attribute]]
	- [[Parameter]]
	- Methoden
- Wir benutzen [[PascalCase]] für
	- Klassen

## Kommentare
Mögliche Kommentierungen sind:
```java
// Eine einzeiliges Kommentar

/*Ein mehrzeiliges Kommentar
das geht hier weiter
*/

/**
* So kann man auch Kommentare schreiben um sie schön zu formatieren
* Das geht natürlich auch über mehrere Zeilen
*/
```

## Whitespace
Leerer Quelltext für die bessere Übersicht oder sogar für die Funktion notwendig.
Beispiele:
- Leerzeichen (blank) - mittels Space
- Zeilenumbruch (newline) - mittels Enter
- Tabulator (tab) - mittels Tab
- 
Notwendig ist es zwischen
- Zwei Schlüsselwörtern
- Zwei Identifiern
- Schlüsselwort und Identifier
- 
beliebig viele *zwischen* lexikalischen Elementen
keine *innerhalb* eines lexikalischen Elements
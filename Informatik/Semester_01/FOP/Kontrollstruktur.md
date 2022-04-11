# Kontrollstruktur
>Oberbegriff für Verzweigungen, Schleifen und in anderen Sprachen auch  Sprunganweisungen. Kontrollstrukturen erlauben es, aus einer oder mehrere Anweisungen eine komplexere Anweisung zu bilden. Aus diesen können durch Kontrollstrukturen wieder komplexere Anweisungen gebildet („ineinandergeschachtelt“) werden usw. (01a:110-163, 03c:223-235)
- [[For-Schleife]]
- [[While-Schleife]]
- [[Verzweigungen]]

## geschweifte Klammern
geschweifte Klammern sind bei Rümpfen die größer sind als eine Zeile notwendig, können aber auch bei einzeiligen Rümpfen verwendet werden

## Vereinfachungen
Alle Kontrollstrukturen können in einem Fluss-Diagramm in einer einzellnen Anweisung dargestellt werden, die die Abstraktere Funktion abbilden
>"Lege 5 Münzen in einer geraden Linie aus"
```java
Robot myRobot = new Robot(0,0,UP,5);
for(int i=0;i<5;i++){
	myRobot.putCoin();
	myRobot.move();
}
```
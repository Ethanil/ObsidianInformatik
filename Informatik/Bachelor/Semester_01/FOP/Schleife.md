# Schleifen
Schleifen sind [[Kontrollstruktur|Kontrollstrukturen]], die im [[Quellcode]] festlegen, dass ein definierter Schleifenrumpf X-Fach ausgeführt wird.
Wie oft die Schleife ausgeführt wird ist abhängig von der Art der Schleife und der Schleifenbedingung.
In Java gibt es 3 Arten von Schleifen
- [[For-Schleife|For-Schleifen]]
- [[While-Schleife|While-Schleifen]]
- [[While-Schleife#Do-While-Schleife|Do-While-Schleifen]]

## Invariante, Variante und Konsequenz
### Invariante
Eine Invariante ist eine Aussage, die am Anfang und am Ende eines jeden Schleifendurchlaufs und vor und nach der Ausführung der Schleife gültig ist.
Während der Schleife muss die Invariante **NICHT** gültig sein
```java
//Schleifeninvariante lautet a * b = (x * y) + result
public int multiplication(int a, int b){
	int x = a;
	int y = b;
	int result = 0;
	//Hier muss die Invariante gültig sein
	while(x>0){
		//Die Invariante muss auch am Anfang der Schleife gültig sein
		result += y;
		//Hier kann die Invariante ungültig sein(Ist sie auch!)
		x--;
		//Am Ende der Schleife muss die Invariante wieder gültig sein
	}
	//Nach Durchlaufen der Schleife muss die Invariante gültig sein
	return result;
}
```
### Variante
Eine Variante beschreibt die Veränderung innerhalb einer Schleife, also im obigen Beispiel das "umschichten" von einem y von der Multiplikation auf die Addition (damit `( x \* y) + result = a \* b` gültig bleibt)
Anders gesagt ist die Variante der Fortschritt unserer Schleife, bei einer einfachen [[For-Schleife#Zähl-Schleife]] ist dies der dritte Teil der Kontrollstruktur `for(_; _; X)`, also das X
### Konsequenz
Die Konsequenz beschreibt das Ergebnis der Schleife, also dass `result` am Ende der Schleife das Ergebnis der Multiplikation enthält.
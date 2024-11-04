---
aliases: 
---
# String Matching basierend auf endlichem Automaten 
## Abstrakt
- T: Den String den wir suchen
- m: die Länge von T
- S: Der String in dem wir suchen
- n: die Länge von S
- $\Sigma$: Das Alphabet aus dem T und S gebildet sind
- R: Liste der Start-Indizes von gefundenen Strings (T in S)
- I: Liste der möglichen Kandidaten, bevor sie in R geschrieben werden
- q: die aktuell maximale prefix Länge
- Wir brauchen noch eine Look-Up Tabelle (der Automat) mit dem wir gültige Kandidaten finden.
### Invariante
Nach $i \geq 0$ Iterationen:
R beinhaltet alle Start-Indizes von T's in S in aufsteigender Ordnung.
q ist die Länge des längsten aktuellen Kandidatens (Beispiel: T= gagaga S=gagagaganb i= 4, dann wäre q 4, da der längste Kandidat, aktuell **gaga**gaganb ist, obwohl ga**ga**gaganb auch ein Kandidat ist und nur 2 lang ist.)
### Variante
i wird um 1 erhöht
### Abbruchbedingung
n Iterationen abgeschlossen.
### Input
zwei Strings über einem Beliebigen Alphabet
### Output
die aufsteigend sortierte Menge aller Vorkommen des Suchstrings ohne Duplikate
## Komplexität
worst-case ist $O(m^{3}\cdot |\Sigma| +n)$
Wir haben also eine sehr gute Laufzeit für lange Text in denen wir suchen (S)
## FUCKY START
fängt mit dem ersten char bei `i=0` an
## Links
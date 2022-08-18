---
aliases: 
---
# String Matching basierend auf endlichem Automaten 
## Abstrakt
- T: Den String den wir suchen
- m: die Länge von T
- S: Der String in dem wir suchen
- n: die Länge von S
- R: Liste der Start-Indizes von gefundenen Strings (T in S)
- I: Liste der möglichen Kandidaten, bevor sie in R geschrieben werden
- r: die Maximale Anzahl an Kandidaten, die gleichzeitig in I sein können.
- q: die aktuell maximale prefix Länge
### Invariante
Nach $i \geq 0$ Iterationen:
R beinhaltet alle Start-Indizes von T's in S in aufsteigender Ordnung.
q ist die größtmöglichste Zahl, wobei von dem Punkt wo wir aktuell in S sind (also der Punkt i) der Suffix
### Variante

### Abbruchbedingung

## Komplexität


## Links
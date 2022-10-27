---
aliases: 
---
# Syntaxbäume 
Ein Syntaxbaum ist ein geordneter, markierter Baum der folgende Eigenschaften hat:
- Die Blätter sind mit [[Terminalsymbol|Terminalsymbolen]] markiert
- Die inneren Knoten sind mit [[Nicht-Terminalsymbol|Nicht-Terminalsymbolen]] markiert
- Die Kinder $X_{1},\dotso X_{n}$ eines Knotens $N$ können aus der Produktion $N:=X_{1} \dotso X_{n}$ erzeugt werden. 
## Konkrete und Abstrakte Syntaxbäume
### Konkreter Syntaxbaum
Bei einem konkreten Syntaxbaum kommt alles im Baum vor, man hat an den Blättern damit quasi das ganze Programm stehen.
### Abstrakter Syntaxbaum
Bei einem abstrakten Syntaxbäumen werden nur essentielle Informationen modelliert. Das heißt Schlüsselwörter und Begrenzer wie `do` oder `:=` sind irrelevant und können weggelassen werden.
## Links
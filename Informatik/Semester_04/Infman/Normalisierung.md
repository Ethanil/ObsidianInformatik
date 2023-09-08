---
aliases: 
---
# Normalisierung 
Bei der Normalisierung wird ein schlechtes [[Logisches Datenmodell|relationales Modell]] in ein gutes Modell überführt. (Also in eine höhere [[Normalformen|Normalform]])
Die Idee ist ein großes Relationsschema in mehrere kleine zu zerlegen. Wobei die Zerlegung danach
- möglichst redundanzfrei ist
- verlustfrei vom vorherigen Modell abgelitten ist.
## Kriterien
1. Verlustlosigkeit: Die Daten in der ursprünglichen Relation $r(R)$ müssen verlustfrei aus $r_{1}(R_{1}),\dotso,r_{n}(R_{n})$ rekunstruierbar sein
	- Die Zerlegung von $R$ ist verlustfrei, falls für jede mögliche Ausprägung $r$ gilt: $r = r_{1} \bowtie r_{2}$ 
2. Abhängigkeitserhaltung: Die für $R$ geltende FDs müssen alle in den Relationsschemata $R_{1},\dotso,R_{n}$ enthalten sein
	- Bei einer Zerlegung gilt die Abhängigkeitserhaltung wenn vor und nach Zerlegung gilt: $F_{R} \equiv (F_{R1}\cup \dotso \cup F_{Rn})$
## Links
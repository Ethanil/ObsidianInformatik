---
aliases: [Pipelining]
---
# Pipelines
Beim Pipelining hat beispielsweise nur jede Station einen Arbeitsschritt, aber alle unterschiedlichen Arbeitsschritte an den mehrfachen Stationen werden parallel ausgeführt, was zu [[Parallelität#zeitliche Parallelität|zeitlicher Paralellität]] führt.
## Grundlegende Begriffe
- Ein Datensatz ist der Vektor aus Eingabewerten, zu denen ein Vektor aus Ausgabewerten berechnet wird
- die Latenz ist die Zeit von der Eingabe eines Datensatzes bis zu Ausgabe des zugehörigen Ergebnisses
- Ein Durchsatz ist die Anzahl von Datensätzen, die pro Zeiteinheit bearbeitet werden können
	- [[Parallelität]] erhöht diesen Durchsatz

## Beispiel Plätchen backen
Wenn ein einzelner Bäcker mit einem einzelnen Blech und Ofen immer das Blech in den schiebt, nachdem er es belegt hat und dann wartet, bis es fertig ist, benutzt er überhaupt keine [[Parallelität]].
Wenn er nun anfängt mit einem zweiten Blech dieses immer schon zu belegen, während das letzte im Ofen backt, dann benutzt er zeitliche Parallelität (und etwas räumliche, da er jetzt ja 2 Bleche hat)(wenn die Backzeit 3/4 der Gesamtzeit ausmacht und die Belegzeit 1/4, haben wir eine Steigerung von 33%)
Wenn ihm nun eine zweite Person hilft und einen zweiten Ofen hat und beide arbeiten so wie im Anfang (also an sich sequentiell), dann können doppelt so viele Plätzchen in der selben Zeit gebacken werden. (100%)
Wenn die beiden Bäcker nun auch noch Zeitlich Parallel arbeiten, dann haben wir eine Steigerung von 166% !
## Stufen von Pipelines
Bei Schaltungen betrachten wir immer unterschiedliche Pipeline-Stufen. Jede Pipeline-Stufe ist von 2 Registern umrahmt. 
Um die Taktzahl einer Schaltung zu erhöhen können wir die Anzahl der Stufen erhöhen, da wir so eine zeitliche [[Parallelität]] erzeugen, wobei hier immer die Stufe mit dem längsten kritischen Pfad die maximale Taktfrequenz vorgibt.
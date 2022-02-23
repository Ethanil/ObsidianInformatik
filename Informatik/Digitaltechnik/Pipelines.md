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
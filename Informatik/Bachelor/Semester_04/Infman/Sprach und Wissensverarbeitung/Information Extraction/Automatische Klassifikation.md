---
aliases: 
---
# Automatische Klassifikation 
Klassifikation ist die Aufgabe einem gewissen Input ein gewisses Label zu geben, basierend an dessen Eigenschaften.
Wir wollen eine menge von Datenpunkten klassifizieren.
Diese Datenpunkte haben Eigenschaften, anhand derer wir sie in einen [[Vektorraum]] positionieren können.
Wir müssen nun nurnoch ein Modell anlernen, welches diese Datenpunkte einem Label zuordnet, wobei das Modell generalisieren soll.
## Varianten
- Binär-Klassifikation vs Multi-Klassen-Klassifikation
- Single-Label vs Multi-Label Klassifikation
- Sequenz-Klassifikation

## Supervisierte Klassifikation
Eine Modell, welches klassifiziert heißt dann supervisiert, wenn es mithilfe von Trainingsdaten geschult wurde, welche korrekte Label für jeden Input hatte.
Wir gehen dabei wie folgt vor:
- Sammle Trainings-, Entwicklungs- und Test-Daten (Daten sollten gesplittet werden!)
- Repräsentiere den Input (mittels Eigenschaften)
- Suche einen Algorithmus aus und trainiere das Modell
- Evaluiere die Ergebnisse und führe die Aufgabe aus
## Links
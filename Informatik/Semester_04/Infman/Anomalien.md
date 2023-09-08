---
aliases: 
---
# Anomalien 
## Update-Anomalien
Wenn in einem [[Relationales Datenmodell|relationalem Datenmodell]] Redundanzen vorhanden sind und wir eine der redundanten Informationen ändern, müssten wir alle gleichen auch ändern. Wenn wir dies nicht machen, kommt es zu Update Anomalien
## Einfüge-Anomalien
Wenn wir in einer Tabelle Informationen gespeichert haben, die nicht eigenständig vorhanden sein können, dies aber möglich ist, kommt es zu Einfüge-Anomalien (bspw. eine Tabelle mit Produkten, ihrer MWst und der Steuerkategorie: Wenn wir eine neue Steuerkategorie hinzufügen wollen müssen wir ein Produkt dieser Kategorie hinzufügen)
## Lösch-Anomalien
Wie Einfüge-Anomalien nur andersherum. Da wir in der Tabelle Daten in kombination mit anderen Daten gespeichert haben, kann es vorkommen dass wir das letzte vorkommen von den Daten A verlieren, weil wir die Daten B löschen, obwohl wir nur die Daten B löschen wollten. (Bsp. von Einfüge Anomalien, wobei wir das letzte Produkt einer Steuerkategorie entfernen)

## Links
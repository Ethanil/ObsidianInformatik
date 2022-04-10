---
aliases: 
---
# Volladdierer
Ein Volladdierer-Modul ist aufgebaut aus n-Eingängen für die Zahlen, die addiert werden sollen(meist 2) und einem Eingang für den Übertrag aus dem vorherigen Modul (hier wird eine 0 angelegt beim ersten Modul).
Als Ausgang gibt es sowohl den Wert der Stelle, als auch den Übertrag für das nächste Modul (oder für den Wert der nächsten Stelle, falls es keine weiteren Module gibt).
## Aufbau
Ein Volladdierer kann aus 2 [[Halbaddierer|Halbaddierern]] aufgebaut werden, von denen der 1. die beiden Zahlen addiert und der 2. dann die Summe der beiden Zahlen mit dem vorherigen Übertrag summiert. Wenn nun einer der beiden Halbaddierer einen Übertrag hatte, dann gibt es einen Übertrag ([[Disjunktion(oder)|Or-Gatter]])
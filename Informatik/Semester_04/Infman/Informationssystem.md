---
aliases: 
---
# Informationssystem 
## Anforderungen
- [[Informationserhalt]]
- Wiedergewinnung der [[Daten]] soll möglichst effizient sein
- [[Konsistenzerhaltung]]
- Anwendungsdaten sollen möglichst redundanzfrei gespeichert werden, um Speicherplatz zu sparen und [[Anomalien]] zu vermeiden

## Entwurfsprozess
1. Anforderungsanalyse (requirements analysis)
	- Fachwissen, Terminologie, Geschäftsfälle, Kosten-/Nutzen-Analyse, Informationsbedarf
	- Informelle Dokumentation, z.B. Interviews, Texte, Formblätter
2. Konzeptioneller Entwurf (conceptual design)
	- Abstrakte Modellierung der Anwendungsdomäne
	- Welche Objekte spielen eine Rolle, wie hängen diese zusammen?
	- Formale Beschreibung, z.B. ER-Modell, UML-Strukturmodell
3. Verteilungsentwurf (distributed system design)
	- Fragmentierung der Daten, Synchronisation und Replikation
4. Logischer Entwurf (logical design)
	- Abbildung des konzeptionellen Modells auf Konzepte des eingesetzten Informationssystems, implementierungsspezifisch, aber geräteunabhängig
	- Logische Datenmodelle, z.B. relationales Modell
5. Datendefinition (data definition)
	- Deklaration/Programmierung des Datenmodells im Informationssystem
	- Definitionssprachen, z.B. SQL
6. Physischer Entwurf (physical deisgn)
	- Definition von Zugriffs- und Speicherstrukturen
	- Wie werden die Daten auf der Festplatte abgelegt?
7. Implementierung und Wartung
## Links
---
aliases: 
---
# Vorlesung 14 
## Border Gateway Protocol(BGP)
- Einzelne autonome Systeme (AS) werden als ein Knoten zusammengewasst
- BGP kümmert sich nur um das routing zwischen diesen Knoten
- BGP wählt primär längster Präfix und sekundär über kürzeste Route
## Sicherheit
- BGP Hijacking
	- Manipuliere Prefix, damit der länger(spezifischer) ist -> alle Daten laufen über dieses Netzwerk (Redirection)
	- Manipuliere Prefix, damit er gleich ist -> die spezifischen Daten gehen an mich(Subversion)
		- Resource Public Key Infrastructure(RPKI)
			- Resourcen die BGP-table Entscheidung ergänzen
## Links
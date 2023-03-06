---
aliases: 
---
# Vorlesung 8 
## DAC (Discretionary Access Control)
Zugriffsmatrix beschreibt Rechte von Subjekten an Objekten(oder andersherum), oft mittels ACL (access control lists)
## RBAC (Rolebased Access Controll)
Jeder Benutzer hat Rollen und jede Rolle hat bestimmte Rechte. In einer Sitzung sind immer bestimmte Rollen aktiv. Rollen können sich gegenseitig ausschließen. Entweder statisch(diese beiden Rollen darf kein Benutzer gleichzeitig haben) oder dynamisch(niemand darf diese beiden Rollen gleichzietig aktiv haben)
## MAC (Mandatory Access Control)
Das System überwacht Zugriffsrechte.
### Bell-La Padula
Jedes Subjekt und Objekt hat eine Sicherheitsklasse(Label + Sicherheitskategorie).
- no read up: Lesezugriff nur auf selber Ebene oder nach unten erlaubt
- no write down: Schreibzugriff nur auf selber Ebene oder obendrüber erlaubt
- strong tranquility: Während Systemlaufzeit darf an Sicherheitsklassen nichts geändert werden
## Links
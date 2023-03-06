---
aliases: 
---
# Vorlesung 9 
- Identität (Menge von Attributen)
- Authentisierung(Bereitstellung von Unterlagen zur Identitätsprüfung)
- Authentifikation (Prüfung der Unterlagen)
- Autorisierung(Gewährung von Rechten)
## Überprüfung und Bestätigung einer Identität
- Wissen(Passwort)
- Besitz(Smartcard)
- Merkmal(Biometrie)

- Einseitige vs Wechselseitige Authentifizierung
### Challenge-Response-Verfahren
- Client schickt ID an Server
- Server erzeugt Challenge und schickt zu Client
- Client löst Challenge und schickt Lösung an Server
- Server vergleicht Lösung der Challenge mit seiner eigenen

## Kerberos
- AS stellt Ticket-Granting-Ticket(TGT) aus
- Mit TGT können wir zum Ticket-Granting-Server(TGS) gehen und uns dort ein Ticket für einen Service holen
- Mit diesem Ticket können wir den Service nutzen
## Links
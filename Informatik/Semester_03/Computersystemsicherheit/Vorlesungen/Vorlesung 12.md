---
aliases: 
---
# Vorlesung 12 
## OSI-Modell
| Name               | Was passiert da                                                   |
| ------------------ | ----------------------------------------------------------------- |
| Physical Layer     | Daten zu physikalische Signale                                    |
| Datalink Layer     | Verbindet 2 Netzwerkgeräte                                        |
| Network Layer      | Weltweit eindeutiger logischer Adresse + Routing                  |
| Transport Layer    | Aufteilung der Daten in Segmente, Flusskontrolle, Fehlererkennung |
| Session Layer      | Authentifizierung und Authorisierung, Encryption, Decrytption     |
| Presentation Layer | Konvertiert, Komprimiert und Encrypted/Decrypted Daten            |
| Application Layer  | Stellt Funktion für netzbasierte Software bereit (HTTP,FTP,SMTP)   |
## TCP/IP Modell
| Layer             | Was            |
| ----------------- | -------------- |
| Link Layer        | MAC-Adresse    |
| Internet Layer    | IP Adresse     |
| Transport Layer   | Port/Protokoll |
| Application Layer | HTTP,FTP,SMTP  |

192.168.0.101/24 -> 24 sind die Anzahl der **führenden** Bits
## IP-Auflösung
- Mittels Broadcast (who has ip1, tell ip2) (Address Resolution Protocol(ARP))
## Dynamic Host Configuration Protocol(DHCP)
- $C \rightarrow all$: Discover(broadcast)
- $S \rightarrow C$: Offer //Alternativ: Offer von Eve
- $C \rightarrow S$: Request
- $S \rightarrow C$: Ackknowledge
### Snooping:
Switch leitet nur Offer von authorisierten Servern weiter.
## Denial of Service (DOS) - Angriffe
Ziel: Verfügbarkeit von Diensten einschränken
### DOS und DDOS
Ein(dos) bzw mehrere(ddos) Rechner involviert
### Ping of Death(PoD)
Schicke miskofingurierte ICMP Nachricht(eigentlich für Information bzw Fehlermeldungen des Netzwerks)
### Smurf (Broadcast Attack)
Tue so, als würdest du als zu dos'ender Server pingen und alle antworten zum Server
### Syn-Flood
Sence SYN-Anfragen ohne SYN-ACK mit ACK zu beantworten (normalerweise C sendet SYN, Server SYN-ACK und dann Antwort mit ACK)
### SYN-ACK-Flood
Zue so, als würdest du als zu dos'ender Server SYN-Anfragen schicken -> viele SYN-ACKs
### UDP Flood
sende gespoofte UDP-Pakete -> Server sucht ziel davon und Antwortet mit ICMP in die Leere
## Firewall
Zustandslos vs Zustandsbasiert
## Intrusion Detection und Prevention (IDS/IPS)
- Netzsensoren
- Hostsensoren
- Datenbankkomponenten
- Managmentstation
- Auswertungsstation
	- Angriffsmuster
	- Anomalieanalyse
	- Korrelation
## Links
[[Vorlesung 13]]

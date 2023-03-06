---
aliases: 
---
# Vorlesung 13 
## Domain Name System(DNS)
- rekursiv vs iterativ
- DNS Cache Poisoning
	- im Auflösevorgang
		- Resolver verwerfen Records die nicht zu ihnen gehören
	- Off-Path (Antwortet schneller)
		- Randomisierte UDP-Quellports/Zusätzlich zufällige ID
	- MITM
		- DNSSEC - Records werden signiert
		- DoH/DoT (DNS over HTTPS/TLS)
- Domain Hijacking
- Flooding Angriff
- Zensur
- DNS Amplification DDos
	- Kapazitätsreserven schaffen(Opfer)
	- Minimierung der Antwortgröße(DNS-Dienst)
	- Eliminierung von Paketen(Gegen Angreifer)
- DNS Tunneling (Übertrage Daten via DNS)
	- Firewall
- Sender Policy Framework(SPF)
	- In DNS-Einträgen steht, wer E-Mails senden darf, andere werden geblockt
- DKIM
	- E-Mail wird signiert und öffi steht im DNS
## Links
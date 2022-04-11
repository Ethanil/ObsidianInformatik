---
aliases: FPGA
---
# Field Programmable Gate Array
FPGAs verwenden feingranulare (bitweise) Konfigurationsspeicher statt wortweisen Instruktionsspeichern. Diese können mittels verschiedener Speicher-Technologien realisiert werden (bspw SRAM, oder auch Flash)
## Aufbau
![[Pasted image 20220228180050.png]]
### Pin
Der Pin wird verwendet als Brücke zu anderen Modulen.
### IOB
IOB verarbeiten den In/Output von und für den Pin. Dafür werden [[Tristate Buffer]] und [[Multiplexer]] verwendet.
### SM
Die Switch Matrix besteht aus Programmierbaren Leitungskreuzungen aus [[Tristate Buffer]], die ihr Enable-Signal vom Speicher des FPGA's bekommen.
### LC
Die Logic Cell ist aus [[Speicherfelder#Lookup-Tabelle LUT|Lookup Tabellen]] und [[Multiplexer|Multiplexern]] aufgebaut, mit denen die kombinatorische Logik realisiert ist. Den Dateninput für das Verhalten kommt auch hier aus dem Speicher des FPGA's
### FB
Die Funktionsblöcke bestehen aus einer begrenzten Menge häufig verwendeten Logikbausteinen wie bspw
- SRAM
- [[Multiplikator]]
- Taktmodifikation (via Phase-Locked Loop PLL)
- Kommunikations-Treiber (USART, USB, Ethernet)
- kleine Prozessoren
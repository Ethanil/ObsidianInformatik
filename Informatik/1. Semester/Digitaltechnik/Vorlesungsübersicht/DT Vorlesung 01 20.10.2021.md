# Einordnung der [[Digitaltechnik]]
![[DT_VL_01_V2.pdf]]
Computersysteme wie
- Handys, Internet, Medizintechnik, Unterhaltung
Anforderungen steigen ständig
-> Man benötigt ein tiefgreifendes Verständnis von Computern
## Technische Informatik
Teilgebiet der Informatik, das sich mit der Entwurf und Realisierung von Computersystemen befasst
- Sensortechnik
- **Digitaltechnik**
- Rechnerarchitektur
- Betirebssysteme
- Compiler
- ...

# Lernziele der DT
## Grundlagen
- Digitale Abstraktionen und ihre technische Umsetzung
- Zahlensysteme
- Logikgatter
- MOSFET Transistoren und CMOS Gatter
- Leistungsaufnahme

## Kombinatorische Schaltungen
- Boole'sche Gleichungen und Algebra
- Abbildung auf Gatter
- Mehrstufige Schlatungen
- Vierwertige Logik (0,1,X,Z)
- Minimierung von Ausdrücken
- Kombinatorische Grundelemente
- Zeitverhalten

## Sequentielle Schaltungen
- Latches
- Flip-Flops
- Entwurf synchroner Schaltungen
- Endliche Automaten
- Zeitverhalten
- Parallelität

## Hardware-Beschreibungssprachen (SystemVerilog)
- Modellierung kombinatoprischer und sequetieller Schaltungen
- Strukturbeschreibung
- Modellierung endlicher Automaten
- Datentypen
- Parametrisierte Module
- Testrahmen

## Grundelemente digitaler Schaltungen
- Arithmetische Schaltungen
- Sequentielle Grundelemente
- Speicherfelder
- Logikfelder

# Komplexität, Abstraktion und Technikmodelle
## Von 0 nach 1
- [[Beherrschung von Komplexität]]
- Digitale Abstraktion
- Zahlensysteme
- Logikgatter
- Darstellung als elektrische Spannungen
- CMOS Transistoren
- Elektrische Leistungsaufnahme

# Bits und Bytes
## Binärsystem als Digitale Disziplin
Im Binärssystem beschränken wir uns auf 2 Werte:
True/False
High/Low
1/0
## Bits
```ad-note
title:Bits
Ein Bit ist die Maßeinheit für Informationen
```
Eine solche Kodierung ist notwendig und sinnvoll um
- Technische Realisierung über Schwellwerte zu verinfachen
- Elektrische Ladung darzustellen (0 = ungeladen, 1= geladen)
- Elektrische Spannung darzustellen (0 = 0 Volt, 1= 5 Volt)
- etc
## Bitfolgen
Wenn wir mehr als nur 2 Zustände darstellen möchten müssen wir Bits kombinieren
```ad-example
title: Himmelsrichtungen
Um Himmelsrichtungen darzustellen, brauchen wir 2 Bits:
- 0 0 = Norden
- 0 1 = Osten
- 1 0 = Süden
- 1 1 = Westen
Wenn wir nun die Zwischenzustände darstellen möchten bräuchten wir noch ein weiteres bit:
- 0 0 0 = Norden
- 0 0 1 = Nord-Osten
- 0 1 0 = Osten
- 0 1 1 = Süd-Osten
- 1 0 0 = Süden
- 1 0 1 = Süd-westen
- 1 1 0 = Westen
- 1 1 1 = Nord-Westen
```
### Zweierpotzenzen: das Einmaleins der Informatik
Da wir in Bits rechnen, benötigen wir die Zahlenfolge der Zweierpotenz um bspw zu wissen, wieviele Zustände wir darstellen können:
2⁰ = 1
2¹ = 2
2² = 4
2³ = 8
...
2¹⁰ = 1024 (Kibi)
2²⁰ = 1024 \* 1024 (Mebi)
2³⁰ = 1024 \* 1024 \* 1024 (Gibi)
2⁴⁰ = 1024 \* 1024 \* 1024 \* 1024 (Tebi)

### Nomenklatur für Teile von Bitfolgen
Um Bitfolgen besser zu lesen, teilen wir
4 Bits in 1 Nibble
8 Bits in 1 Byte ( bzw 2 Nibble in 1 Byte)
2 Bytes in 1 Halbwort
2 Halbwort in 1 Wort
Halbwort und Wort hängt meistens vom Kontext ab, Byte ist viel wichtiger!

# Zusammenfassung und Ausblick
- Organisation
	- Bis Übermorgen(22.10) 12:00 Gruppenwunsch
	- Übungsaufgabe bearbeiten
- Inhalt
	- Einordnug der Digitaltechnik
	- Wie Beherrschen wir Komplexität
	- Einführung in Bits
- Ausblick:
	- Zahlensysteme
		- Wie stellen wir Zahlen in bits dar
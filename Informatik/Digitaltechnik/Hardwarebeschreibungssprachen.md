---
aliases: [HDL,"HDL's"] 
---
# Hardwarebeschreibungssprachen
Hardwarebeschreibungssprachen sind notwendig um die steigende Komplexität technischer Systeme neherrschen zu können. ([[Moore'sches Gesetz]])
Dabei benutzen sie auch [[Beherrschung von Komplexität#Hierarchie Hierarchy|Hierarchie]], [[Beherrschung von Komplexität#Modularität Modularity|Modularität]], [[Beherrschung von Komplexität#Regularität Regularity|Regularität]] als Konzepte.
## Geschichte
Seit Beginn der Rechnerentwicklung wurde nach verständlichen und einheitlichen Beschreibungssprachen für
- Designspezifikation
- Simulation
- Verifikation
- Dokumentation
gesucht.
Zunächst wurden Hochsprachen wie bspw. [[Pascal]], [[LISP]], [[Petri-Netze]] zur Hardware-Beschreibung eingesetzt.
1960/70 wurden Register-Transfersprachen verwendet, die den Datentransfer zwischen [[Register|Registern]] durch [[Kombinatorische Logik|kombinatorische Operatoren]] verwendeten.
## Wichtige HDL Standards
### Consensus Language (CONLAN)
CONLAN ist eine allgemeine, erweiterbare Sprache, die den akademischen "Wildwuchs" in geordnete Bahnen lenken und damit die Akzeptanz von HDL's in der Industrie fördern sollte.
### Very High-Speed Integrated Circuits HArdware Description Language (VHDL)
VHDL wurde vocm US Department of Defense maßgeblich gefördert und hat den IEEE Standard 1076. VHDL wurde 1998 zu VHDL-AMS (analog and Mixed-Signal) erweitert.
### Verilog HDL
Verilog wurde von Gateway Design Automation (Cadence) zur Simulation entwickelt. Hat den IEEE Standard 1364. Wurde 1998 zu Verilog-AMS (Analog and Mixed-Signal) und 2002 zu [[SystemVerilog]] erweitert.
## Aktuelle Tendenz
Die aktuelle Tendenz geht hin zu Höheren Abstraktionslevel wie [[SystemC]], [[Chisel]] oder [[BSV]] und High-Level-Synthese, also aus low-level Verilog/VHDL aus abstrakten Anwendungsbeschreibungen ([[C]], [[Java]], [[Matlab]]) zu erzeugen.
## Von HDL zu [[Logik-Realisierung mit Basis-Gattern]]
Die HDL simuliert das funktionale/zeitliche Verhalten der beschriebenen Schaltung, also werden die vorgegebenen Eingaben auf Korrektheit überprüft, was um ein vielfaches einfacher und billiger ist als dies in realer [[Hardware]] zu machen.
Synthese übersetzt die Hardware-Beschreibung dann in eine [[Netzliste]]
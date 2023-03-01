---
aliases: 
---
# Diagrammarten 
## CFG Diagramm
- Javacode in basic blocks aufteilen und an JEDE Kante eine EINZELNE Bedingung schreiben
![[Pasted image 20230301144728.png]]
## Feature Diagramm
| Beschreibung                                    | Was ist es                      |
| ----------------------------------------------- | ------------------------------- |
| ausgefüllter winkel                             | or                              |
| nichts                                          | and                             |
| leerer Kreis                                    | optional                        |
| ausgefüllter Kreis(braucht ausgefüllter Winkel) | mandatory                       |
| leerer Winkel                                   | xor                             |
| requires auf gestr. Pfeil                       | requires                        |
| excludes                                        | schließt aus                    |
| param mit i                                     | joa param(typ nicht vergessen!) |
![[Pasted image 20230301145015.png]]
## Klassendiagramm
| Art des Pfeils               | Bedeutung                             |
| ---------------------------- | ------------------------------------- |
| Pfeil mit leerem Pfeilkopf   | inherit                               |
| Pfeil mit normalem Pfeilkopf | Komposition (Zahlen nicht vergessen!) |

## Objektdiagramm
Wie Klassendiagramm nur halt Objekte, die Namen haben
![[Pasted image 20230301144658.png]]
## Strategie Diagramm
Wie Klassendiagramm, nur Strategie
![[Pasted image 20230301144855.png]]
## Domänendiagramm
An sich ein Klassendiagramm, aber wir haben keine komposition. Jede Kante hat einen Namen und wie oft es vorkommt.
![[Pasted image 20230301144630.png]]
## LCOM-Diagramm
- Methoden zusammenfassen nach ihnen verbindende Fields
![[Pasted image 20230301144757.png]]
## Use Case Diagramm
- Ein großes Viereck mit Überschrift
- Kreise für Use-Cases
- außerhalb des Vierecks Aktoren, die den Use Cases zugeordnet sind
- extends, erweitert optional einen Usecase abhängig von dem extensionpoint(diesem muss einen namen gegeben werden) und extends hat eine Bedingung
- includes fügt einen use case zu einem anderen zwangsweise hinzu
![[Pasted image 20230301144611.png]]
## State machine Diagramm
- quasi wie ein FSM
- Einsteigspunkt ausgefüllter Punkt
- erfolgreicher endzustand ist ein umkreister Punkt
- zwischendrin die States und untendrunter jeweils sachen die ausgeführt werden aufgeteilt in
	- entry
	- do
	- exit
- die states werden gewechselt über einen methodencall, der auch sachen ändern kann, dieser kann eine guard haben
	- es gibt zusätzlich noch eine methode die bei dem übergang gecalled wird und was machen kann
![[Pasted image 20230301144642.png]]

## Links
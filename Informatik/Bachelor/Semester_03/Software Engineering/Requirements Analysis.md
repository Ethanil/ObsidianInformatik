---
aliases: Requirement, Requirements
---
# Requirements Analysis 

## Anforderungen
### Was sind Anforderungen
Anforderungen sind die Beschreibungen 
- der Dienste, die ein System bereitstellt.
- der Randbedingungen die das System erfüllen muss
### Arten von Anforderungen
#### Benutzer-Anforderungen
Beschreiben in natürlicher Sprache oder Diagrammen
- Was für Dienstleistungen erwartet wird, dass das System bereitstellt
- In welchem Umfeld der Dienst arbeitet
#### System-Anforderungen
Sind präzise und detailierte Spezifikationen über das System und beschreiben
- Funktionen und Dienste
- Operationelle Nebenbedingungen
#### Funktionale Anforderungen (FR)
Welche Funktionen der Dienst bereitstellen soll.
Welche Reaktionen das System zu spezifischen Inputs oder Events haben soll.
Welches Verhalten soll das System in spezifischen Situationen haben.
#### Nicht-Funktionale Anforderungen (NFR)
Einschränkungen/Nebenbedinungen die wir an das System stellen. Beispielsweise wie schnell das System auf einen Input reagiert.
NFRs beziehen sich häufig auf verschiedene Module im System und nicht nur ein spezifisches (anders als idR die FR).
Kann auch häufig nicht nur durch Software umgesetzt werden.
##### Arten von Nicht-Funktionalen Anforderungen
- Portabilität
- Verlässlichkeit
- Effizienz (Perfomanz, Größe)
- Benutzbarkeit (Sprache des GUI)
- Wie kommt das Produkt an den Kunden (Delivery)
- Implementierung (Welche Sprache)
- Standards (ISO 9000)
- Interoperabilität (Funktioniert mit anderen Systemen)
- Ethische Betrachtungen
- Gesetzliche Vorschriften (safety, security, privacy) z
#### Domänen Anforderungen
Entstehen aus der Domäne für die die App entwickelt wird. 
- Die Anforderungen sind häufig in Domänen-spezifischer Sprache formuliert und dadurch schwer für "Außenstehende"(Also dem Software-Entwickler) zu verstehen.
- Die Anforderungen werden von den Experten aus der Domäne häufig als offensichtlich angesehen und gar nicht formuliert.
- Können Funktional oder Nicht-Funktional sein.

## Viewpoint-oriented approach
Das System kann aus verschiedenen Sichtweisen betrachtet werden
### Interactor viewpoint (Benutzer)
Personen (oder Systeme), die direkt mit dem System interagieren, wie Endverbraucher, Administratoren oder Service-Personal
### Indirect viewpoint (Stakeholder)
Personen, die Interesse am System haben, obwohl sie nicht direkt mit dem System interagieren. Beispielsweise CFO oder Datenzschutzbeauftragte
### Domain viewpoints
Domänen Besonderheiten und Beschränkungen die die Systemanforderungen beschränken, wie beispielsweise Gesetzesvorschriften.

## Arten die Anforderungen zu erfassen
### Interviews
#### Closed Interviews
Bei geschlossenen Interviews werden vorgefertigte Fragen gestellt (zum Beispiel via Fragebogen)
#### Open Interviews
Bei offenen Interviews werden verschiedene Fragen gestellt.
#### Problematik mit Interviews
Interviews sollten nur als zusätzliche Informationsquelle verwendet werden, da beispielsweise die Kooperation nicht immer gegeben ist (Der Interviewte hat bspw. Angst seinen Job zu verlieren) oder weil Domänen-Wissen vom Interviewten vorausgesetzt/verwendet wird.
### Szenarien
Sequenz von Interaktionen mit dem System.

## Anforderungen klassifizieren
Mittels des `FURPS+`-Modells
- **F**unctional
- **U**sability
- **R**eliability
- **P**erformance
- **S**upportability
- +
	- Implementation
	- interfaceOperations
	- Packaging
	- Legal
### Priorisierung der Anforderungen
Es kann vorkommen, dass nicht alle Anforderungen erfüllt werden können, dann müssen manche priorisiert werden und Konflikte durch Gespräche aufgelöst werden.
## Links
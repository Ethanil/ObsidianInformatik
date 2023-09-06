---
aliases:
  - ER-Diagramme
  - ER-Modell
  - ER-Modelle
---
# ER-Diagramm 
ER-Diagramme/Modelle oder Entity-Relationship Diagramme/Modelle sind zur [[Konzeptionelles Datenmodell|konzeptionellen Modellierung]] von [[Daten]]:
Sie legen den Fokus auf statische Eigenschaften von Daten und haben im Gegensatz zu [[UML-Klassendiagramm|UML-Klassendiagrammen]] keine dynamische Eigenschaften.

Sie haben eine einfache/intuitive Darstellung und ermöglichen so die Diskussion mit Endanwendern übnner Anforderungen

## Graphische Notation (nach Chen) - Chen-Notation
### Entitätstype
Wird mit einem Rechteck notiert bzw mit E(Attribut1, Attribut2...)
Ist der gemeinsame Typ aller Instanzen eines Typs - Vergleiche Entität: Ein individuell identifizierbares Objekt
### Beziehungstyp
Wird mit einer Raute notiert bzw mit R(Entitätstyp1, Entitätstyp2,... ; Attribut1, Attribut2,....)
Beschreibt die Beziehung zwischen zwei oder mehr Entitätstypen, wobei eine Beziehung eine konkrete Beziehung zwischen zwei oder mehr Entitäten darstellt.
#### Rekursiver Beziehungstyp
Wird gleich wie ein normaler Beziehungstyp notiert
Setzt eine Entität mit einer Entität des gleichen Typs in Beziehung, dabei sind Rollennamen hilfreich!
#### Kardinalitäten bzw Funktionalitäten
Kardinalitäten werden als Zahl zwischen Entitätstypen und Beziehungstypen notiert.
Sie legen fest an wie vielen konkreten Beziehungen eine Entität maximal beteiligt sein kann.
### Attribut / Merkmal
Wird als Oval notiert
#### Schlüsselattribute
Wird als unterstrichenes Attribut notiert.
Schlüsselattribute sind die Teilmenge der Attribute eines Entitätstyps, die eine Entität eindeutig identifiziert. 
##### Auswahl
Die Auswahl der Schlüsselattribute ist eine Modellierungsentscheidung und benötigt Anwendungs-/ Domänenwissen.
Man kann gegebenenfalls künstliche Schlüsselattribute einführen.
## min-max
## Links
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
![[ER-Diagramm 07.09.2023 01-07-41.excalidraw|100]]
Ist der gemeinsame Typ aller Instanzen eines Typs - Vergleiche Entität: Ein individuell identifizierbares Objekt
#### schwache Entitätstypen
Werden wie die zugehörige Beziehung doppelt umrahmt. Das Schlüsselattribut wird gestrichelt unterstrichen.
Existieren nur, wenn auch starke Entitätstypen existieren.
![[ER-Diagramm 07.09.2023 01-10-56.excalidraw]]
### Beziehungstyp
Wird mit einer Raute notiert bzw mit R(Entitätstyp1, Entitätstyp2,... ; Attribut1, Attribut2,....)
![[ER-Diagramm 07.09.2023 01-08-25.excalidraw|100]]
Beschreibt die Beziehung zwischen zwei oder mehr Entitätstypen, wobei eine Beziehung eine konkrete Beziehung zwischen zwei oder mehr Entitäten darstellt.
#### Rekursiver Beziehungstyp
Wird gleich wie ein normaler Beziehungstyp notiert
Setzt eine Entität mit einer Entität des gleichen Typs in Beziehung, dabei sind Rollennamen hilfreich!
#### Kardinalitäten bzw. Funktionalitäten
Kardinalitäten werden als Zahl zwischen Entitätstypen und Beziehungstypen notiert.
Sie legen fest an wie vielen konkreten Beziehungen eine Entität maximal beteiligt sein kann.
![[ER-Diagramm 07.09.2023 01-00-43.excalidraw]]
sprich: N Flächen umhüllen 1 Polyeder
### Attribut / Merkmal
Wird als Oval notiert
![[ER-Diagramm 07.09.2023 01-09-19.excalidraw|100]]
#### Schlüsselattribute
Wird als unterstrichenes Attribut notiert.
Schlüsselattribute sind die Teilmenge der Attribute eines Entitätstyps, die eine Entität eindeutig identifiziert. 
##### Auswahl
Die Auswahl der Schlüsselattribute ist eine Modellierungsentscheidung und benötigt Anwendungs-/ Domänenwissen.
Man kann gegebenenfalls künstliche Schlüsselattribute einführen.

### Generalisierung (Vererbung)
Wird mit einem 6-eck in dem "is-a" steht notiert, Untertypen zeigen mit einem Pfeil auf dieses und das 6-eck zeigt auf den Obertypen.
![[ER-Diagramm 07.09.2023 01-14-56.excalidraw|300]]
Damit können gemeinsame Attribute mehrerer Entitäten in einem Obertypen zusammengefasst werden. Diese Attribute werden also an die Untertypen vererbt.

### Aggregation (Teil-Ganzes Beziehung)
Wird wie ein Beziehungstyp mit einer Raute notiert, wobei der Typ eine "part-of" Beziehung ist.
Beschreibt Teile aus denen ein Entitätstype besteht. Bspw das Fahrrad das aus Rädern und einem Rahmen besteht, die wiederum aus Entitätstypen bestehen.
## min-max-Notation
Ist genauer als Funktionalität, da es die genaue maximale wie auch genaue minimale Anzahl darstellt.
![[ER-Diagramm 07.09.2023 01-02-35.excalidraw]]
sprich: 4 bis * Flächen umhüllen genau 1 Polyeder
Andersherum als Chen-Notation: Hier beschreiben die Zahlen mit wievielen Entitäten A die jeweilige Entität B die Beziehung eingeht und nicht wieviele von Entitäten A an einer Beziehung beteiligt sind.
## Links
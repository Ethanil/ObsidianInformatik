---
aliases:
  - Relationale Algebra
  - Relationale Abfragesprache
---
# Relationale Abfragesprachen 
Eine Relationale Abfragesprache ist dafür da aus einem [[Relationales Datenmodell]] Daten zu extrahieren.
Dabei können drei in der Aussagekraft gleichwertige Ansätze verwendet: Relationalalgebra, Relationentupelkalkül oder Relationenwertebereichkalkül.
(Nur die erste wird behandelt)
## Relationale Algebra(RA)
Jeder der folgenden Operationen bekommt eine oder zwei Relationen als Eingabe und erzeugt eine Relation als Ausgabe. D.h. RA ist geschlossen
### $\sigma:$ Selektion
Die Selektion $\sigma_{P}(r)$ ist die Auswahl aller Tupel aus $r$, welche die Bedingung $P$ erfüllen. $P$ kann dabei aus Konstanten- bzw Attributsselektionen bestehen (Vergleich über $\{=, <, >, \leq, \geq\}$ mit Konstante bzw Attribut) oder aus Logischen Verknüpfungen ($\land, \lor, \lnot$)
### $\pi:$ Projektion
Die Projektion $\pi_\alpha(r)$ ist eine Reduktion aller Tupel in $r(R)$ auf die Spalten $\alpha$, wobei $\alpha \subseteq R$. Duplikate werden eliminiert!
### $\times:$ Kartesisches Produkt
Das kartesische Produkt $r \times s$ ist die Menge aller möglichen Kombinationen der Tupel aus $r$ und $s$.
### $\cup:$ Vereinigung
Die Vereinigung $R \cup S$ ist die Menge aller Tupel, die in $R$ *oder* $S$ enthalten sind.
### $-:$ Mengendifferenz

## Links
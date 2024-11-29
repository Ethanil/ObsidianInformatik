---
aliases:
  - Relationale Algebra
  - Relationale Abfragesprache
---
v# Relationale Abfragesprachen 
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
Die Mengendifferenz $R - S$ ist die Menge aller Tupel, die in $R$, aber nicht in $S$ enthalten sind.
### $\div:$ Relationale Division
$t \in R \div S$, falls für alle $s \in S$ ein $r \in R$ existiert, so dass $r(S)=s(S)$ und $r(R-S) = t$ gilt.
### $\upchi:$ Gruppierung
Die Gruppierung $\upchi_{\alpha, \text{AggregatFkt}(\alpha)}$ gruppiert alle Zeilen nach den Spalten $\alpha$ bzw erschafft neue Aggregat-Spalten nach der [[Anfragesprache SQL#Aggregation und Gruppierung|Aggregatfunktion]].
### $\bowtie:$ Natürlicher und Allgemeiner Join (Verbund)
Der natürliche Join $L \bowtie R$ ist die Menge aller Tupel, die gleiche Einträge in den gemeinsamen Spalten von $L$ und $R$ besitzen, wobei die gemeinsamen Spalten verschmolzen werden.
Der Allgemeine Join $L \bowtie_{P}R$ ist die Menge aller Tupel, für die die Bedingung $P$ erfüllt ist. Die Menge der Spalten der Ausgabe ist gleich der Summer der Menge der Spalten beider Eingaben.
### Äußere Joins
#### ⟕/⟖: Left/Right Outer Join
Wie Natürliche bzw Allgemeine Joins, allerdings werden alle Einträge von $L$ bei einem Left- oder $R$ bei einem Right-Outer Join verwendet, egal ob es diesen Eintrag im jeweils anderen gibt oder nicht.
#### ⟗: Full Outer Join
Wie Left Outer Join (bzw Right Outer Join) nur dass von der anderen Seite alle nicht verwendeten Einträge auch in die Ausgabe kommen.
### ⋉/⋊: Left/Right Semi-Join
Wie Natürlicher bzw Allgemeiner Join nur dass nur die Spalten von $L$(Bei Left) bzw $R$(Bei Right) in der Ausgabe sind. (nicht vergessen, das hier auch alle duplikate gelöscht werden, wie immer!) 
### $\uprho:$ Umbenennen
Man kann sowohl Relationen($\rho_{\text{anderer Name}}(\text{Name})$) als auch Attribute($\rho_{A \leftarrow \text{Attribut1}, B \leftarrow \text{Attribut2}}$) umbennen.

## Äquivalenzen der Relationalen Algebra
### 1. Aufbrechen von Konjunktionen im Selektionsprädikat
$$\sigma_{c1\land c2 \land \dotso \land c_{n}}(R) \equiv \sigma_{c1}(\sigma_{c2}(\dotso(\sigma_{c_{n}}(R))))$$
### 2. $\sigma$ ist kommutativ
$$\sigma_{c1}(\sigma_{c2}(R))\equiv \sigma_{c2}(\sigma_{c1}(R))$$
### 3. $\pi-$Kaskaden: Falls $L_{1}\subseteq L_{2}\subseteq \dotso \subseteq L_{n}$
$$\pi_{L1}(\pi_{L2}(\dotso(\pi_{L_{n}}(R)))) \equiv \pi_{L1}(R)$$
### 4. Vertauschen von $\sigma$ und $\pi$: Falls $\theta$ sich nur auf die Attribute $A_{1},\dotso,A_{n}$ von $\pi$ bezieht
$$\pi_{A_{1},\dotso,A_{n}}(\sigma_{c}(R)) \equiv \sigma_{c}(\pi_{A_{1},\dotso,A_{n}}(R))$$
### 5. $\times, \cup, \cap$ und $\bowtie$ sind kommutativ
### 6. Vertauschen von $\sigma$ mit $\bowtie$
Falls das Selektionsprädikat $c$ nur auf Attribute der Relation $R$ zugreift, kann man die beiden Operationen vertauschen:
$$\sigma_{c1}(R \bowtie S) \equiv \sigma_{c1}(R) \bowtie S$$
### 7. Vertauschung von $\pi$ mit $\bowtie$
Die Projektionsliste $L$ sei $L=\{A_{1},\dotso,A_{n},B_{1},\dotso,B_{n}\}$ wobei $A_{i}$ Attribute aus $R$ und $B_{i}$ Attribute aus $S$ seien
Falls sich das Joinprädikat $c$ nur auf Attribute aus $L$ bezieht, gilt folgende Umformung:
$$\pi_{L}(R \bowtie_{c} S) \equiv (\pi_{A_{1},\dotso,A_{n}}(R))\bowtie_{c}(\pi_{B_{1},\dotso,B_{n}}(S))$$
### 8. Die Operationen $A, \times, \cup, \cap$ sind jeweils assoziativ
### 9. Die Operation $\sigma$ ist distributiv mit $\cup, \cap, -$
### 10. Die Operation $\pi$ ist distributiv mit $\cup$
### 11. Die Join- und/oder Selektionsprädikate können mittels [[Aussagen und ihre Verknüpfungen#de Morgan'sche Regel|de Morgan's Regeln]] umgeformt werden
### 12. Join Ersetzung
Sei $c$ eine Bedingung der Form $A$ $op$ $B$, mit $A$ ein Attribut aus $R$ und $B$ ein Attribut aus $S$ und $op$ ein Vergleichsoperator.
$$\sigma_{c}(R \times S) \equiv R \bowtie_{c} S$$
## Links
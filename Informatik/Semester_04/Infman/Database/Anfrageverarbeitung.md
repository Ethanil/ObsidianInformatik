---
aliases: 
---
# Anfrageverarbeitung 
[[Anfragesprache SQL|SQL]]-Anfragen werden zuerst in einen [[Relationale Abfragesprachen|Logischen Plan]] umgewandelt und dann optimiert. Diese Optimierung läuft in unterschiedlichen Phasen ab. 
Zuerst Optimieren wir regelbasiert, dann kostenbasier.
Das Ziel dabei ist einen Effizienten Ausführungsplan für eine Anfrage zu finden(idR bezogen auf die Minimierung der Ausführungszeit)
## Regel-basierte Optimierung
Die Regel-basierte Optimierung verwendet einen Regelsatz, um einen logischen Ausführungsplan umzuschreiben. Diese Regeln sind dabei unabhängig von den [[Daten]] in der Datenbank.
Wir verwenden die [[Relationale Abfragesprachen#Äquivalenzen der Relationalen Algebra|Äquivalenzen der relationalen Algebra]] zum Umformen:
1. Mittels  [[Relationale Abfragesprachen#1. Aufbrechen von Konjunktionen im Selektionsprädikat|Regel 1]] werden konjuktive Selektionsprädikate in Kaskaden von $\sigma$ Operationen zerlegt
2. Selektions-Pushdown: Mittels Regeln  [[Relationale Abfragesprachen#2. $ sigma$ ist kommutativ|2]],  [[Relationale Abfragesprachen#4. Vertauschen von $ sigma$ und $ pi$ Falls $ theta$ sich nur auf die Attribute $A_{1}, dotso,A_{n}$ von $ pi$ bezieht|4]],  [[Relationale Abfragesprachen#6. Vertauschen von $ sigma$ mit $ bowtie$|6]] werden Selektionsoperationen soweit nach unten propagiert wie möglich
3. Join-Ersetzung: Mittels  [[Relationale Abfragesprachen#12. Join Ersetzung|Regel 12]] wird eine $\times$-Operation, die von einer $\sigma$ Operation gefolgt wird, in eine Join-Operation umgewandelt
4. Projektions-Pushdown: Mittels Regeln  [[Relationale Abfragesprachen#3. $ pi-$Kaskaden Falls $L_{1} subseteq L_{2} subseteq dotso subseteq L_{n}$|3]],  [[Relationale Abfragesprachen#4. Vertauschen von $ sigma$ und $ pi$ Falls $ theta$ sich nur auf die Attribute $A_{1}, dotso,A_{n}$ von $ pi$ bezieht|4]],  [[Relationale Abfragesprachen#7. Vertauschung von $ pi$ mit $ bowtie$|7]] und  [[Relationale Abfragesprachen#10. Die Operation $ pi$ ist distributiv mit $ cup$|10]] werden Projektionen soweit wie möglich nach unten propagiert
5. Zusammenfassung: Versuche Operationsfolgen gleicher Operatoren wieder zusammenzufassen (Anwendung von Regel  [[Relationale Abfragesprachen#1. Aufbrechen von Konjunktionen im Selektionsprädikat|1]] und  [[Relationale Abfragesprachen#3. $ pi-$Kaskaden Falls $L_{1} subseteq L_{2} subseteq dotso subseteq L_{n}$|3]])
## Kosten-basierte Optimierung
Die kosten-basierte Optimierung verwendet ein Kostenmodell(zur Schätzung der Laufzeit), um einen "schnellen" Plan auszuwählen. Die Kosten eins Plans sind dabei abhängig von den [[Daten]] in der Datenbank.
Der Ablauf der kosten-basierten Optimierung ist in 2 Phasen:
1. Auswahl einer optimalen Join-Reihenfolge
2. Auswahl von "physischen Operatoren" für jeden logischen Operator (z.B. Hash-basiert oder Nested-Loop-basierter Join)
### Auswahl optimaler Join-Reihenfolge
Bei einem einfachen Kostenmodell verwenden wir die Größe der Zwischenergebnisse um die Kosten abzuschätzen. Dafür brauchen wir die Tabellengrößen und auch Beschaffenheiten am Anfang der Tabellen um damit die Ergebnisgrößen Bottom-Up abzuschätzen.
Die Zwischenergebnisgrößen Schätzen wir mit der "Selektivität" eines Operators, also wieviel Prozent der Daten nach der Anwendung dessen noch vorhanden sind.
#### Selektivität des Selektionsoperators $\sigma_{p}$
$$sel(\sigma_{p}(R)) = \frac{|\sigma_{p}(R)|}{|R|}$$
#### Abschätzung der Selektivität der Selektion $\sigma$
$$sel(\sigma_{A=Konstante}(R)) = \frac{1}{|A|}$$
$$sel(\sigma_{A=B}(R)) = \frac{1}{\max(|A|,|B|)}$$
Hierbei wird von einer Gleichverteilung und eine
r statistischen Unabhängigkeit ausgegangen.
#### Komplexere Prädikate mit AND und OR
$$sel(\sigma_{p_{1}\text{ AND }p_{2}}(R)) = sel(\sigma_{p_{1}}(R))*sel(\sigma_{p_{2}}(R))$$
$$sel(\sigma_{p_{1}\text{ OR }p_{2}}(R)) = sel(\sigma_{p_{1}}(R))+sel(\sigma_{p_{2}}(R))-sel(\sigma_{p_{1}}(R))*sel(\sigma_{p_{2}}(R))$$
#### Selektivität des Join-Operators $\bowtie$
$$sel(R \bowtie S) = \frac{|R \bowtie S|}{|R \times S|}$$
#### Abschätzung der Selektivität des Joins
Join über Fremdschlüssel:
$$sel(R \bowtie_{R.A = S.B} S) = \frac{|S|}{|R \times S|}$$
Join über normale Attribute:
$$sel(R \bowtie_{A=B}) = \frac{1}{\max(|A|,|B|)}$$
### Alternativen zur Selektivitätsberechnung
#### Stichprobenverfahren
Berechne Selektivität für eine Stichprobe und Verallgemeienre auf gesamte Eingabe
#### Histogramme
Vereinfachte Häufigkeitsverteilung meist auf einem Attribut, an dem man die relative Häufigkeit dieser Teilbereiche berechnen kann
#### Parametrisierte Verteilung(Synopsen)
Hierbei wird eine Annahme über die Verteilung gemacht( z.B. dass sie eine Normalverteilung hat) und dann verwenden wir die geschlossene Formel für die Verteilung um die Selektivität zu berechenen.
## Links

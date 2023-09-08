---
aliases: 
---
# Anfrageverarbeitung 
[[Anfragesprache SQL|SQL]]-Anfragen werden zuerst in einen [[Relationale Abfragesprachen|Logischen Plan]] umgewandelt und dann optimiert. Diese Optimierung läuft in unterschiedlichen Phasen ab. 
Zuerst Optimieren wir regelbasiert, dann kostenbasiert und zum Schluss können wir uns noch für verschiedene physische Pläne entscheiden, bei denen dann unterschiedliche konkrete Algorithmen zur Ausführung ausgewählt werden.
Das Ziel dabei ist einen Effizienten Ausführungsplan für eine Anfrage zu finden(idR bezogen auf die Minimierung der Ausführungszeit)
## Regel-basierte Optimierung
Die Regel-basierte Optimierung verwendet einen Regelsatz, um einen logischen Ausführungsplan umzuschreiben. Diese Regeln sind dabei unabhängig von den [[Daten]] in der Datenbank.
Wir verwenden die [[Relationale Abfragesprachen#Äquivalenzen der Relationalen Algebra|Äquivalenzen der relationalen Algebra]] zum Umformen:
1. Mittels  [[Relationale Abfragesprachen#1. Aufbrechen von Konjunktionen im Selektionsprädikat|Regel 1]] werden konjuktive Selektionsprädikate in Kaskaden von $\sigma$ Operationen zerlegt
2. Selektions-Pushdown: Mittels Regeln  [[Relationale Abfragesprachen#2. $ sigma$ ist kommutativ|2]],  [[Relationale Abfragesprachen#4. Vertauschen von $ sigma$ und $ pi$ Falls $ theta$ sich nur auf die Attribute $A_{1}, dotso,A_{n}$ von $ pi$ bezieht|4]],  [[Relationale Abfragesprachen#6. Vertauschen von $ sigma$ mit $ bowtie$|6]] werden Selektionsoperationen soweit nach unten propagiert wie möglich
3. Join-Ersetzung: Mittels  [[Relationale Abfragesprachen#12. Join Ersetzung|Regel 12]] wird eine $\times$-Operation, die von einer $\sigma$ Operation gefolgt wird, in eine Join-Operation umgewandelt
4. Projektions-Pushdown: Mittels Regeln  [[Relationale Abfragesprachen#3. $ pi-$Kaskaden Falls $L_{1} subseteq L_{2} subseteq dotso subseteq L_{n}$|3]],  [[Relationale Abfragesprachen#4. Vertauschen von $ sigma$ und $ pi$ Falls $ theta$ sich nur auf die Attribute $A_{1}, dotso,A_{n}$ von $ pi$ bezieht|4]],  [[Relationale Abfragesprachen#7. Vertauschung von $ pi$ mit $ bowtie$|7]] und  [[Relationale Abfragesprachen#10. Die Operation $ pi$ ist distributiv mit $ cup$|10]] werden Projektionen soweit wie möglich nach unten propagiert
5. Zusammenfassung: Versuche Operationsfolgen gleicher Operatoren wieder zusammenzufassen (Anwendung von )
## Kosten-basierte Optimierung
Die kosten-basierte Optimierung verwendet ein Kostenmodell(zur Schätzung der Laufzeit), um einen "schnellen" Plan auszuwählen. Die Kosten eins Plans sind dabei abhängig von den [[Daten]] in der Datenbank.
## Links
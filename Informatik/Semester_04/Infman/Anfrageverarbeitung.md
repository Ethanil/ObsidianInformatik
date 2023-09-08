---
aliases: 
---
# Anfrageverarbeitung 
[[Anfragesprache SQL|SQL]]-Anfragen werden zuerst in einen [[Relationale Abfragesprachen|Logischen Plan]] umgewandelt und dann optimiert. Diese Optimierung läuft in unterschiedlichen Phasen ab. 
Zuerst Optimieren wir regelbasiert, dann kostenbasiert und zum Schluss können wir uns noch für verschiedene physische Pläne entscheiden, bei denen dann unterschiedliche konkrete Algorithmen zur Ausführung ausgewählt werden.
Das Ziel dabei ist einen Effizienten Ausführungsplan für eine Anfrage zu finden(idR bezogen auf die Minimierung der Ausführungszeit)
## Regel-basierte Optimierung
Die Regel-basierte Optimierung verwendet einen Regelsatz, um einen logischen Ausführungsplan umzuschreiben. Diese Regeln sind dabei unabhängig von den [[Daten]] in der Datenbank.
## Kosten-basierte Optimierung
Die kosten-basierte Optimierung verwendet ein Kostenmodell(zur Schätzung der Laufzeit), um einen "schnellen" Plan auszuwählen. Die Kosten eins Plans sind dabei abhängig von den [[Daten]] in der Datenbank.
## Links
---
aliases: 
---
# 3NF Synthesealgorithmus 
Dieser Synthesealgorithmus dient zur Zerlegung einer Relation eines Relationsschemas in [[Normalformen#Dritte Normalform 3NF|3NF]].

1. Bestimme die "kanonische Überdeckung" aller [[Funktionale Abhängigkeit|FDs]] in $R$
	1. Linksreduktion (Linke Seite einer FD verkleinern)
		- Überprüfe für $\alpha \rightarrow \beta$ ob $\beta \subseteq \text{Attributshülle}(\alpha-X)^{+}$ wobei $X \in \alpha$, wenn ja entferne Attribut $X$ aus FD
	2. Rechtsreduktion (Rechte Seite einer FD verkleinern)
		- Überprüfe für alle $B \in \beta$, ob $B \in \alpha^{+}$ mit $F-(\alpha \rightarrow \beta)\cup(\alpha \rightarrow(\beta-B))$, falls dies der Fall ist, dann ersetzte $\alpha \rightarrow \beta$ druch $\alpha \rightarrow(\beta-B)$
	3. Entfernung von FDs der Form $\alpha \rightarrow \emptyset$
	4. Zusammenfassung gleicher linker Seiten
2. Erzeuge neue kleinere Relationen für R
	1. Erzeuge für jede funktionale Abhängigkeit $\alpha \rightarrow \beta$ ein Relationsschema
	2. Weise die FDs den Relationsschemata zu
3. Überprüfe ob ein Schlüsselkandidat erhalten bleibt
	1. Falls eines der Attribute einen Schlüsselkandidaten vollständig erhält sind wir fertig, ansonsten erschaffen wir ein neues Schema mit $R_{k}:=\{k\}$ wobei $k$ ein Schlüsselkandidat ist
4. Fasse kleinere Schemata mit anderen Schemata zusammen
	1. Entferne diejenigen Relationsschemata $R$ die in einem anderen Schema $R'$ komplett erhalten sind

## Links
---
aliases: 
---
# Normalformen 
Durch [[Normalisierung]] erhalten wir ein [[Relationales Datenmodell#Schema R|Schema]] in einer höheren Normalform
## Erste Normalform 1NF
Eine Relation ist in 1NF wenn alle Attributwerte ***atomar*** sind.
## Zweite Normalform 2NF
Eine Relation ist in 2NF, wenn sie in 1NF ist und alle [[Nichtprimattribut|Nichtprimattribute]] [[Funktionale Abhängigkeit#Volle funktionale Abhängigkeit|vollständig]] von jedem [[Relationales Datenmodell#Schlüsselkandidat|Schlüsselkandidaten]] [[Funktionale Abhängigkeit#Volle funktionale Abhängigkeit|abhängen]]:
$\forall A \in NPA(R). \forall K \in KEYS(R). K \rightarrow A$ ist FD in der $A$ voll von $K$ abhängig ist.
## Dritte Normalform 3NF
Eine Relation ist in 3NF, wenn sie in 2NF ist und alle [[Nichtprimattribut|Nichtprimattribute]] nicht [[Funktionale Abhängigkeit#Transitive Abhängigkeiten|transitiv]] von einem [[Relationales Datenmodell#Schlüsselkandidat|Schlüsselkandidaten]] [[Funktionale Abhängigkeit#Transitive Abhängigkeiten|abhängen]]:
Um eine Relation von 2NF in 3NF zu überführen verwenden wir den [[3NF Synthesealgorithmus]].
## Links
---
aliases: 
---
# Normalformen 
Durch [[Normalisierung]] erhalten wir ein [[Relationales Datenmodell#Schema R|Schema]] in einer höheren Normalform
## Erste Normalform 1NF
Eine Relation ist in 1NF wenn alle Attributwerte ***atomar*** sind.
## Zweite Normalform 2NF
Eine Relation ist in 2NF, wenn sie in 1NF ist und alle [[Nichtprimattribut|Nichtprimattribute]] vollständig von jedem [[Relationales Datenmodell#Schlüsselkandidat|Schlüsselkandidatem]] [[Funktionale Abhängigkeit#Volle funktionale Abhängigkeit|abhängen]]:
$\forall A \in NPA(R). \forall K \in KEYS(R). K \rightarrow A$ ist FD in der $A$ voll von $K$ abhängig ist.
## Links
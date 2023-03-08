---
aliases: 
---
# Einführung in die formale Modellierung 
## Beispiel Mann, Wolf, Ziege, Kohlkopf
- Objekte: $O=\{m,w,z,k\}$
- Aspekte: $(L,R) \in P(O) \times P(O)$
- Beschränkungen: $Z:= \{(L,R) \in P(O) \times P(O) | L \cap R = \emptyset \land \{m,w\} \subseteq L \cup R\}$
- Anfangszustand: $(\{m,w,z,k\},\emptyset) \in (L,R)$
- Aktion Beschränkungen: 
	- $T \subseteq O = \{m,w,z,k\}$
	- $E:= \{\text{fahre}(T)|T = \{m\} \lor T=\{m,x\} \land x \in O \backslash \{m\}\}$
- Zustandsübergang: 
	- $\rightarrow \subseteq Z \times E \times Z$
	- $\rightarrow:=\{((L,R),\text{fahre}(T),(L',R') \in Z \times E \times Z)\}$
- Beschränkungen: $T \subseteq L \land L' = L \backslash T \land R' = R \cup T \land (z \notin L' \lor \{w,k\}\cap L' = \emptyset) \lor T \subseteq R \land R' = R \backslash T \land L' = L \cup T \land (z \notin R' \lor \{w,k\} \cap R' = \emptyset)$

## Links
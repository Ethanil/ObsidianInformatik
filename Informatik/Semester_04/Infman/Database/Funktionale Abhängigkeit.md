---
aliases: 
---
# Funktionale Abhängigkeit 
Gegeben sei $R=\{A_{1},\dotso,A_{n}\}$ ein [[Relationales Datenmodell#Schema R|Relationsschema]] mit Attribut-Teilmengen $\alpha$ und $\beta$.
Die Menge $\beta$ ist genau dann von der Menge $\alpha$ ***funktional abhängig*** wenn für jeden Wert aus $\alpha$ genau ein Wert für $\beta$ existiert.
Wenn $\alpha$ von $\beta$ funktional abhängig ist schreiben wir $\alpha \rightarrow \beta$ 

## Schlüsselabhängigkeit
Schlüsselabhängigkeit ist eine spezielle funktionale Abhängigkeit für Schlüsselkandidaten.
Dabei gilt für alle Schlüsselkandidaten $K$ von $R$, dass $K \rightarrow R$ gilt.

## Volle funktionale Abhängigkeit
$\beta$ heißt ***voll funktional Abhängig*** von $\alpha$ genau dann, wenn $\alpha \rightarrow \beta$ gilt und es kein $\alpha'\subset \alpha$ gibt mit $\alpha'\rightarrow \beta$

## Partielle funktionale Abhängigkeit
$\beta$ heißt partiell funktional abhängig von $\alpha$ genau dann, wenn $\beta$ funktional von $\alpha$ ist aber nicht voll funktional abhängig.

## Transitive Abhängigkeiten
Eine Attributsmenge $\beta$ heißt ***transitiv abhängig*** von $\alpha$ genau dann, wenn $\alpha \rightarrow \gamma$ und $\gamma \rightarrow \beta$ [[Funktionale Abhängigkeit#Volle funktionale Abhängigkeit|voll funktional abhängig]] sind, aber $\gamma \rightarrow \alpha$ keine voll funktionale Abhängigkeit ist. 
## Schlüsselkandidaten aus FDs
- Bestimme Attribute, die nicht auf der rechten Seite einer FD vorkommen => diese müssen in jedem Schlüsselkandidaten enthalten sein
- Attributshülle der einzelnen Determinanten und fehlende Attribute der Hülle bestimmen
	- Alle $det \cup fehlt$ sind Superschlüssel
- Minimiere Superschlüssel

## Links
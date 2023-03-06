---
aliases: 
---
# Vorlesung 2 
## Schutzziele
```ad-abstract
title:Definition - Schutzziele
|Name|Beschreibung|
|-----|-----|
|Vetraulichkeit|Schutz vor unbefugtem Zugriff auf Informationen / Daten|
|Integrität|Schutz vor Veränderung von Informationen / Daten|
|Verfügbarkeit|Daten oder Systeme sind verfügbar oder erreichbarn|
|Authentizität|Schutz vor Fälschungen von Informationen / Daten|
|Nicht-Abstreitbarkeit|Aktion ist nachprüfbar und kann nicht abgestritten werden|

```
## Kerckhoffs Prinzipien
1. Das System muss praktisch, wenn nicht sogar mathematisch, unentschlüsselbar sein.
2. Es darf keine Geheimhaltung erfordern und darf ohne Schwierigkeiten in die Hände des Feindes fallen.
3. Der Schlüssel muss ohne Hilfe geschriebener Notizen kommunizierbar und aufbewahrbar sein und er muss ausgewechselt oder modifiziert werden können nach Belieben der Kommunikationspartner.
4. Es muss anwendbar sein auf die telegraphische Kommunikation.
5. Es soll portabel sein und seine Funktion soll nicht die Zusammenkunft mehrerer Personen erfordern.
6. Schließlich ist es notwendig, angesichts der Umstände, unter denen es angewendet werden soll, dass das System einfach benutzbar ist und weder große gedankliche Anstrengung erfordert noch die Kenntnis einer langen Liste zu beachtender Regeln.
## Angriffe auf Kryptosystem
```ad-abstract
title:Definition - 
|Abkürzung|Bedeutung|Beschreibung|
|----|----|----|
|COA|ciphertext-only-attack oder known-chipertext attack|Der Angreifer kennt Chiffretexte|
|KPA|known-plaintext attack|Angreifer kennt Klartext + Chiffrate|
|CPA|chosen-plaintext attack|Angreifer kann Klartexte seine Wahl verschlüsseln lassen|
|CCA|chosen-chipertext attack|Angreifer kann Chiffrate seiner Wahl entschlüsseln und enthält somit die zugehörigen Klartexte erhalten.|
```
## Teilbarkeit, Zeug für Beweise
```ad-abstract
title:Definition - Eigenschaften von Teilbarkeit
$$\begin{align}
a|b &\land b|c &\Rightarrow a|c \\
a|b &\land b \neq 0 &\Rightarrow |a| \leq |b| \\
a|b &\land b|a &\Rightarrow |a| = |b| \\
a|b &\land b|c &\Rightarrow a|c
\end{align}$$
```

```ad-abstract
title:Definition - Euklid
$ggT(a,b) = k*a+l*b$

| a     | b   | $\lfloor\frac{a}{b}\rfloor$ | k    | l      |
|---|---|---|---|---|

$i \in [1..j]: j = \text{Anzahl Iterationen des Euklid}$

unterstes $k_{j} = 1$ $l_{j}=0$

$k_{i-1}=l_{i}$ und $l_{i-1} = k_{i} - \lfloor\frac{a}{b}\rfloor_{i-1} * l_{i}$
```

```ad-abstract
title:Definition - Lemma von Euklid
Es gilt für eine Primzahl $p$
$$p|ab \Rightarrow p|a \lor p|b$$
```

```ad-abstract
title:Definition - lineare Diophantische Gleichung
$$\begin{align}
a,b,c,x,y \in \mathbb{Z} \\
a*x + b*y &= c = ggT(a,b) \Leftrightarrow ggT(a,b)|c \\
\end{align}$$
```
## Links
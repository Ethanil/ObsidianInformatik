Die [[Segmentierung|segmentierten]] Bereiche wollen wir in Objektklassen einteilen.

Das Ziel der Klassifikation ist die Interpretation des Bildinhaltes, also ein "intelligenter" Prozess.

## Ablauf der Klassifizierung
1. Wir erstellen ein "Mehrkanaliges" Bild (Merkmalsvektor) $S = (g_{1}, \dotso, g_{n})$, Stichprobe
2. Wir wählen Merkmale aus
	1. Kleinste Anzahl, die voneinander unabhängig sind
	2. Durch die Merkmale muss eine Klassenzuordnung ermöglicht werden
	3. Ggf müssen die Merkmale normiert bzw normierbar sein
3. Danach definiere
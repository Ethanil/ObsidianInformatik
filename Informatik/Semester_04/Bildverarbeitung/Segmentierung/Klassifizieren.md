Die [[Segmentierung|segmentierten]] Bereiche wollen wir in Objektklassen einteilen.

Das Ziel der Klassifikation ist die Interpretation des Bildinhaltes, also ein "intelligenter" Prozess.

## Ablauf der Klassifizierung
1. Wir erstellen ein "Mehrkanaliges" Bild (Merkmalsvektor) $S = (g_{1}, \dotso, g_{n})$, Stichprobe
2. Wir wählen Merkmale aus
	1. Kleinste Anzahl, die voneinander unabhängig sind
	2. Durch die Merkmale muss eine Klassenzuordnung ermöglicht werden
	3. Ggf müssen die Merkmale normiert bzw normierbar sein
3. Danach definieren wir Klassen
	1. Anhand von objektiven Kriterien, wählen wir Klassen sinnvoll aus
	2. Die Klassen müssen gut voneinander trennbar sein(also keine fließenden Grenzen haben)
	3. Die Klassen sollten jeden Bereich des Merkmalsraumes abdecken
	4. Ich benötige eine Stichprobe, bei der in $n$-Beobachtungen Häufungen bzw Muster im Merkmalsraum entstanden sind
4. Wir bestimmen die Klassengrenzen, also dimensionieren die Kassen bspw durch Segmentierung/Unterilung des Merkmalsraumes
5. Wir wählen eine Zuordnungsmethode, die einen Vektor einer Klasse zuordnet

![[Pasted image 20231001161303.png# 5/6 left shadow|Der Klassifizierungsvorgang]]
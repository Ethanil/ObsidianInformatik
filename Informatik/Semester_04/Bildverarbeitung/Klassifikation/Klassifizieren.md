Die [[Segmentierung|segmentierten]] Bereiche wollen wir in Objektklassen einteilen.

Das Ziel der Klassifikation ist die Interpretation des Bildinhaltes, also ein "intelligenter" Prozess.

## Ansätze der Klassifikation
### Syntaktisch
Dinge werden so durch Folgen von Symbolen beschrieben, dass Objekte der gleichen Kategorie die selben Beschreibungen aufweisen. Das Problem der Mustererkennung stellt sich in diesem Fall als Suche nach einer formalen Grammatik dar, also nach einer Menge von Symbolen und Regeln zum Zusammenfügen derselben
### Statistisch
Ziel ist es hier, ein Objekt in die Kategorie mit der höchsten Wahrscheinlichkeit einzusortieren. Statt Merkmale nach vorgefertigten Regeln auszuwerten, werden sie hier einfach als Zahlenwerte gemessen und in einem Merkmalsvektor zusammengefasst. Eine mathematische Funktion ordnet dann jedem denkbaren Merkmalsvektor eindeutig eine Kategorie zu.
### Strukturell
verbindet verschiedene sytnatkische und/oder statistische Verfahren zu einem einzigen neuen Verfahren. Die grundlegende Merkmalserkennung wird dabei allgemeinen statistischen Verfahren überlassen, während übergeordnete Inferenzverfahren Spezielwissen über das Sachgebiet einbringen.

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
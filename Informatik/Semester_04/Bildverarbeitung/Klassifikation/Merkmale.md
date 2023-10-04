Wir wollen die kleinste, voneinander unabhängige Anzahl an Merkmalen finden, die eine Klassenzuordnung ermöglichen und gegebenenfalls normiert/normierbar sind.

Wenn die Merkmale Symbolisch sind, also Mitglieder eines endlichen Alphabets, dann verwenden wir syntaktische Klassifikatoren.
Wenn die Merkmale numerisch sind, also in (reelle oder komplexe) Zahlen zu erfassende "Vektoren" sind, dann verwenden wir numerische Klassifikatoren
## Auswahl
Wir können Merkmale entweder heuristisch, also durch Intuition, Erfahrung oder Beobachtung oder analytisch, gewinnen.
Das heuristische Vorgehen ist dabei oft mangelhaft, insignifikant oder wenig aussagefähig und das analytische wählt somit die "optimalen" Merkmale bezüglich eines Kriteriums aus.
### Heuristisch
Nach einem Preprocessing extrahieren wir Merkmale anhand derer wir eine [[Klassifizieren|Klassifikation]] vornehmen können.
### Analytisch
Wir wählen $M$ Merkmale aus, welche ein Kriterium am besten optimieren. Dabei unterscheiden wir grundsätzlich zwei Arten von Kriterien
1. Trennbarkeit von Klassen, Gruppierung von Merkmalen
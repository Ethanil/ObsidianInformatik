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
#### Trennbarkeit von Klassen, Gruppierung von Merkmalen
Wir versuchen die Merkmalsmenge so klein wie möglich zu halten, allerdings ist der Abstand der Clustermittelpunkte allein noch kein ausreichendes Kriterium.

#### Klassifikationsfehlwahrscheinlichkeit, also die Streuung des Merkmalswertes
Theoretisch ist es sinnvoll die Fehlwahrscheinlichkeit zu minimieren um eine Zuordnung zu der Klasse mit höchster a-posteriori Wahrscheinlichkeit zu gewährleisten. Dafür verwenden wir den optimalen Bayes-Abstand.
Das Problem hierbei sind bedingte Dichten $p(x|C_{i})$ ist idR unbekannt, darum haben wir nur eine Näherung über die Stichprobe.
### Strategien zur Auswahl
1. Jedes Merkmal wird alleine bewertet und wir wählen die $N$ besten aus
2. Erst das bestbewerteste Merkmal wird ausgewählt, dann eine Tupel-Kombination aus Merkmalen
3. Zuerst zwei schlechteste zu trennende Klassen ermitteln, dafür Merkmale auswählen die zur Trennung optimal beitragen
4. Erst Klassifizieren wird mit allen Merkmalen und lassen dann immer mehr Merkmale weg, bis eine optimale Kombination erreicht wird

Die Auswertung heuristischer Merkmale ist aufwendig, daher ist es besser eine Bewertung durch Lagebeurteilung der Vektoren im Merkmalsraum auszuführen.
Wir brauchen objektive Kriterien, die eine sinnvolle Auswahl von Klassen erlauben, diese sollen gut trennbar sein und keine fließenden Grenzen haben.
## Auswahl der Klassen & -grenzen
Wir müssen Punktewolken(Cluster) im Merkmalsraum ermitteln, also wieviele und wo ihr jeweiliger Mittelpunkt liegt. Wir müssen die Cluster voneinander abgrenzen. Richtig gewählte [[Merkmale]] führen zu (einigermaßen) zusammenhängenden Clustern, aber wie bestimmen wir die Anzahl und Grenzen der Cluster?

### [[Stichprobe|Stichproben-Strategie]]
Wir können entweder überwachte oder unüberwachte Stichproben haben. Damit haben wir zusammen mit der Dimensionierung der Stichproben 4 Möglichkeiten.
### Fest-Dimensionierte überwachte Strategie
Wir benötigen eine Stichprobe bekannter Objekte, bei denen Musterklassen eindeutig durch die Stichprobe festgelegt ist und die Wahrscheinlichkeiten a-priori bekannt sind/gemessen wurden.
#### Probleme
Die Stichprobe ist immer nur eine Approximation einer Klasse. Das heißt bei einer nicht repräsentativen Stichprobe haben wir auch die Klassen nicht gut modeliert. Siehe [[Stichprobe#Probleme bei der Stichprobe]]
Unsere Dimensionierung ist statisch, wir haben also eine Feste Anzahl an Klassen mit festen Grenzen.
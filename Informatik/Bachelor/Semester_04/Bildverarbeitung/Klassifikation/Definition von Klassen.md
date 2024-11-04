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

### Fest-Dimensioniert unüberwachte Stategie
Hier haben wir zwar eine feste Menge an Trainigsvektoren, aber die Anzahl der Klassen und die Klassengrenzen sind nicht bekannt, das heißt beides wird während der Klassifikation generiert durch [[Clustering]].
Dadurch ist eine Stichprobe einfache und weniger anfällig, die Grenzen sind flexibler und es ist Re-clustering möglich(also eine dynamische Dimensionierung)

### Lernende Strategien
Es ist nicht unüblich, dass sich Stichproben mit der Zeit verändern, darauf können wir mit Fest-Dimensionerten Stichproben nicht reagieren. Eine Lösung dafür ist es lernende Stichproben zu verwenden, die bspw eine Trenderkennung durch Rückkopplung erhalten. Dabei wir jeder Sample neu klassifiziert und der Trainingsmenge zugeführt, was zu einer Erweiterung führt. Wir erhalten dann eine neudefinition von Klassengrenzen (bei überwachten Stichproben) oder auch der Klassenazahl (bei unüberwachten Stichproben)
#### Überwacht
Die erstdimensionierung wird durch eine bekannte Stichprobe und einer festgelegten Menge an Klassen gemacht. Jede Probe wird klassifiziert und zur Stichprobe zugeführt, wordurch die Stichprobe erweitert wird, da nach jeder Klassifikation auch eine re-Dimensionierung der Klassengrenzen stattfindet.

![[Pasted image 20231005014908.png# 2/3 left shadow|Die Stichprobe wird verbessert, indem ihr die Merkmalsvektoren zugeführt werden]]
#### Unüberwacht(Train-on-the-job)
Wir haben eine sich erweiternde Stichprobe, anhand derer die Anzahl **und** die Grenzen der Klassen dynamisch durch [[Clustering]] festgelegt werden. Wir legen nur die Kriterien(z.B. Schwellen) für die Vereinigung/Trennung von Clustern fest.

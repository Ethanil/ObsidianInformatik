## Geometrisch
Wir ordnen den Vektor derjenigen Klasse zu, welche "am nahesten" zu dem Sample liegt (nearest neighbour)
### Metrik
#### Manhatten(City-Block)
Die Summe der absoluten Differenzen
$$d(x,y) = L_{1}(x,y) = \sum^{n}_{i=1}|x_{i}-y_{i}|$$
#### Euklidisch
Die Wurzel aus der Summe der quadratischen Differenzen
$$d(x,y) = L_{2}(x,y) = \sqrt{\sum^{n}_{i=1}(x_{i}-y_{i})^{2}}$$
#### Quadratrisch Euklidisch
Summe der quadratischen Differenzen
$$d(x,y) = L_{3}=\sum^{n}_{i=1}(x_{i}-y_{i})^{2}$$

Mit dieser Metrik vergleichen wir das Sample dann entweder mit einem Cluster-Vetreter (Mittelwert, Schwerpunkt, Median, häufigster Wert) oder mit mehreren Cluster-Elementen([[Nearest-Neighbour|nächster klassifizierter Nachbar]] oder [[K-Nearest-Neighbour|Mehrheit von mehreren klassifizierten Nachbarn]]).
Das vergleichen mit einem Cluster-Vertreter funktioniert gut, wenn die Cluster kompakt sind, es also eine geringe Streuung mit glatten Grenzen gibt.
![[Pasted image 20231005021728.png# 2/3 left shadow|Wenn wir nur den nächsten Nachbar betrachten, würde das Sample zu einem Kreis gemacht werden, bei 9 Nachbarn wird es eindeutig als Quadrat eingeordnet]]
## Statistisch
Wir ordnen den Vektor derjenigen Klasse zu, zu der der Sample "am wahrscheinlichsten" gehört (maximum likelyhood)
Bei der statistischen Zuordnungsstrategie betrachten wir wie Wahrscheinlich es ist, dass das sample zu einer Klasse gehört und gleichzeitig, wenn es denn zu der Klasse gehört, die Eigenschaften hat, die es hat. Dies machen wir für alle Klassen und ordnen das sample dann der Klasse zu, bei der die größte Wahrscheinlichkeit entstanden ist:
$$\begin{align*}
p(C_{i})&&\text{Wahrscheinlichkeit, dass das Sample der Klasse }C_{i}\text{ angehört}\\
p(x|C_{i})&&\text{Wahrscheinlichkeit, dass das Sample die Eigenschaft $x$ hat, unter der Bedingung, dass es die Klasse $C_{i}$ hat}\\
p(C_{i})\cdot p(x|C_{i})&&\text{Likelyhood für die Zugehörigkeit von einem Sample mit den Eigenschaften $x$ zur Klassen $C_{i}$}
\end{align*}$$
Diese Wahrscheinlichkeiten müssen dabei a-priori bekannt sein. $p(C_{i})$ ist einfach zu erhalten, allerdings ist $p(x|C_{i})$ schwer zu erhalten, daher nehmen wir eine Gaus'sche Verteilung an.

## Ursachen für Fehlklassifikation
Es kann zu Fehlklassifikation kommen, wenn Klassen sich überschneiden, also fließende Grenzen haben, wie beispielsweise Farben, hierbei können unter Umständen fuzzy Klassifikationsverfahren helfen.
Zu wenige oder nicht hinreichend signifikante Merkmale könne auch Fehlklassifikationen zur Folge haben, da sie zu zufälligen Ergebnissen führen.
Messfehler bei der [[Merkmalsextraktion]] kann zu Fehlklassifikation führen.
Unzureichendes Training eines Lernverfahrens (bpsw. [[Clustering]]) kann zur Fehlklassifikation führen.
Ein ungeeigneter Trainingsdatensatz kann zur Fehlklassifikation führen, wenn beispielsweise die [[Stichprobe]] nicht repräsentativ für die Klassen ist.
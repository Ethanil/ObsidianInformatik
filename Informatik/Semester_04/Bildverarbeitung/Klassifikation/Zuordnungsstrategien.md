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
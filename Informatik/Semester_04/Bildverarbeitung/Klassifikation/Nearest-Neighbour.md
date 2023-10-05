Ist geeignet für irreguläre Cluster, die beispielsweise eine große Streuung, eine unrunde Form oder mehrere Ballungsanhäufungen im Merkmalsraum haben.
Für jedes Sample vergleichen wir in jedem Cluster das Sample mit jedem Vertreter dieses Clusters.

- Wir berechnen die Distanzen des Samples zu allen Vertretern des Clusters
- Wir setzen die Distanz auf die geringste Distanz zu einem Vertreter
- Wir ordnen das Sample zum Cluster mit der insgesamt kleinsten Distanz zu
- Falls es über einer Schwelle liegt, weisen wir das Cluster zu Zurückweisungsklasse zu

Dies führt gegebenfalls zu einem "Phantom-Cluster" falls es outliers gibt, um dies zu verhindern können wir [[K-Nearest-Neighbour]] verwenden

Nearest Neighbour kann verwendet werden, um eine [[Definition von Klassen#Lernende Strategien|lernende]] [[Zuordnungsstrategien]] zu implementieren.
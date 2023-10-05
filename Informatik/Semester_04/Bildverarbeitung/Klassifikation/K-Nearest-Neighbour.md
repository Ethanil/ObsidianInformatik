Wir berechnen alle Distanzen, wie bei [[Nearest-Neighbour]]. Wir bestimmen die $k$ nächsten Nachbarn zum Sample (mit einem ungeraden $k$). Wir verwenden eine Mehrheitsentscheidung, welcher Klasse das sample zugeordnet wird.

Bei einem kleinen $k$ berücksichtigen wir nur nahe Klassen, bei einem großen $k$ auch ferne Klassen.

Wir können dieses Verfahren eventuell erweitern, indem wir nähere Nachbarn mehr gewichten (bspw mit [[Zuordnungsstrategien#Quadratrisch Euklidisch]])
Dieses Verfahren ist wesentlich robuster gegenüber outliern, als [[Nearest-Neighbour]], was $k=1$ entspricht.

K-Nearest Neighbour kann verwendet werden, um eine lernende [[Zuordnungsstrategien]] zu implementieren.
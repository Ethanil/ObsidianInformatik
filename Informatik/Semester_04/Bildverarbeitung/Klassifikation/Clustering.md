## K-Means (minimum distance) Clustering
1. Initialie Generierung von (zufällige, beliebigen oder vordefinierten) Clustern
2. Für jeden Sample der Stichprobe berechenen wir die Distanz zu allen Clustern
3. Wir Ordnen jedes Sample zum nächstliegenden Cluster zu, also zur kleinsten Distanz, falls diese kleiner als $S_{1}$ ist
4. Wir bewerten die Clusteranzahl, -Grenzen und -Schwerpunkte neu:
	- Wenn Vektoren zu keinem Cluster gehören(also weiter als $S_{1}$ von allen Clustern entfernt sind), dann erschaffen wir ein neues Cluster
	- Wenn Cluster sich zu nahe kommen (kleiner als $S_{2}$), dann werden sie vereinigt
	- Wenn Cluster zu groß werden (größer als $S_{3}$), dann können sie geteilt werden
	- Wir berechnen die Schwerpunkte neu
5. Wir Ordnen alle Vektoren den Clustern erneut zu
6. Wir berechnen die Summe der Distanzmaße für jeden Cluster
7. Wir fangen bei 3 wieder an, bis 6 minimiert wurde

![[Pasted image 20231005011512.png# 5/6 left shadow|Nach 3 Iterationen haben wir einen steady state erreicht, obwohl wir mit schlechten Start-Clustern begonnen haben]]
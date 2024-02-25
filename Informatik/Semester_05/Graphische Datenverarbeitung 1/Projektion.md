---
aliases: 
---
Siehe [[Transformation#Affine Unterräume]] und [[Transformation#Position durch Transformation]].
# Projektiver Raum
Ein projektiver Raum ist die Menge aller 1-dimensionaler Unterräume $P(V)=\{U:U=\{t v\}:v \text{ aus }V\backslash\{0\}\}$ eines Vektorraums $V$
## Einbettung
Wir können einen Vektorraum, also bspw $\mathbb{R}^3$ in einen Projektiven Raum mit einer 1 höheren Dimension einbetten, also dann $\mathbb{R}^4$.
Die Abbildung von $\mathbb{R}^3$ nach $P(\mathbb{R}^4)$, festgelegt durch $(x,y,z)^{T}\rightarrow[x,y,z,1]^{T}$ ordnet jedem Punkt im $\mathbb{R}^{3}$ einen projektiven Punkt von $P(\mathbb{R}^{4})$ zu.
Jeder Punkt $(x,y,z)^{T}$ in $\mathbb{R}^{3}$ ist also eine Urpsrungsgerade in $\mathbb{R}^{4}$ durch $(x,y,z,1)^{T}$.
Umgekehrt ist jedem Projektiven Punkt $(x,y,z,w)^{T}$ aus $P(\mathbb{R}^{4})$ mit $w \neq 0$ ein Punkt im $\mathbb{R}^{3}$ wie folgt zugeordnet: $[x,y,z,w]^{T}\rightarrow(\frac{x}{w},\frac{y}{w},\frac{z}{w})^{T}$ 
## Projektive Fernpunkte
Mit der Abbildung wie in [[Projektion#Einbettung]] sind die Punkte der Form $[x,y,z,0]^{T}$ projektive Fernpunkte, die als unendlich ferne Punkte in $\mathbb{R}^{3}$ interpretiert werden.
 
## Links
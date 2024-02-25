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
 
# Projektion
Bei einer Projektion(Projektiven Abbildung):
- Geraden bleiben Geraden
- Schnitte von Geraden bleiben erhalten
- Flächen bleiben Flächen
- Reihenfolge von Punkten auf Geraden bleiben gleich

- Winkel werden verändert
- Parallelität geht verloren(Schneiden sich in Fluchtpunkten)
- Rechtecke werden auf Vierecke transformiert
- Fernpunkte werden zu endlichen Fluchtpunkten
## Parallele Projektion
![[Pasted image 20240225125241.png# shadow float right 1/2]]
Die Parellele Projektion ist eine Projektion des sichtbaren Volumens in den "Einheitswürfel", also eine Translation gefolgt von einer Skalierung
## Perspektivische Projektion
![[Pasted image 20240225125459.png# shadow float right 1/2]]
Perspektivische Projektionen werden druch projektive Abbildungen verwirklicht, da hier anders als bei der Parallen Projektion, affine Abbildungen nicht ausreichen. Vom Blickpunkt weit entfernte Objekte werden kleiner dargestellt, als nahe Objekte. Das Ergebnis ist ein realistischer räumlicher Eindruck, aber keine Längeninvarianz.
Nach der perspektivischen Projektion wird noh eine Trarnsformation auf den Einheitswürfel durchgeführt.
### Sichtbarkeitsbereich
Der Sichtbarkeitsbereich im dreidimensionalen ist ein Pyramidenstumpf bestehend aus 6 Clipping-Ebenen.
## Links
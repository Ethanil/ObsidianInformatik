---
aliases: Norm
---
# Normierte Räume
Mithilfe von normierten Räumen kann man Längen und Abstände in [[Vektorraum|Vektorräumen]] messen. Wir betrachten uns dabei reelle Vektorräume (komplexe sind nahezu analog dazu).
## Norm
Eine Norm ist eine [[Abbildung]] mit folgenden Eigenschaften:
- $\forall v\in V: ||v||\geq 0$ und $(||v||=0\Leftrightarrow v=0)$ ([[Definitheit]])
- $\forall \alpha\in\mathbb{R} \forall v\in V: ||\alpha v|| = |\alpha|||v||$ ([[Homogenität]])
- $\forall v,w\in V: ||c+w||\leq ||v||+||w||$ ([[Dreiecksungleichung]])
Eine Vektorraum mit einer Norm heißt normierter Raum.
## 2-Norm
Der Alltagsbegriff von der Länge ist der Euklidische Abstand:
$$||x||_2:=\sqrt{\sum^n_{j=1}x^2_j}\ \ \ \ x=(x_1,x_2,\dotso,x_n)^T\in \mathbb{R}^n$$
## 1-Norm
Wir betrachten in $\mathbb{R}^2$ die [[Abbildung]] $||\cdot||_1:\mathbb{R}^2\rightarrow \mathbb{R}$ mit
$$||x||_1=\sum^n_{j=1}|x_j|,\ \ \ \ x=(x_1,x_2,\dotso,x_n)^T\in\mathbb{R}^n$$
## Maximums- oder $\infty$-Norm
$$||x||_\infty=max\{|x_1|,|x_2|,\do$$

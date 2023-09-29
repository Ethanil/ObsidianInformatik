Die Hough Transformation ist wie die [[Radon Transformation]] eine paremtrisierte Bildtransformation.
Ihr Ziel ist eine "Globale" Linienerkennung durch das Transformieren des Segementierungsproblems im Bildraum in ein Finden von lokalen Maxima im Parameterraum.

Bei der Hough Transformation schauen wir uns für jeden Punkt im Bild an, zu welchem möglichen Geraden ($\rho = x \cdot\cos(\theta) + y \cdot \sin(\theta)$) dieser gehören könnte und plotten diese möglichen $\rho$ und $\theta$-Werte (alternativ von $y = ax+b$ die möglichen $a$ und $b$ Werte). Wenn in diesem Transformationsraum nun peaks entstehen, ist dies eine mögliche Gerade mit diesem Winkel $\theta$ und der Entfernung vom Ursprung $\rho$.

![[Pasted image 20230929122336.png# 5/6 shadow left|Der Bildraum links mit den 5 Punkten wird in den Hough-Raum rechts transformiert, wobei wir den Peak A finden, der dann als gelbe Gerade links eingezeichnet wurde]]

Die Hough Transformation ist wie die [[Radon Transformation]] auch robust gegenüber unterbrochenen Linien, da der peak zwar verringert wird, aber trotzdem ein peak bleibt.
Bei verrauschten Linien erhalten wir keinen einzelnen peak sondern ein Cluster mit hohen Werten.
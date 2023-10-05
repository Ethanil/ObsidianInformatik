Wir wollen bei [[Machine Learning]] den regularisierten "Loss" über alle Datenpunkte minimieren, indem wir unsere Parameter perfekt einstellen.
$$ \lambda \omega(w) + \frac{1}{m}\sum^{m}_{i=1}l(x_{i},y_{i},w)$$

Die Funktion $l$ ist dabei die loss Funktion und ist unser Anzeiger für Qualität.
Insgesamt nennt man diese Art der Anschauung Risiko, darum versuchen wir dies auch zu minimieren.

Wir wollen unser Parameter $w$ generalisiert an ungesehene Daten anpassen, also nicht für unsere Trainingsdaten overfitten. Dies machen wir indem wir Komplexe Modelle penalisieren.

Dieses Problem verwandeln wir nun in ein [[Konvexe Funktion|konvexes Problem]], da wir auf solche Probleme gute Optimierungsstrategien anwenden können.
Mittels eines reduce Operators wird die obere Hälfte der Anteile des Frequenzspektrums eines Bildes herausgefiltert und das Bild in Zeilen- und Spaltenrichtung gleichzeitig um die Hälfte verkleinert.
Wir haben also eine Tiefpassfilterung und eine Verkleinerung was zu einem Informationsverlust führt.
Wenn man dieses Vorgehen fortsetzt erhält man die Gauß Pyramide.

Um die einzelnen Ebenen dieser Pyramide vergleichen zu können verwenden wir eine expand-Operation um eine Ebene auf die Größe der nächst größeren Ebene zu vergrößern.
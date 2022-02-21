---
aliases: 
---
# Conditional Sum Adder
Wir halbieren die Bits in eine untere und in eine odere Hälfte.
Die untere Hälfte wird ganz normal ausgerechnet und ergibt dann eine Summe und einen Übertrag.
Bei der oberen Hälfte bräuchten wir eigentlich zuerst den Übertrag der unteren Hälfte um es richtig zu berechnen, das würde aber keinen Zeitgewinn bringen.
-> Wir berechnen einfach für die obere Hälfte das Ergebnis für beide Möglichkeiten des Übertrags der unteren Hälfte
-> 50% mehr Hardware, aber sehr viel schneller.
---
aliases: 
---
# Mehrwertige Logik
außer 1en (auf 1 getrieben) oder 0en (auf 0 getrieben) gibt es noch 2 weitere Werte:
## X - mehrfach getrieben:fehlerhaft
Ein X(nicht zu verwechseln mit [[Don't Care|Don't Cares]]!!!) entsteht wenn 2 unabhängige Treiber für den selben Schaltungsknoten existieren. Dabei kommt es zu einem Konflikt, sobald die Treiber in unterschiedliche Richtungen ziehen (kann zu Instabilität oder zum Kurzschluss kommen).
## Z - ungetrieben/hochohmig : gezielt
Wird durch [[Tristate Buffer]] erzeugt und ist bspw. bei einem Bus gewollt, damit mehere Treiber auf einen Draht schreiben können. Dabei darf aber nur ein [[Tristate Buffer]] gleichzeitig enabled sein.
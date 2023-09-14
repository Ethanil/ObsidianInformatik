---
aliases: 
---
# Sequenzkalkül 
 ![[Sequenz]]

Wir erzeugen allgemeingültige Sequenzen durch Sequenzregeln: neue Sequenzen aus bereits abgeleiteten Sequenzen

## Format
Vergleiche [[Hilbertkalküle]]
$$\frac{\text{Prämisse}}{\text{Konklusion}}$$ 
```ad-example
title:Beispiel
collapse:
$$\frac{}{\Gamma, \varphi \vdash \Delta, \varphi}$$

---


$$\frac{\Gamma \vdash \Delta, \varphi}{\Gamma, \neg\varphi \vdash \Delta}$$
```
 
 ```ad-abstract
title:Definition - Ableitbarkeit
Eine Sequenz heißt ableitbar im Sequenzkalkül, falls sie (in endlich vielen Schritten) durch Anwendung von Sequenzregeln (ausgehend von Axiomen, d.h. Regeln ohne Prämissen) als Konklusion gewonnen werden kann.
```

```ad-abstract
title:Definition - Abschwächungslemma
Ist $\Gamma \vdash \Delta$ mit Beweistiefe $n$ ableitbar, so auch $\Gamma, \Gamma' \vdash \Delta, \Delta'$
```
```ad-abstract
title:Definition - Inversionslemma
Alle Regeln für $\neg, \lor, \land, \rightarrow$ sind auch von unten nach oben gelesen korrekt.
Genauer: Ist die Konklusion (mit Beweis der Tiefe $n$) herleitbar, dann auch die Prämisse(n) (mit gleicher Tiefe)
```
```ad-abstract
title:Definition - Kontraktionslemma
Ist $\Gamma, \varphi, \varphi \vdash \Delta$ (bzw. $\Gamma \vdash \Delta, \varphi, \varphi$) beweisbar (mit Tiefe $n$), so auch $\Gamma, \varphi \vdash \Delta$ (bzw. $\Gamma \vdash \Delta, \varphi$)
```

## Regeln
![[Informatik/Semester_02/APL/Aussagenlogik/Sequenzkalkülregeln]]

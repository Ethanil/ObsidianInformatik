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

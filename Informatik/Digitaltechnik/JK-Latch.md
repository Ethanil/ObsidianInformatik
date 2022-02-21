---
aliases: 
---
# JK-Latch
Ein JK-Latch besteht aus einem [[SR-Latch]] mit 2 vorgeschalteten [[Konjunktion(und)|Und-Gattern]].
![[JK-Latch_21.02.2022 18-41-57.excalidraw.md]]
Mit den beiden [[Konjunktion(und)|Und-Gattern]] wird der [[SR-Latch#Problematik|Problemfall]] des SR-Latches verhindert, da auch wenn $J=K=1$ ist $S$ und $R$ beide niemals $1$ werden können, wir Togglen einfach den Output, also wenn $Q$ vorher $0$ war ist es nach $J=K=1$ dann auf eine $1$ gesetzt.
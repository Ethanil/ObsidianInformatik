---
aliases: 
---
# SR-Latch
Set- und Reset-Latch
Bei einem SR-Latch schalten wir wie bei der [[Bistabile Grundschaltung]] 2 [[NOR|NOR-Gatter]] hintereinander.
![[SR-Latch_21.02.2022 18-34-51.excalidraw.md]]
## Funktion
- Wenn $S$ und $R$ beide 0 sind, dann wird der vorherige Zustand gehalten (Latch)
- Wenn $S$ 1 und $R$ 0 ist, dann wird der aktuale Zustand $Q$ auf 1 gesetzt (Set)
- Wenn $S$ 0 und $R$ 1 ist, dann wird der aktuale Zustand $Q$ auf 0 gesetzt (Reset)
- Wenn $S$ und $R$ beide 1 sind, dann sind wir in einem ungültigen Zustand
## Problematik
Der ungültige Zustand $S=R=1$.
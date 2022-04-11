---
aliases: 
---
# Multiplexer
Ein Multiplexer oder $MUXn$ wählt aus $n$ Eingängen (Hier $A_0 und A_1$) genau 1 aus, für seinen Ausgang($Y$).
Dabei hat der Multiplexer zusätzlich zu seinen Eingängen noch ein Steuersignal($S$), welches $log_2n$ Bits hat (also es gibt so viele Verschiedene Zustände im Steuersignal wie es Eingänge gibt.)
![[Multiplexer_21.02.2022 13-36-09.excalidraw]]
Wenn in unserem Bsp. das Steuersignal also $0$ ist, wird der Eingang $A_0$ also zu $Y$ "durchgeschaltet" und bei einem Steuersignal von $1$ der Eingang $A_1$.

| $S$ | $A_0$ | $A_1$ | $Y$ |
| --- | ----- | ----- | --- |
| 0   | 0     | 0     | 0   |
| 0   | 0     | 1     | 0   |
| 0   | 1     | 0     | 1   |
| 0   | 1     | 1     | 1   |
| 1   | 0     | 0     | 0   |
| 1   | 0     | 1     | 1   |
| 1   | 1     | 0     | 0   |
| 1   | 1     | 1     | 1   |

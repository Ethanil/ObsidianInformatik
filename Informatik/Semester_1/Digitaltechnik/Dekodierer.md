---
aliases: 
---
# Dekodierer
Ein Dekodierer implementiert eine sogenannte "One-Hot" Kodierung, also wir haben $n$-Eingänge und $2^n$ Ausgänge. Wenn im Eingang nun eine $0_2$ anliegt, dann ist der 1. Ausgang an und alle anderen sind aus. Wenn eine $3_2=11$ anliegt, dann ist der 4. Ausgang an und alle anderen snd aus

| $A_1$ | $A_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0     | 0     | 1     | 0     | 0     | 0     |
| 0     | 1     | 0     | 1     | 0     | 0     |
| 1     | 0     | 0     | 0     | 1     | 0     |
| 1     | 1     | 0     | 0     | 0     | 1     |

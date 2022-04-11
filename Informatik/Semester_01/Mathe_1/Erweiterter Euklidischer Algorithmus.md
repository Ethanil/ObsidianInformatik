# Erweiterter Euklidischer Algorithmus
Beim erweiterten eukdlischen Algorithmus wird im Vergleich zum [[Der Euklidische Algorithmus|normalen]] nicht nur der [[ggT]] sondern auch zwei ganze Zahlen ermittelt für die gilt
$$ggT(a,b) = k*a+l*b$$

Um dies zu ermitteln führen wir zuerst den normale Euklidischen Algorithmus durch, bis wir $0$ für $b$ erhalten, dabei schreiben wir uns gleich $\lfloor\frac{a}{b}\rfloor$ auf:

| a   | b   | $\lfloor\frac{a}{b}\rfloor$ |
| --- | --- | --------------------------- |
| 141 | 9   | 15                          |
| 9   | 6   | 1                           |
| 6   | 3   | 2                           |
| 3   | 0   |                             |

Diese Tabelle gehen wir dann von unten nach oben durch und berechnen $k$ und $l$.
Dafür setzen wir $k=1$ und $l=0$ in der untersten Zeile.
In der obendrüber setzen wir $k=l$ und $l = k - \lfloor\frac{a}{b}\rfloor * l$

| a     | b   | $\lfloor\frac{a}{b}\rfloor$ | k    | l            |
| ----- | --- | --------------------------- | ---- | ------------ |
| $141$ | $9$ | $15$                        | $-1$ | $16=1-15*-1$ |
| $9$   | $6$ | $1$                         | $1$  | $-1 = 0-1*1$ |
| $6$   | $3$ | $2$                         | $0$  | $1 = 1-2*0$  |
| $3$   | $0$ |                             | $1$  | $0$          |

Wir erhalten für $k=-1$ und für $l=16$ $\Longrightarrow ggT(141,9)=3=141*-1+9*16 \checkmark$
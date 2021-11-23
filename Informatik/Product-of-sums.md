---
aliases: [POS,KNF,Konjunktive Normalform]
---
# Product-of-sums
Die POS besteht aus dem [[Konjunktion(und)|Produkt]] aller [[Maxterm|maxterme]].
Jede boolsche Funktion hat genau eine POS.
```ad-example
collapse: true
| A   | B   | Y   | Minterm                       |
| --- | --- | --- | ----------------------------- |
| 0   | 0   | 0   | $m_0=A+B$                      |
| 0   | 1   | 1   | $m_1=A+\overline{B}$           |
| 1   | 0   | 1   | $m_2=\overline{A}+B$           |
| 1   | 1   | 0   | $m_3=\overline{A}+\overline{B}$ |

$SOP=(A+B)(\overline{A}+\overline{B})=m_0m_3$
```

Siehe [[Sum-of-products|SOP]]
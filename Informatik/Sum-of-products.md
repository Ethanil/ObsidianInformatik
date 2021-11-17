---
aliases: [SOP,Disjunkte Normalform,DNF]
---
# Sum-of-products
Die SOP besteht aus der [[Disjunktion(oder)|Summe]] aller [[Minterm|minterme]].
Jede boolsche Funktion hat genau eine SOP.
```ad-example
collapse: true
| A   | B   | Y   | Minterm                        |
| --- | --- | --- | ------------------------------ |
| 0   | 0   | 0   | $m_0=\overline{A}\overline{B}$ |
| 0   | 1   | 1   | $m_1=\overline{A}B$            |
| 1   | 0   | 1   | $m_2=A\overline{B}$            |
| 1   | 1   | 0   | $m_3=AB$                       |

$SOP==m_1+m_2
```
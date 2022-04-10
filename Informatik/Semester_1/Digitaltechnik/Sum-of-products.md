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

$SOP=\overline{A}B+A\overline{B}=m_1+m_2$
```

Siehe [[Product-of-sums|POS]]

Ziffer x0 x1 x2 x3 a b
0
1
2
3
4
5
6
7
8
9 0
0
0
0
0
0
0
0
1
1 0
0
0
0
1
1
1
1
0
0 0
0
1
1
0
0
1
1
0
0 0
1
0
1
0
1
0
1
0
1 1
0
1
1
0
1
1
1
1
1 1
1
1
1
1
0
0
1
1
1
c
d
e
f
g1
g2 h i j k l m dp dk
0
0
1
1
1
1
1
0
1
1 0
0
0
0
0
0
0
0
0
0 0
0
0
0
0
0
0
0
0
0 1
1
0
0
0
0
0
0
0
0 1
0
0
0
0
0
0
0
0
0 0
0
0
0
0
0
0
0
0
0 0
0
0
0
0
0
0
0
0
0 0
0
0
0
0
0
0
0
0
0 0
0
0
0
0
0
0
0
0
0
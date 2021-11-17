---
aliases: 
---
# Boolsche Algebra
Um die Terme die wir durch [[Sum-of-products|SOP]] und [[Product-of-sums|POS]] (o.ä.) erhalten haben zu vereinfachen können wir bewiesene Regeln innerhalb der Boolschen Algebra verwenden.
Um Theoreme zu Beweisen müssen wir zuerst Axiome festlegen, die nicht beweisbar sind.

| Axiom                   | Dual                      | Name         |
| ----------------------- | ------------------------- | ------------ |
| $A1: B=0 \ if \ B\neq1$ | $A1': B=1 \ if \ B\neq 0$ | Binary field |
| $A2: \overline{0}=1$    | $A2': \overline{1}=0$     | NOT          |
| $A3: 0\cdot 0=0$        | $A3': 1+1=1$              | AND/OR       |
| $A4: 1\cdot 1=1$        | $A4': 0+0=0$              | AND/OR       |
| $A5: 1\cdot 1=1\cdot 1=0$ | $A5': B=1 \ if \ B\neq 0$ | AND/OR       |

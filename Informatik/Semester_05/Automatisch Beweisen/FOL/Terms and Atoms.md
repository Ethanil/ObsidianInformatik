---
aliases:
  - term
  - terms
  - atom
  - atoms
---
Terms($T$) und Atoms($A$) sind induktiv definiert
1. $Var \subseteq T_{\Sigma}$ 
2. Wenn $t_{1},\dotso ,t_{n} \in T_{\Sigma}$ und $f \in F_{\Sigma}$ $n$-ary ist, dann ist $f(t_{1},\dotso,t_{n})\in T_{\Sigma}$
3. Wenn $t_{1},\dotso ,t_{n} \in T_{\Sigma}$ und $p \in P_{\Sigma}$ $n$-ary ist, dann ist $p(t_{1},\dotso,t_{n})\in A_{\Sigma}$

Ein variable-free Term(bzw Atom) nennt man ground term(bzw atom)
$T_{\Sigma}^{0}$(bzw $A_{\Sigma}^{0}$) sind die Mengen aller ground terms (bzw atomic formulars) über $\Sigma$
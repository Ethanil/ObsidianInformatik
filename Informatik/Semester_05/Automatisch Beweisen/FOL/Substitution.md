Substitution ist ein mapping von Variablen: $\upsigma : Var \rightarrow T_{\Sigma}$ 
Die Substitution domain sind alle Variablen die auf etwas anderes gemapped werden: $dm(\upsigma) = \{x \in Var |\upsigma(x) \neq x\}$
Substitution range sind alle Variablen auf die gemapped werden: $rg(\upsigma) = \{\upsigma(x) | x \in dm(\upsigma)\}$

Wir schreiben für substitutions mit endlichen domainen $\{x_{1}/\upsigma(x_{1})...\}$ 

## Erweiterung mit [[Terms and Atoms|terms]] und [[Formula|Formulas]]
- $\upsigma(s) = s$ (wobei $s$ eine 0-ary funktion oder predicate ist)
- $\upsigma(true) = true, \upsigma(false)=false$
- $\upsigma(s(t_{1},...,t_{n})) = s(\upsigma(t_{1}),...,\upsigma(t_{n}))$ (wobei $s$ eine n-ary funktion oder predicate ist)
- $\upsigma(\lnot \varphi)=\lnot \upsigma(\varphi)$
- $\upsigma(\varphi_{1} \circ ... \circ \varphi_{n})=\upsigma(\varphi_{1})\circ ... \circ \upsigma(\varphi_{n})$, wobei $\circ \in\{\land, \lor\}$ 
# Aussagen und ihre Verknüpfungen
## Beispiele für Aussagen
```ad-example
title: Beispiele für Aussagen
$2 + 3 = 5$ 							|wahre Aussage
$7 < 3$ 								|falsche Aussage
5 ist eine Primzahl					|wahre Aussage
Es gibt unendlich viele Primzahlen 	|wahre Aussage
```
## Aussageformen
Aussageformen können Variablen enthalten
```ad-example
title: Beispiele für Aussageformen mit Variablen
$x + y = y + x$					|wahre Aussage, die auf alle reellen Zahlen zutrifft
$x² + y² = 1$					|Das ist eine Aussage die nicht für alle reellen Zahlen zutrifft
$n \ge 2$								
$n*k=m$
```
## Quantoren
### [[Allquantor]]
### [[Existenzquantor]]

---
Es gibt unendlich viele Primzahlen würde man folgender Art und Weise aufschreiben:
$\forall n \in \mathbb{N}:\exists p\in \mathbb{N}:n\le p\wedge P_z(p)$
Übersetzt:
Für alle natürlichen Zahlen $n$ gibt es mindestens eine natürliche Zahl $p$ für die gilt: $p$ ist größer als $n$ und für $p$ gilt $P_z$(ist eine Primzahl)
## Aussagen und ihre Verknüpfungen (Aussagenlogische Junktoren)
Mithilfe dieser Junktoren kann man aus 2 Aussagen eine neue Aussage treffen

| $A$ | $B$ | $A\wedge B$ | $A\vee B$ | $A\Rightarrow B$ | $\neg A$ | $A\Leftrightarrow B$ |
| --- | --- | ----------- | --------- | ---------------- | -------- | -------------------- |
| w   | w   | w           | w         | w                | f        |                      |
| w   | f   | f           | w         | f                | f        |                      |
| f   | w   | f           | w         | w                | w        |                      |
| f   | f   | f           | f         | w                | w        |                      |

### [[Konjunktion(und)]]
### [[Disjunktion(oder)]]
### [[Negation(nicht)]]
### [[Implikation]]
### [[Äquivalenzrelation]]
### [[Logische Äquivalenz]]
#### de Morgan'sche Regel:
$$\neg(A\vee B)\Leftrightarrow(\neg A)\wedge (\neg B)\equiv\neg A\wedge\neg B$$
$$\neg(A\wedge B)\Leftrightarrow(\neg A)\vee (\neg B)\equiv\neg A\vee\neg B$$
#### Kommutativgesetzt
$$A\vee B\equiv B\vee A$$
$$A\wedge B\equiv B\wedge A$$
#### [[Assoziativitätgesetz|Assoziativ]]sgesetz
$$(A\wedge B)\wedge C\equiv A\wedge(B\wedge C)$$
$$(A\vee B)\vee C\equiv A\vee(B\vee C)$$
#### [[Distributivgesetz]]e
$$C\wedge(A\vee B)\equiv(C\wedge A)\vee(C\wedge B)$$
$$C\vee(A\wedge B)\equiv(C\vee A)\wedge(C\vee B)$$
#### Kontraposition
$$(A\Rightarrow B)\Leftrightarrow((\neg B)\Rightarrow\neg A)$$
#### de Morgansche Regel für Quantoren
$$\neg\exists x\in M:A(x)\Leftrightarrow\forall x\in M:\neg A(x)$$
$$\neg\forall x\in M:A(x)\Leftrightarrow\exists x\in M:\neg A(x)$$
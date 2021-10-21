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
### Allquantor
$\forall x \in M:E(x)$ -> für ALLE ($\forall$) $x$ in $M$ gilt: $x$ hat die Eigenschaft $E$
### Existenzquantor
$\exists x \in M:E(x)$ -> es exisistieren ($\exists$) $x$ in $M$ für die gilt: $x$ hat die Eigenschaft $E$

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

### Konjunktion(und)
$$A\wedge B$$
Die beiden Aussagen, welche mit dem Junktor `und` verbunden wurden ergeben genau dann wahr, wenn beide Aussagen wahr sind. Wenn eine, oder beide der Aussagen falsch ist ist das ergbnis falsch.
### Disjunktion(oder)
$$A\vee B$$
Die beiden Aussagen, welche mit dem Junktor `oder` verbunden wurden ergeben genau dann wahr, wenn mindestens eine der beiden Aussagen wahr ist. Wenn beide Aussagen falsch sind, ist das Ergebnis auch falsch.
### Negation(nicht)
$$\neg A$$
Mithilfe von `nicht` kann man den Wahrheitswert von einer Aussage ändern. Eine Wahre Aussage wird falsch, eine falsche Aussage wird wahr.
### Implikation
$$A\Rightarrow B$$
Dieser Junktor kann auch dargestellt werden mit
$$A\Rightarrow B\equiv\neg A \vee B$$
Die Aussage $A$ impliziert $B$ ist also nur dann falsch, wenn $A$ wahr ist und $B$ falsch.
### Äquivalenz
$$A\Leftrightarrow B$$
Diese Aussage kann man auch ausdrücken durch:
$$A\Leftrightarrow B\equiv A\Rightarrow B \wedge B\Rightarrow A$$
### LOGISCHE ÄQUIVALENZ
$$\equiv$$
Logische Äquivalenz beschreibt eine Gleichheit beider Seiten, sie sind also äquivalent zueinander.
#### de Morgan'sche Regel:
$$\neg(A\vee B)\Leftrightarrow(\neg A)\wedge (\neg B)\equiv\neg A\wedge\neg B$$
$$\neg(A\wedge B)\Leftrightarrow(\neg A)\vee (\neg B)\equiv\neg A\vee\neg B$$
#### Kommutativgesetzt
$$A\vee B\equiv B\vee A$$
$$A\wedge B\equiv B\wedge A$$
#### Assoziativsgesetz
$$(A\wedge B)\wedge C\equiv A\wedge(B\wedge C)$$
$$(A\vee B)\vee C\equiv A\vee(B\vee C)$$
#### Distributivgesetze
$$C\wedge(A\vee B)\equiv(C\wedge A)\vee(C\wedge B)$$
$$C\vee(A\wedge B)\equiv(C\vee A)\wedge(C\vee B)$$
#### Kontraposition
$$(A\Rightarrow B)\Leftrightarrow((\neg B)\Rightarrow\neg A)$$
#### de Morgansche Regel für Quantoren
$$\neg\exists x\in M:A(x)\Leftrightarrow\forall x\in M:\neg A(x)$$
$$\neg\forall x\in M:A(x)\Leftrightarrow\exists x\in M:\neg A(x)$$
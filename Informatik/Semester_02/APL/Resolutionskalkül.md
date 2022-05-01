---
aliases: 
---
$\newcommand{\f}[1]{\mathcal{#1}}\newcommand{\F}[1]{\mathfrak{#1}}\newcommand{\b}[1]{\mathbb{#1}}$
# Resolutionskalkül 
Der Resolutionskalkül ist ein Kalkül , der auf den Nachweis der Unerfüllbarkeit von AL-Formeln in [[Konjunktive und disjunktive Normalformen|KNF]] gerichtet ist. Also sogenannte Widerlegung oder Refutation.
Dabei weisen wir die Unerfüllbarkeit einer gegebenen Klauselmenge durch Ableitung der leeren Klausel nach.

## Beobachtungen
$C$ ist eine [[Klausel]] und $K$ eine [[Klausel#Klauselmenge|Klauselmenge]]
Wenn $L$ und $\bar{L}$ aus $C$ sind, dann ist $C$ immer wahr ([[Grundlegende semantische Begriffe#Allgemeingültigkeit|Tautologie]])
Wenn $C\in K$ und $C \equiv 1$ dann ist $K \equiv K \backslash \{C\}$
Wenn die leere Klausel $\square$ in $K$ ist, dann ist $K$ nicht [[Erfüllbarkeit|erfüllbar]].
Wenn $K=\{C_{1},C_{2}\}$ und $L \in C_{1}$ und $\bar{L}\in C_{2}$ dann können wir ein $C$ mit $C=(C_{1}\backslash \{L\}) \cup(C_{2}\backslash\{\bar{L}\})$ definieren, sodass dann $K \equiv K \cup \{C\}$. (Also $K \vDash C$)
```ad-important
title:Dieses $C$ nennt man Resolvente
```

## Beweise im Resolutionskalkül
Wir erstellen einen [[baum|Ableitungsbaum]] für $\square$, wobei die Knoten mit Klauseln, $\square$ die Wurzel, die Resolventen an den binären Verzweigungen und die Klauseln aus K an den Blättern sind.

```ad-abstract
title:Definition - Res(K)
$$Res(K):=K \cup\{C:C \text{ Resolvente von Klauseln in }K\}$$
```

```ad-abstract
title:Definition - Ableitbar
Eine Klausel $C$ heißt (im Resolutionskalkül) **ableitbar** aus $K$, gdw. $C \in \underbrace{Res( \dotso Res(K))}_{\text{n-mal}}$ für ein $n \in \mathbb{N}$
```

```ad-abstract
title:Definition - $Res*(K)$

```
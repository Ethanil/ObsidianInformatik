---
aliases: [Finite State Machine(FSM),Finite State Machine, FSM]
---
# Zustandsautomaten
Ein Zustandsautomaten besteht immer aus endlich vielen Zuständen, Übergängen zwischen diesen Zuständen und mindestens einem akzeptierenden Zustand
## Zustandsautomaten und Digitaltechnik
In der [[Digitaltechnik]] werden v.a. [[Moore Automat|Moore-]] und [[Mealy Automat|Mealy Automaten]] verwendet.
Damit können synchrone, sequentielle Schaltungen mit
- $n$ Eingabebits
- $k$ Ausgabebits
- ein interner Zustand (besteht aus $m \geq 1$ Bits)
- Takt und Reset
in jedem Takt (zur steigenden Flanke) wird abhängig ob der Reset aktiv oder inaktiv ist, entweder der aktuale Zustand auf den Startzustand(wenn Reset aktiv) oder
## Anwendungsbeispiele
Ein Zahlenschloss beziehungsweise generelle Mustererkennung kann sehr einfach mit einem Automaten implementiert werden.
## Automaten Diagramme als gerichtete Graphen
Automaten kann man außer durch das Aufschreiben von Zuständen, Übergängen, Start und End-Zustand auch als einen gerichteten Graphen notieren.
Dabei werden die Zustände zu Knoten mit symbolischen Namen(typischerweise $S_0,S_1 \dotso$) und die Übergänge werden als Kanten mit einem boolschen Ausdruck dargestellt. Wenn ein Zustand unverändert bleibt kann man diese Kante auch weglassen um es vereinfacht zu notieren. Genau eine Kante ohne einen Startpunkt für Reset.
Ausgabel sind entweder an Kanten ([[Mealy Automat]]) oder in den Zuständen ([[Moore Automat]])
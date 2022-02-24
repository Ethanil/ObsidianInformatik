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
## Automaten als Zustandsübergänge und Ausgabe
Das Ziel ist eine Realisierung mittels [[Hardware]], dabei ist das Vorgehen immer das selbe:
- Beschreibung: egal ob textuell, FSM, Wahrheitstabelle, [[Karnaugh Diagramme]]
- Gleichung: abgeleitet von der Beschreibung
- Schaltung: [[Kombinatorische Logik|kombinatorisch]], [[Sequentielle Schaltungen|sequentiell]] oder [[Synchrone sequentielle Logik|synchron]]
### Zustandsübergangs- und Ausgabetabelle
Tabellen sind sehr praktisch, da sie eine maschinenlesbare Darstellung sind. Man kann mit noch abstrakteren Zuständen und Ausgaben arbeiten und dabei Don't Cares verwenden. Der aktuelle Zustand wird dabei als $S$ und der nächste Zustand als $S'$ bezeichnet.
#### Beispiel
Der folgende [[Moore Automat]] würde wie folgt als Tabelle dargestellt werden:
![[Moore Automat_24.02.2022 15-29-18.excalidraw.md]]
##### Zustandsübergangstabelle:
| $S$ | $a_A$ | $a_B$ | $S'$ |
| --- | ----- | ----- | ---- |
| A   | 0     | X     | AB   |
| A   | 1     | x     | A    |
| AB  | X     | X     | B    |
| B   | X     | 0     | BA   |
| B   | x     | 1     | B    |
| BA  | X     | X     | A    |

##### Ausgabetabelle:
| $S$ | $y_A$ | $y_B$ |
| --- | ----- | ----- |
| A   | grün  | rot   |
| AB  | gelb  | rot   |
| B   | rot   | grün  |
| BA  | rot   | gelb  |

Der folgende [[Mealy Automat]] würde wie folgt als Tabelle dargestellt werden:
![[Mealy Automat_24.02.2022 15-35-07.excalidraw.md]]
##### Zustandsübergangstabelle
| $S$ | $a_A$ | $a_B$ | $S`$ |
| --- | ----- | ----- | ---- |
| A   | 1     | X     | A    |
| A   | 0     | X     | AB   |
| AB  | X     | X     | B    |
| B   | X     | 1     | B    |
| B   | X     | 0     | BA   |
| BA  | X     | X     | A    |
##### Ausgabetabelle
| $S$ | $a_A$ | $a_B$ | $y_A$ | $y_B$ |
| --- | ----- | ----- | ----- | ----- |
| A   | 1     | X     | grün  | rot   |
| A   | 0     | X     | gelb  | rot   |
| AB  | X     | X     | rot   | grün  |
| B   | X     | 1     | rot   | grün  |
| B   | X     | 0     | rot   | gelb  |
| BA  | X     | X     | grün  | rot   |

Wie man eindeutig sieht ist bei einem [[Mealy Automat]] der Output auch vom Input abhängig, bei einem [[Moore Automat]] nicht.
### FSM als [[Synchrone sequentielle Logik|synchrone sequentielle Schaltung]]
Um eine FSM als Schaltung zu realisieren benötigen wir immer ein Zustandsregister, welches den aktuellen Zustand $S$ speichert und in der nächsten Taktflanke den Zustand $S'$ übernimmt.
Wir benötigen außerdem kombinatorische Logik, die sowohl den nächsten Zustand (next state logic) als auch den Output (output Logic) bestimmen, welche wir aus den Zustandsübergangstabellen und Ausgabetabellen ableiten können.
Für das Umsetzen benötigen wir eine binäre Kodierung der Zustände und Ein-/Ausgaben
![[Pasted image 20220224174427.png]]
#### Zustandskodierung
Bei der Zustandskodierung weisen wir jedem Zustand einen $m$ Bit breiten Wert zu, welcher idR frei gewählt werden kann. Das simpelste ist das einfache Durchnummerieren, also bei 4 Zuständen diese einfach $00,01,10,11$ zu nennen.
Manchmal sind aber auch andere Kodierungen sinnvoll wie bspw. die [[One-Hot-Kodierung]] oder eine bestehende [[Ausgabekodierung]]. Oftmals ist die Kodierung der Ein
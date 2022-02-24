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
| AB  | X     | X     | B    |
| B   | X     | 0     | BA   |
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
|     |       |       |      |
##### Ausgabetabelle
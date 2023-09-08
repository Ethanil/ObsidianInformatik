---
aliases:
  - Transaktion
  - Schedule
---
# Transaktionsverarbeitung 
Eine Transaktion ist eine Folge von logisch zusammengehörigen [[Anfragesprache SQL||SQL]]-Anfragen und SQL-Änderungsoperationen. Die Transaktionsverarbeitung in Datenbanksystemem setzt ACID-Garantien bei Ausführung um.
## ACID-Garantien
***A***tomicity: Entweder alle oder keine Änderung einer Transaktion werden angewandt
***C***onsistency: Transaktionen überführen eine Datenbank von einem konsistenten in einen anderen konsistenten Zustand
***I***solation: Garantiert korrekte Ausführung von Transaktionen unter Nebenläufigkeit
***D***urability: Das Ergebnis einer Transaktion wird (nur) im Erfolgsfall **persistent** gespeichert.

Die ACID-Garantien können auf Verschiedene Art und Weisen umgesetzt werden
- Atomicity und Durability durch Logging und Recovery (Fehlerbehandlung)
- Consistency durch Constraint Checking
- Isolation durch Concurrency Control
## Isolation über Concurrency Control
### Anomalien
| Anomalie     | Beschreibung                                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Lost Update  | Die Änderung der Transaktion1 werden durch Transaktion2 überschrieben.                                            |
| Dirty Read   | Wiederholte Lesevorgänge der Transaktion2 liefern unterschiedliche Ergebnisse                                     |
| Phantom Read | Transaktion2 liest bei einer gleichen Anfrage unterschiedliche Datensätze, die von Transaktion 1 eingefügt wurden |

### Transaktions-Scheduler
Der Transaktions-Scheduler bestimmt die Reihenfolge in der die Schritte von nebenläufigen Transaktionen ausgeführt werden
Datenbanken setzten sich dabei in einem vereinfachten Modell aus einer Menge von Datenbankobjekten ($o_{1},o_{2},\dotso,o_{n}$) zusammen und Transaktionen führen Lese- und Schreib-Operationen auf diesen Datenbankobjekten aus.
Datenbankobjekte sind dabei typischerweise ein kompletter Datensatz(also eine Zeile einer Tabelle) oder nur einzelne Attribute des Datensatzes.

#### Scheduler-Ansätze
Es gibt unterschiedliche Alternativen eine Scheduler zu implementieren, der serialisierbare Schedules erzeugt:
Durch einen pessimistischen Ansatz werden Konflikte durch bspw. Sperren von vorneherein vermieden.
Durch optimistische Ansätze lassen wir erstmal alles durchlaufen und erkennen die Konflikte im Nachhinein.
Optimistische Ansätze haben einen höheren Durchsatz, wenn es weniger Konflikte gibt.
### Transaktionen und Schedule

```ad-abstract
title:Definition - Transaktion
Eine Transaktion ist eine geordnete Folge von Schritten
- Transaktion $T_{i}<s_{i}^{1},\dotso,s_{i}^{n}>$ für Schritte 1...n in Transaktion i wobei Schritt-Indizes häufig weggelassen werden
- Typische Schritte sind Lesen( $r_{i}(o_{k})$ ) oder Schreiben( $w_{i}(o_{k})$ )
- Weiter Schritte: $b_{i}$(begin), $c_{i}$(commit), $a_{i}$(abort), wobei $b_{i}$ und $c_{i}$ häufig weggelassen werden
```

```ad-abstract
title:Definition - Schedule
Ein Schedule S für eine Menge von Transaktionen $T=\{T_{1},\dotso,T_{n}\}$ ist eine (partielle) [[Ordnungsrelation|Ordnung]] der Schritte ALLER Transaktionen
- Bei einem Ein-Prozessor-System stellt $S$ eine totale Ordnung ansonsten eine partielle Ordnung dar
- Die Reihenfolge der Schritte innerhalb einer Transaktion bleiben in $S$ erhalten: $s^{k}(o_{k})<s^{I}(o_{I})$ in $T_{n}\Rightarrow s^{k}(o_{k})<s^{I}(o_{I})$ in $S$
```

```ad-abstract
title:Definition - serieller Schedule
Ein serieller Schedule ist ein spezieller Schedule bei dem alle Schritte einer Transaktion **konsekutiv** aufeinander folgen
```

Serielle Schedules erzeugen keine Anomalien, allerdings ist die Performanz (Durchsatz) eines seriellen Schedules idR geringer als für nicht serielle Schedules

Ein Schedule $S$ heißt serialisierbar, wenn $S$ äquivalent zu irgendeinem seriellen Schedule $S'$ ist.
Äquivalent bedeutet, dass
- Alle Leseaktionen den gleichen Wert lesen
- Die Werte aller geänderter Datenbankobjekte nach der Ausführung der beiden Schedules $S$ oder $S'$ gleich sind.
### Konfliktgraph
Die Serialisierbarkeit eines Schedules $S$ kann mit Hilfe eines Konfliktgraphen $G$ überprüft werden
Der Graph enthält einen Knoten pro Transaktion und eine Kante pro Konflikt zwischen zwei Transaktionen
Ein Konflikt zwischen Transaktion $T_{X}$ und $T_{Y}$ entsteht dabei wenn
- $s_{x}(o_{k})$ vor $s_{y}(o_{y})$ auf dem gleichen Objekt $o_{k}$ im Schedule liegt und
- $s_{x}$ oder $s_{y}$ eine Schreiboperation auf $o_{k}$ ist

Wenn dieser Konfliktgraph nun **azyklisch** ist, dann ist der Schedule $S$ serialisierbar.

### Lock-based Concurrency Control
Lock-based concurrency control ist eine Möglichkeit einen pessimistischen Scheduler zu implementieren, der serialisierbare Schedules mithilfe von Sperren(locks) erzeugt.
Die Idee dahinter ist, dass sich die Transaktion zum Lesen oder Ändern ein Lock auf das Objekt holt. Nebenläufige Transaktionen müssen auf Locks warten und nach erfolgereicher Änderung geben Transaktionen das Lock wieder frei.
#### Naives Locking
Beim naiven locking wird direkt vor und nach jedem Lese oder Änderungszugriff ein Lock auf das Objekt geholt/entfernt.
Dies garantiert ***keine*** serialisierbaren Schedules
#### Two-Phase Locking(2PL)
Beim Two-Phase-Locking ifndet das Locking pro Transaktion in zwei Phasen statt, der Grow und der Release-Phase. Während der Release-Phase dürfen keine neuen Locks geholt werden.
2PL garantiert seriaisierbare Schedules.
2PL hat allerdings noch 2 Probleme: Deadlocks und Cascading Aborts.
#### Preclaiming
Beim Preclaiming werden alle Locks atomar vor Beginn der Transaktion angefordert. Dies verhindert offensichtlich Deadlocks.
#### Strict 2PL
Beim Strict 2PL werden alle Locks bis zum Ender der Transaktion gehalten und dann atomar freigegeben. Dies verhindert Cascading Aborts, da nachfolgende Transaktionen keine Änderungen lesen können, bevor die Transaktion nicht beendet ist.

### Isolationsstufen
Nicht alle Anwendungen benötigen die höchste Isolationsstufe(Serialisierbarkeit), daher ermöglicht es SQL 92 eine Isolationsstufe zu setzen. Dies führt auf kosten von mehr Anomalien zu einem höheren Durchsatz

| Isolationsstufe | Beschreibung                                                                                                  | Lost Updates  | Dirty Reads   | Non-repeatable Reads | Phantom Reads |
| --------------- | ------------------------------------------------------------------------------------------------------------- | ------------- | ------------- | -------------------- | ------------- |
| Read uncommited | Transaktionen fordern keine Sperren an. Diese Stufe ist nur für Lese-Transaktionen verwendbar.                | möglich       | möglich       | möglich              | möglich       |
| Read Commited   | Transaktionen fordern Write-Locks mit Strict 2PL an. Ihre Lese-Locks werden direkt freigegeben.               | möglich       | NICHT möglich | möglich              | möglich       |
| Read stability  | Schreib- und Lese-Locks werden mit Strict 2PL angefordert.                                                    | NICHT möglich | NICHT möglich | NICHT möglich        | möglich       |
| Serializable    | Schreib- und Lese-Locks werden mit Strict 2PL angefrodert mit Lösung für Phantom Problem (durch Range Locks). | NICHT möglich | NICHT möglich | NICHT möglich        | NICHT möglich |

### Multi-Version Concurrency Control(MVCC)
Hierbei liegt jedes Datenobjekt in mehreren Versionen vor und jeder Schreiber erzeugt eine neue Version, wobei alte Versionen erhalten bleiben. Hierbei ist Garbage Collection no
## Links
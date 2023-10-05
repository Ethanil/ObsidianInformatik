Machine Learning erlaubt Rechnern zu lernen ohne explizit dafür programmiert zu sein.
Wir teilen Machine Learning in Supervised([[Generative]] und [[Discriminative]]), Semi-Supervised(Metric Learning) und Unsupervised([[Clustering]]) ein.

## Generative vs Discriminative
Die Entscheidung in welche Klasse ein Objekt gehört ist bei Discriminative sehr viel einfacher.
Da die "World state"(also bspw. gesund oder krank) sehr viel kleiner als bspw Bilddaten sind, ist das erlernen für discriminative sehr viel einfacher.
Wenn wir Informationen über das Generieren von Daten haben wollen, müssen wir generative verwenden.
Wenn wir während des trainings/testens noch nicht alle Daten haben, verwenden wir generative.
Wenn wir Expertenwissen einarbeiten wollen verwenden wir generative.

## Discriminative Learning
Wir wollen, wenn wir bestimmte visuelle Daten $x$ erhalten, einen world state $y$ erzeugen.
Dies nennt man bei einem diskreten World state [[Klassifizieren|Klassifikation]] und bei wertkontinuierlichen World state Regression.

## Komponenten des Machine Learnings
- Modell
- Lern-Algorithmus
- Inference Algorithmus

### Modell
Beim Modell bringen wir mathematisch visuelle Daten mit einem wordstate in Verbindung. Diese Verb
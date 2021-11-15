# Der Euklidische Algorithmus
Mithilfe des euklidischen Algorithmus können wir den [[ggT]] zweier Zahlen herausfinden.
Um ihn zu benutzen müssen wir allerdings zuerst 2 [[Lemma]] beweisen.

## Lemma
$ggT(a,b) = ggT(b, a \ mod \ b)$
$b|a\Longrightarrow ggT(a,b)=b$
Beweise siehe Skript

## Anwendung
Um den Eukldischen Algorithmus anzuwenden schreiben wir das ganze am besten mit einer Tabelle auf:
Wir setzen als neues $a$ immer $b$ ein und als neues $b$ $a \ mod \ b$

| a   | b   |
| --- | --- |
| 128 | 36  |
| 36  | 20  |
| 20  | 16  |
| 16  | 4   |
| 4   | 0   | 

Sobald wir für $b$ $0$ erhalten haben wir bei $a$ den ggT gefunden!
$\Rightarrow ggT(128,36)=4$
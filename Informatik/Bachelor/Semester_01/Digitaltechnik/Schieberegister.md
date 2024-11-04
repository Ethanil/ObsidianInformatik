---
aliases: 
---
# Schieberegister
In einem Schiebe [[Register]] wird bei jeder steigenden Taktflanke der Speicherinhalt ein [[D-Flip-Flop|Flip-Flop]] weiter verschoben.
Kann als Seriell-Parallel-Wandler verwendet werden, indem man nach jedem [[Register]] den Output dieses Registers ausließt.
Um ein [[Schieberegister]] mit parallelem Laden zu realisieren benötigen wir noch ein Load-Signal das bestimmt, wann der Inhalt der [[Register]] vom Input überschrieben werden sollen.
Natürlich kann man beide Varianten auch kombinieren.
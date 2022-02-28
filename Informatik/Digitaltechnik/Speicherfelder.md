---
aliases: Speicherfeld
---
# Speicherfelder
Ein Speicherfeld ist ein 2 dimensionales Array von Bitzellen. Jede Bitzelle speichert ein Bit.
Die Tiefe des Arrays ist gleichbedeutend mit der Adresse des jeweiligen Bitwortes. Wobei jedes Bitwort so breit ist, wie das Array selbst auch.
Ein $2^2 \times 3$-Bit Array hat also 4 Wörter, die jeweils 3 Bits lang sind.
## Speicherarten
### Direktzugriffsspeicher (random access memory, RAM)
RAM ist ein flüchtiger Speicher, also er verliert beim Ausschalten alle Daten, der allerdings ein schnelles Lesen und Schreiben erlaubt. Man unterscheidet Dynamic RAM ([[DRAM]]) und Static RAM ([[SRAM]]).
Der deutsche Begriff Direktzugriffsspeicher kommt daher, dass anders als bei Kasetten oder Bandlaufwerken direkt auf das gesamte Datenwort zugegriffen werden konnte.
![[Pasted image 20220228155753.png]]
#### Festwertspeicher (read-only memory, ROM)
ROM ist im Gegensatz zu RAM nicht flüchtig, also die Daten bleiben auch beim Ausschalten erhalten. ROM erlaubt ein schnelles Lesen, allerdingst ist Schreiben unmöglich oder nur langsam möglich. 
Der Name kommt daher, dass man ROMs früher nur einmalig beschrieben konnte, es daher fest war. Für Flash-Speicher und andere Arten von ROM's gilt dies heutzutage nicht mehr.
#### Logik via ROM
Mir den im ROM eingespeicherten Werten kann man Logik realisieren. Mithilfe eines Dekoders und einem ROM-Baustein
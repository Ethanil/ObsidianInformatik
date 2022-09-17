---
aliases: Pipelined-Implementierung
---
# Pipeline-Prozessor 
Die Phasen der Befehlsausführung werden in fünf Phasen eingeteilt:
- Instruction Fetch
- Instruction Decode, Read Register
- Execute ALU
- Memory Read/Write
- Write Register

Wir verwenden den Datenpfad von einem [[Eintakt-Prozessor]] und Pipelinen diesen an den 5 Stellen, damit wir diese gleichzeitig Ausführen können.
## Data Hazard
### Read-after-Write-Hazard (RAW)
Da damit jeder Befehl 5 Takte braucht um einen Befehl vollständig abzuarbeiten und diesen wieder in das gewünschte Register zu schreiben, kann der direkt nachfolgende Befehl erst ausgeführt werden, nachdem das Register aktualisiert wurde.
### Umgang mit Data Hazards
#### Wartezeit einplanen
Wir fügen nops zur Compile Zeit ein, damit dieses Problem nicht auftritt.
#### Bypassing/Forwarding
Wir geben schon berechnete Daten weiter und umgehen erstmal das schreiben.
#### stall
Wir erzeugen eine mögliche Schleife, also Phasen werden doppelt ausgeführt.
## Control Hazard

## Links
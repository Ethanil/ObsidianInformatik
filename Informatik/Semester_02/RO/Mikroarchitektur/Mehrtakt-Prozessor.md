---
aliases: 
---
# Mehrtakt-Prozessor
Der Mehrtakt-Prozessor hat eine kombinierte Komponente für Instruction und Data Memory, anders als der Eintakt-Prozessor.
## Mehrtakt-Datenpfad anhand des ldr-Befehls
### 1. Hole Instruktions
Aus dem Instruction Memory wird die Instruktion mit der Adresse des PC geladen und in ein Instruktionsregister (iR) geladen.
### 2. Lese Quelloperand aus Registerfeld und Werte Direktwert aus
Basisadresse wird an das RegisterFile angelegt und die Basisadresse wird in einem Register gespeichert.
Das Immediate wird auf 32 Bit erweitert.
### 3. Berechne die Speicheradresse (Basisadresse + Offset)
Über eine ALU wird die Basisadresse aus dem Register mit dem Immediate verrechnet um die Speicheradresse zu erhalten, die Ihrerseits wieder in einem Register gespeichert wird.
### 4. Lese Daten aus Speicher
Die Speicheradresse wird aus dem Data-Memory geladen und in einem Register gespeichert.
### 5. Schreibe die Daten ins passende Register
Die Daten werden über einen Multiplexer verschaltet zu WD3 des RegisterFiles angelegt, damit sie dort dann geschrieben werden können.
### 6. Berechne Adresse des nächsten Befehls
Der alte PC wird über einen Multiplexer verschaltet an die selbe ALU angelegt und dort mit 4 addiert.
### 7. Behandlung von r15(pc)
Der um +4 erhöhte PC wird nochmals um 4 erhöht und an r15 angelegt.
## Links
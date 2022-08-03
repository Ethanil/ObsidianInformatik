---
aliases: 
---
# Eintakt-Implementierung 
## Datenpfad anhand Beispiel ldr
### 1. Befehl holen
Über den Programmcounter im Instruction Memory die Instruction auslesen.
### 2. Lesen der Quell-Operanden vom Registerfeld
Rn, also das was mit dem ldr Befehl eingelesen werden soll, wird an den Adresseingang A1 angelegt.
Rd, also  das Destination Register (wo ldr Rn speichern soll) wird an A3 angelegt.
### 3. Erweiterung des immediates
imm12, also der 12-Bit-Offset, wird mit 0en erweitert, damit er 32 Bit lang ist.
### 4. Berechnung der Speicheradresse
Der 32-Bit lange immediate wird dann mit dem Wert der Basisadresse (Rn) addiert wird um die Adresse zu erhalten von der kopiert werden soll. 
### 5. Lesen der Daten aus dem Speicher und Schreiben in das Registerfeld
Diese Adresse wird an Data Memory angelegt und das Ergebnis wird an WD3 des Register Files angelegt, damit dann der Wert an der Adresse, die ja an A3 angelegt wurde, gespeichert werden kann.
### 6. Berechnung der Adresse des nächsten Befehls
Wir addieren 4 zum Programcounter und schreiben das in das Programcounter-Register, der nächste Befehl kann ausgeführt werden.
## Links
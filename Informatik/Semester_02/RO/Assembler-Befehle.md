---
aliases: 
---
# Assembler-Befehle 
`CC` steht für [[Condition Codes]] und S für mögliche Suffixe um [[Statusflags]] zu setzen.
## mögliche Operanden
- Direkter Wert (I)
- Register (R)
- Speicher (M)
- Adresse (PTR)
## Arithmetische Befehle
| Befehl | Operanden | Statusbits | Beispiel                                                       | Wirkung |
| ------ | --------- | ---------- | -------------------------------------------------------------- | ------- |
| Add    | R,R,R/I   | N,C,Z,V    | `ADD r1,r2,#7` <br> `ADDEQS r1,r2,r3` | addiert r2 und 7 auf r1 <br> addiert r2 und r3 auf r1, wird nur bei Flag `Z=1` ausgeführt und setzt flags        |
|        |           |            |                                                                |         |

## Transportbefehle

## Logische Befehle

## Kontroll- und Sprungbefehle

## Links
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
| Befehl     | Operanden | Statusbits | Beispiel                              | Wirkung                                                                                                   |
| ---------- | --------- | ---------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ADD(CC)(S) | R,R,R/I   | N,C,Z,V    | `ADD r1,r2,#7` <br> `ADDEQS r1,r2,r3` | addiert r2 und 7 auf r1 <br> addiert r2 und r3 auf r1, wird nur bei Flag `Z=1` ausgeführt und setzt flags |
| ADC(CC)(S) | R,R,R/I   | N,C,Z,V    | `ADC r1,r2,r3`                        | `r1:=r2+r+C`addiert r2,r3 und `C` auf r1                                                                  |
| MUL(CC)(S) | R,R,R     | N,Z        | `MUL r1,r2,r3`                        | `r1:=r2*r3` speichert least significant 32 bit in `r1`                                                    |
| SUB(CC)(S) | R,R,R/I   | N,C,Z,V    | `SUB r1,r2,r3`                        | `r1:=r2-r3`                                                                                               |

## Transportbefehle

## Logische Befehle

## Kontroll- und Sprungbefehle

## Links
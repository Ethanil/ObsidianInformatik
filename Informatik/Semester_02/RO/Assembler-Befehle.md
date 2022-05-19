---
aliases: 
---
# Assembler-Befehle 
Jeder Befehl, außer `NOP`, kann sogenannte [[Condition Codes]] verwenden, indem sie hinter den Befehl geschrieben werden (`BEQ` anstatt nur `B`, damit nur dann gesprungen wird wenn die entsprechenden [[Statusflags]] gesetzt wurden) und S für mögliche Suffixe um [[Statusflags]] zu setzen.
## mögliche Operanden
- Direkter Wert (I)
- Register (R)
- Speicher (M)
- Adresse (PTR)
## Arithmetische Befehle
| Befehl     | Operanden | Statusbits | Beispiel                              | Wirkung                                                                                                   |
| ---------- | --------- | ---------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| ADD(S) | R,R,R/I   | N,C,Z,V    | `ADD r1,r2,#7` <br> `ADDEQS r1,r2,r3` | addiert $r2$ und $7$ auf $r1$ <br> addiert $r2$ und $r3$ auf $r1$, wird nur bei Flag `Z=1` ausgeführt und setzt flags |
| ADC(S) | R,R,R/I   | N,C,Z,V    | `ADC r1,r2,r3`                        | $r1:=r2+r+C$ addiert $r2,r3$ und `C` auf $r1$                                                                  |
| MUL(S) | R,R,R     | N,Z        | `MUL r1,r2,r3`                        | $r1:=r2*r3$ speichert least significant 32 bit in $r1$                                                    |
| SUB(S) | R,R,R/I   | N,C,Z,V    | `SUB r1,r2,r3`                        | $r1:=r2-r3$                                                                                              |

## Transportbefehle
| Befehl | Operanden          | Statusbits    | Beispiel                                                                                                     | Wirkung                                                                                    |
| ------ | ------------------ | ------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| LDR    | R,M                | Keine         | `LDR r1,adr_v1`<br>`LDR r3,[r1,#4]`<br>`LDR R0, [R1,R2,LSL #4]`<br>`LDR R0, [R1, #4]!`<br>`LDR R0, [R1], R2` | $r1:=$ Adresse von $v1$ <br>$r3:=r1[1]$<br>$r0:=r1[(r2<<4)]$<br>$r1+=4; r0:=*rl$<br>$r0=*r1; r1+=r2$ |
| STR    | R,M                | Keine         | `STR r1,adr_v1`<br>`STR r3,[r1, #4]`<br>`STR R0, [R1,R2,LSL #4]`                                             | Adresse von $v1:=r1$<br>$r1[1]:=r3$<br>$r1[(r2<<4)]:=0$                                          |
| MOV(S) | N,Z                | `MOV r1, #26` | $r1:=26$                                                                                                       |                                                                                            |
| POP    | {R} oder {R,R,...} | Keine         | `POP r1`                                                                                                     | Legt den Inhalt vom Stack in das Register $r1$                                               |
| Push   | {R} oder {R,R,...} | Keine         | `PUSH r1`                                                                                                    | Legt den Inhalt des Registers $r1$ auf den Stack                                                                                           |

## Logische Befehle
| Befehl | Operanden     | Statusbits | Beispiel          | Wirkung                                              |
| ------ | ------------- | ---------- | ----------------- | ---------------------------------------------------- |
| AND(S) | R,R,R/I       | N,Z        | `AND r1,r2,#0xF9` | $r1=r2 \& 0xF9$                                         |
| ASR(S) | R,R,R/I(1-32) | C,Z,N      | `ASR r1,r1#8`     | Arithmetischer Shift von $r1$ nach rechts um $8$ Stellen |
| EOR(S) | R,R,R/I       | N,Z        | `EOR r1, r2, r3`  | $r1:=r2 \oplus r3$                                   |
| LSL(S) | R,R,R/I       | N,C,Z      | `LSL r1, r2, #4`  | $r1:=$Logischer Shift von $r2$ nach links um $4$ Stellen   |
| LSR(S) | R,R,R/I       | N,C,Z      | `LSR r1, r2, #4`  | $r1:=$ Logischer Shift von $r2$ nach rechts um $4$ Stellen |
| MVN(S) | R,R/I         | N,Z        | `MVN r1, r2`      | $r1:=!r2$                                            |
| ORR(S) | R,R,R/I       | N,Z        | `ORR r1, r2, r3`  | $r1:=r2 | r3$                                                     |

## Kontroll- und Sprungbefehle
| Befehl | Operanden | Statusbits | Beispiel     | Wirkung                                                                      |
| ------ | --------- | ---------- | ------------ | ---------------------------------------------------------------------------- |
| B      | PTR       | Keine      | `B loopA`    | Springt zu label loopA                                                       |
| BL     | PTR       | Keine      | `BL lopA`    | Speichert nachfolgende Befehlsdresse in LR und springt zu loopA              |
| BLX    | PTR/R     | Keine      | `BLX loopA`  | Wie `BL` und kann Instruction Set zwischen A32 und T32 wechseln              |
| BX     | PTR/R     | Keine      | `BX lr`      | Springt an Adresse $lr$ und kann Instruction Set zwischen A32 und T32 wechseln |
| CMP    | R,R/I     | N,C,Z,V    | `CMP r1, #3` | Zieht $3$ von Wert in $r1$ ab, updatet Statusflags, Wert $r1$ unverändert          |
| CMN    | R,R/I     | N,C,Z,V    | `CMN r1, #3` | Addiert $3$ zu dem Wert in $r1$, updatet Statusflags, Wert $r1$ unverändert        |
| NOP    |           | Keine      | `NOP`        | Nulloperation/Verzögerung                                                    |

## Links
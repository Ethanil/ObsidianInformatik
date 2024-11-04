---
aliases: 
---
# Condition Codes 
Condition Codes sind Suffixe von Befehlen, die Bedingungen anhand der [[Statusflags]] definieren. Diese Bedinungen müssen erfüllt sein, damit die Anweisung ausgeführt wird.
| Suffix     | Flags                            | Bedeutung           |
| ---------- | -------------------------------- | ------------------- |
| EQ         | Z gesetzt                        | Gleich              |
| NE         | Z ungesetzt                      | Ungleich            |
| CS oder HS | C gesetzt                        | $\geq$ für unsigned |
| CC oder LO | C ungesetzt                      | $<$ für unsingend   |
| MI         | N gesetzt                        | negative            |
| PL         | N ungesetzt                      | Positiv oder Null   |
| VS         | V gesetzt                        | Overflow            |
| VC         | V ungesetzt                      | Kein Overflow       |
| HI         | C gesetzt und Z ungesetzt        | $>$ für unsigned    |
| LS         | C ungesetzt oder Z gesetzt       | $\leq$ für unsigned |
| GE         | N und V sind gleich              | $\geq$ für signed   |
| LT         | N und V sind ungleich            | $<$ für signed      |
| GT         | Z ungesetzt, N und V sind gleich | $>$ für signed      |
| LE         | Z gesetzt, N und V sind ungleich | $\leq$ für signed   |



## Links
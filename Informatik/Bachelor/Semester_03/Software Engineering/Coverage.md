---
aliases: 
---
# Coverage 
## Structural Coverage
### Statement Coverage
Für ein Programm p gibt es für jedes Statemenet s einen Test in der Testbench, der dieses ausführt.
### Basic Block Coverage
Für ein Programm p gibt es für jedes Statemenet s einen Test in der Testbench, der dieses ausführt.
Also fast wie Statement Coverage, nur dass man es bei bytecode bzw machinecode macht.
### Branch Coverage
Für ein Programm p wird jede Kante in seinem CFG von einem Test der Testbench ausgeführt.
### Path Coverage
Für ein Programm p wird jeder mögliche Pfad durch sein CFG von einem Test der Testbench ausgeführt
## Logic-Based-Coverage
### Decision Coverage
Eine Testbench hat Decision-Coverage wenn jede Decision einmal False und einmal als True evaluated wurde. Eine Decision besteht aus mehrere Conditions.
### Condition Coverage
Eine Testbench hat Condition-Coverage wenn jede Condition einmal False und einmal als True evaluated wurde. Eine Condition ist der kleinste Logikblock in einer Bedingung.
### Modified Condition-Decision Coverage(MCDC)
Für jedes Auftreten einer Condition c in der Decision d ist MCDC erfüllt, wenn
- d mindestens 2mal evaluated wird
	- einmal davon muss c false sein und einmal true
	- d muss in beiden versionen unterschiedlich ausgewertet sein
	- alle anderen conditions in d werden gleich oder gar nicht ausgewertet
### Multiple-condition Coverage(MCC)
Alle möglichkeiten für Conditions werden mindestens einmal ausgeführt.
## Links
---
aliases: 
---
# Logikfelder
## Programmable Logic Array(PLA)
ein PLA realisiert einfache kombinatorische Logik via [[Sum-of-products|SOP]]. Varianten davon sind ein Programmable [[Speicherfelder#Festwertspeicher read-only memory ROM|ROM]] oder eine Programmable Array Logic (PAL), bei dem nur das Eingabefeld programmierbar ist.
## Performanz vs Flexibilität
Logikfelder kann man auf verschiedene Arten implementieren, dabei muss die Performance mit der Flexibilität abgewogen werden.
Extrem performant, aber nicht flexibel sind anwendungsspezifische integrierte Schaltungen(ASIC, application-specific integrated circuit), welche nur für eine Anwendung optimierte Datenpfade ausführen kann und daher nicht zur Laufzeit an neue Anwendungen anpassbar ist.
Ein Software-Prozessor kann generische Instruktionen sequentiell ausführen und in ihmist nur generische Architektur in Hardware realisiert, dafür ist er aber sehr flexibel, da er zur Laufzeit nur durch Austauschen der Instruktionssequenz an neue Anwendungen anpassbar ist.
Ein [[Field Programmable Gate Array]] (FPGA) vereint die Flexibilität von einem Software-Prozessor mit der Performance von einem ASIC.
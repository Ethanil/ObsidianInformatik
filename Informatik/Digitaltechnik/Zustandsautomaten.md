---
aliases: [Finite State Machine(FSM),Finite State Machine, FSM]
---
# Zustandsautomaten
Ein Zustandsautomaten besteht immer aus endlich vielen Zuständen, Übergängen zwischen diesen Zuständen und mindestens einem akzeptierenden Zustand
## Zustandsautomaten und Digitaltechnik
In der [[Digitaltechnik]] werden v.a. [[Moore Automat|Moore-]] und [[Mealy Automat|Mealy Automaten]] verwendet.
Damit können synchrone, sequentielle Schaltungen mit
- $n$ Eingabebits
- $k$ Ausgabebits
- ein interner Zustand (besteht aus $m \geq 1$ Bits)
- Takt und Reset
in jedem Takt (zur steigenden Flanke) wird abhängig ob der Reset aktiv oder inaktiv ist, entweder der aktuale Zustand auf den Startzustand(wenn Reset aktiv) oder
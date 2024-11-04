---
aliases: 
---
# Vorlesung 1 
## Fault Error Failure

```ad-abstract
title:Definition - Fault
Ein Fault ist eine abnormale Condition(wie bspw. kosmische Strahlung) die zu einem Error führen kann.
```

```ad-abstract
title:Definition - Error
Ein Error ist eine Diskrepanz zwischen erwarteten und wirklichen Werten (wie bspw. ein Bit in einer Speicherzelle hat den Falschen Wert). Der Error kann dann zu einem Failure führen.
```

```ad-abstract
title:Definition - Failure
Ein Failure kann dann zu einem Fehler im Programm führen(Berechnung falsch)
```

## Verfügbarkeit berechnen
```ad-abstract
title:Definition - Availability
$\text{Availability} =  \frac{\text{Total Up-Time}}{\text{Total(Up + Down-Time)}}$
```

```ad-abstract
title:Definition - Availability 2.0
$\text{Availability} = \frac{\text{MTTF}}{\text{MTTF}+\text{MTTR}}$
```
$$MTTF = E[T] = \int^{\infty}_{0}1- F(t) dt - \int^{0}_{-\infty}F(t) dt = \int^{\infty}_{0} R(t)dt $$
$$MTTF = \int^{\infty}_{0}e^{-\lambda t} dt = \frac{1}{\lambda}\text{    für exponentielle Modelle}$$
Bei in Reihe geschalteten, unabhängigen Komponenten reicht es, dass eine Komponente ausfällt, damit das ganze System ausfällt, daher müssen die für die Überlebenswahrscheinlichkeit des Systems die Wahrscheinlichkeit für ein Failure für jede Komponente multiplizieren.
Bei einer Parallelschaltung müssen alle Komponenten ausfallen, damit das ganze System ausfällt, wodurch wir für die Überlebenswahrscheinlichkeit die Gegenwahrscheinlichkeit berechnen müssen, dass alle Komponenten ausfallen.
## Umgang mit Fehlern
- Fault avoidance (Testen, Verifikation)
- Fault recovery (wieder in korrekten Systemzustand, aber wie Fehler erkennen?)
- Fault tolerance (Redundanz)
	- Physikalische Redundanz(Einfach mehrere Komponenten, die berechnen)
		- statisch(Einer entscheidet an sich alles, bei Fehler wird auf anderen umgeswitcht)
		- dynamische Redundanz(Alle werfen ihre Lösung in einen Topf und Mehrheitsprinzip)
	- Zeitliche Redundanz(Auf dem selben System mehrmals rechnen)
## Links
[[Vorlesung 2]]
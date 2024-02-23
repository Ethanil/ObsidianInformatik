---
aliases: 
---
Eingabedaten für 3D-Modelle zu erhalten ist ein Problem.
Um diese zu erzeugen kann auf verschiedene Lösungen zurückgegriffen werden, die jeweils vor- und nachteile haben
## Interaktive Eingabegeräte
Mit interaktiven Eingabegeräten kann der Nutzer interaktiv Daten eingeben.
### 2D
2D Eingabegeräte sind beispielsweise eine Maus oder ein Zeichenstift. Diese haben das Problem, dass vom 2 Dimensionalen auf das 3 Dimensionale übertragen werden muss
### 3D
3D Eingabegeräte sind beispielsweise Tracker mit 3 oder 6 Freiheitsgrade, die auf unterschiedliche Technologien zurückgreifen, um Input zu generieren. Sie sind oft unintuitiv zu verwenden oder haben wenig software-support.
## Abtastung realer Objekte
Reale Objekte können abgetastet werden, um verschiedene digitalisierte Darstellungen dieses zu erhalten. Zum Beispiel Einzelne Tiefenkanten, Punktwolken oder Dreiecksnetze.
### Optische Verfahren
Bei optischen Verfahren unterscheidet man zwischen aktiven und passiven Methoden. Bei passiven Methoden werden aus Bildern und Videos mittels verschiedener Methoden die Daten generiert. Bei aktiven Methoden wird Stereo mit Zusatzinformation verwendet, bspw Markerpunkte oder eine projizierte Textur.
#### Vorteile
- Kontaktfrei
- Sicher
- Kostengünstig
- Schnell
#### Nachteile
- Abhängig von optischen Eigenschaften
- Verdeckungsproblematik
- Textur
### Optische Triangulation
![[Pasted image 20240223205149.png# shadow float right 4/5]]
Bei der passiven optischen Triangulation wird mit 2 Kameras aus unterschiedlichen(bekannten) Positionen Bilder gemacht und daraus die Form des Objekts berechnet, allerdings muss immer eine Korrespondenz von den einzelnen Objekten bei den beiden Bildern gefunden werden.



![[Pasted image 20240223211309.png# shadow float right 4/5]]
Bei der aktiven Triangulation wird ein Laser verwendet, um das Objekt abzutasten. Dieser wird über die Szene bewegt und der reflektierte Punkt(wenn er nicht verdeckt wird) kann eindeutig identifiziert und zur Triangulation verwendet werden. Ein besseres System verwendet einen Laserstriches anstatt eines punktes. Ein Problem ist hierbei, zusätzlich zur Verdeckung, die relfektorischen eigenschaften des Modells.
## Links
---
aliases: 
---
# Zerlegung von Zustandsautomaten
Oftmals kann man komplexe [[Zustandsautomaten|FSM's]] in einfachere und interagierende aufteilen. Wenn wir uns das [[Moore Automat#Beispiel Ampelsteuerung|Beispiel der Ampelsteuerung mit einem Moore Automaten]] anschauen und dort einen überschreibenden Zustand haben möchten, der bei einem Festumzug die Ampel nur in eine Richtung anschaltet, dann ist dies am simpelsten möglich, indem wir dies "vorschalten" und nicht versuchen es zu integrieren.
## Unzerlegtes Beispiel
![[Pasted image 20220224183443.png]]
![[Pasted image 20220224183429.png]]
## Zerlegtes Beispiel
![[Pasted image 20220224183452.png]]
![[Pasted image 20220224183502.png]]
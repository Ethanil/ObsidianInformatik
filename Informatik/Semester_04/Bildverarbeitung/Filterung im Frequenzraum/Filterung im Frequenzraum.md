Bei der Filterung im Frequenzraum wird anders als bei der [[Filterung im Ortsraum]] eine Bildtransformation über eine Manipulation der Koeffizienten im [[Frequenzraum]] ausgeführt. Danach wird eine Rücktransformation in den Bildbereich gemacht.

![[Pasted image 20230927104729.png# 4/5 left shadow|allgemeines Vorgehen bei der Filterung im Frequenzraum, beispielhaft mit der Fourier Transformation]]


In der Regel wird nur im Amplituden Spektrum und **nicht** im Phasenspektrum gefiltert, wir verwenden sogenannte Zero-Phase-Shift Filter.
## idealer Tiefpass-Filter

![[Pasted image 20230927112423.png# 5/6 left shadow|Eine Visualisierung des Idealen Tiefpass-Filters]]

Der Ideale Tiefpass Filter ist ein Zylinder mit dem sehr starkes [[Ringing]] entsteht.

## Butterworth Tiefpass-Filter

![[Pasted image 20230927112906.png# 5/6 left shadow|Der Butterworth Tiefpass-Filter ist eine "abgerundete" Version des idealen Tiefpass-Filters]]

Beim Butterwort Tiefpass-Filter kann das [[Ringing]] stark reduziert werden.

## Gauss'scher Tiefpass-Filter

![[Pasted image 20230927113401.png# 5/6 left shadow|Der Gauss'sche Tiefpass reduziert das Ringing am besten und führt damit zu den besten Ergebnissen]]

## Hochpass/Bandpass/Bandstop-Filter
Die Drei Filter gibt es auch als Hochpass, Bandpass oder Bandstop Filter.

## Homomorphische Filterung
Signale können in nicht-linearer Art kombiniert sein, dann hilft uns eine lineare Signalanalyse nicht weiter.
Wir können dafür das Bild zuerst logarithmieren, dann Transformieren, dann Filtern und dann alles wieder Rückgängig machen und können so bspw die multiplikativen Komponenten des Bildraums einzeln herausfiltern.
![[Pasted image 20230927121125.png# 5/6 left shadow|Zuerst wird das Bild logarithmiert, bevor es transformiert und gefiltert wird]]


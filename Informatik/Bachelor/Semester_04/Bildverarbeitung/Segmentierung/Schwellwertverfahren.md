Beim Schwellwertverfahren für die [[Segmentierung]] legen wir einen bestimmten Schwellwert fest ab dem wir bspw. die Pixel schwarz färben und für jeden Pixel der diesen Schwellwert nicht überschreitet, färben wir ihn weiß.
![[Pasted image 20230929123216.png# 5/6 left shadow|Wir färben alles über dem Schwellwert T weiß ein und alles unter dem Schwellwert schwarz.]]

Unterstützen können wir dies durch einen vorherigen [[Lineare Filter#Tiefpass|Tiefpass-Filter]], durch den wir Rauschen entfernen.

![[Pasted image 20230929123316.png# 5/6 left shadow|wenn wir vor dem Schwellwertverfahren einen Tiefpass anwenden, funktioniert das verfahren sehr viel besser]]

Wenn wir bspw. einen Gradienten über unserem Bild (also bspw. schlechte Beleuchtungsverhältnisse) haben, können wir anstatt einem Globalen Schwellwert mehrere lokale Schwellwerte festlegen, um ein gutes Ergebnis zu erzielen

![[Pasted image 20230929123513.png# 5/6 left shadow| Das Bild wurde in 6 Teile aufgeteilt und für jeden ein einzellner Schwellwert festgelegt, sodass sich das Ergebnis signifikant verbessert]]


# Physikalische Realisierung von Logikgattern
Um die "Nullen und Einsen" zu realisieren müssen wir diese irgendwie darstellen. Dies tun wir, indem wir bestimmte Spannungspegel festlegen die dann bedeuten, ob etwas eine Null oder eine Eins darstellt.
Da Physikalische Systeme niemals perfekt sind, können wir nicht einfach festlegen, dass bspw 5V an und 0V aus bedeutet, da bspw durch Temperatur die Spannung fluktuiert.
Daher müssen wir Bereiche festlegen in denen etwas als an und etwas als aus zählt.
## Schwellwerte
Wir definieren 4 Schwellwerte um festzulegen wann etwas als 1 und wann etwas als 0 zählt:
- $V_{OH}:$ kleinste Spannung, die Treiber als 1 ausgibt ("Voltage Output High")
- $V_{IH}:$ kleinste Spannung, die Empfänger als 1 interpretiert ("Voltage Input High")
- $V_{IL}:$ größte Spannung, die Empfänger als 0 interpretiert ("Voltage Input Low")
- $V_{OL}:$ größte Spannung, die Treiber als 0 ausgibt ("Voltage Output Low")

---
- $NM_H= V_{OH}-V_{IH}$ oberer Störabstand ("Noise Margin High")
- $NM_L= V_{IL}-V_{OL}$ unterer Störabstand ("Noise Margin Low")
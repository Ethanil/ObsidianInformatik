Bei einer Filtermaske wird ein Pixel abhängig von den Pixelwerten in seiner [[Nachbarschaft]](also dem lokalen Kontext) manipuliert.
Die Operation ist dabei definiert innerhalb der Nachbarschaft mit einer gewissen Gewichtung abhängig, wie weit der benachbarte Pixel entfernt ist.
![[Pasted image 20230926100305.png# 5/6 left shadow]]
$$\begin{align*}
g[m,n] = \sum^{M_{+}}_{l=-M_{-}}\sum^{N_{+}}_{k=-N_{-}}w_{l,k}\cdot f[m-l,n-k]
\end{align*}$$
## Randbetrachtung
Wir haben einen Sonderfall, wenn wir Pixel am Rand betrachten, da wird dort keine vollständige Matrix an Nachbarn haben. Möglichkeiten damit umzugehen:

| Name                                 | Vorgehen                                                                           |
| ------------------------------------ | ---------------------------------------------------------------------------------- |
| Keine Randbetrachtung                | Wir verwenden die Maske erst weiter innen                                          |
| Zero-Padding                         | Wir tun so, als ob es 0en außerhalb des Bildes gäbe                                |
| Last-Value                           | Wir duplizieren den letzten Wert am Rand "nach außen"                              |
| Periodische Fortsetzung              | Wir wrappen around(also wenn wir links rausgehen, nehmen wir werte von rechts)     |
| Symmetrische Fortsetzung             | Wenn wir aus dem Bild herausgehen würden, gehen wir in die andere Richtung         |
| Extrapolative Fortsetzung            | Wir extrapolieren das Bild nach außen weiter (raten wie die Pixel aussehen würden) |
| Konstruktion spezieller Filtermasken | Wir verwenden spezielle, kleinere Masken für die Ränder                            |

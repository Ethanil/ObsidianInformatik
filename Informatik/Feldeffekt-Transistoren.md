# Feldeffekt-Transistoren
Logikgatter werden üblicherweise aus Transistoren aufgebaut, heute werden dafür überwiegend sogenannte Feldeffekttransistoren (FET, "Field Effect Transistor") verwendet.
![[Feldeffekt-Transistoren_2021-11-10 18.22.59.excalidraw|150|right-wrap]]
Transistoren sind Spannungsgesteuerte Schalter
zwei Anschlüsse (Source s & Draind d), werden je nach Spannung am dritten Eingang (Gate g) verbunden oder getrennt

## Halbleiter
Um durch Spannung etwas leitend zu machen in unseren Transistoren benutzen wir sogenannte Halbleiter, welche durch den Feldeffekt leitend werden und ohne Feldeffekt nicht leitend sind.
Wir erzeugen Halbleiter indem wir in nicht leitende Materialien wie Silizium (Glas) leitende Atome einbauen, wie Phosphor oder Bromium. Dabei fügen wir entweder weitere Elektronen hinzu und erzeugen so ein n-Typ Silizium oder wir nehmen Elektronen weg und erzeugen so ein p-Typ Silizium.

## P/N Übergang - Diode
Wenn wir nun p-Typ und n-Typ Halbleiter direkt nebeneinander setzen und daran eine Spannung anlegen können wir sie leitend bzw nichtleitend machen (abhängig von der Seite an der wir + bzw - anschließen). Wir erzeugen also eine Diode, also ein Baustück welchse von p-Typ zu n-Typ leitet, aber andersherum nicht.

## MOS Feldeffekttransistoren (MOSFETs)
MOS steht für Metalloxid-Halbleiter (Metall-Oxide-)
Bei einem MOSFET betten wir 2 n-Typ Halbleiter(Source und Drain) in einen p-Typ Halbleiter (Substrat) ein (nMOS), bzw 2 p-Typ in ein n-Typ (pMOS).

## nMOS
![[Pasted image 20211110184249.png|300]]
![[Pasted image 20211110184423.png|300]]
Durch anlegen von Spannung an das Gate (das obere GND im oberen Bild und $V_{DD}$ im unteren) "öffnen" wir den Transistor, indem wir den p-Typ Halbleiter leitend machen und damit eine Verbindung zwischen den beiden n-Typ Halbleitern erstellt haben.
Die Majoritätsladungsträger in einem nMOS sind Elektronen, was bedeutet dass er 0'en gut von Source nach Drain weiterleiten kann.

## pMOS
![[Pasted image 20211110185126.png]]
pMOS Transistoren schließt man "nach unten" zur Versorgungsspannung ($V_{DD}$) und ist ausgeschaltet, wenn das Gate 1 ist.
Die Majoritätsladungsträger sind "Löcher", also leiten wir 1'en gut von Source nach Drain weiter.
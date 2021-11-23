---
aliases: 
---
# DT-Projekt1

In dieser Aufgabe untersuchen Sie mögliche Zahlendarstellungen der gemeldeten COVID-19 Impfungen. Am 26.10.2021 gab es deutschlandweit 55 158 070 gemeldete vollständige Impfungen.
a) Geben Sie eine allgemein gültige Formel an, welche die minimale Bitbreite z ausgibt, die zur Darstellung der Dezimalzahl x benötigt wird. Es wird also eine Gleichung der Form z = ... gesucht.
Hinweis: Verwenden Sie die Notation dN e , um N auf die nächste ganze Zahl aufzurunden (z.B. d1, 23e = 2 ). (1PP)
$$z=\lceil log_2(x+1)\rceil$$
b) Wie viele Bits werden benötigt, um die oben genannte Anzahl vollständiger Impfungen im Binärsystem darzustellen? Verwenden Sie zur Berechnung Ihre in a) hergeleitete Formel. (0,5 PP)
$$z=\lceil log_2(55,158,070+1)\rceil$$
$$z=\lceil log_2(55,158,071)\rceil$$
$$z=\lceil 25.717068668\rceil$$
$$z=26$$

c) Um die Anzahl der benötigten Stellen zur Repräsentation der Anzahl vollständiger Impfungen zu verringern, sollen die Zahlen im 7er-Zahlensystem dargestellt werden. Berechnen Sie die benötigte Anzahl an Stellen für die Repräsentation der oben genannten Anzahl vollständig geimpfter Personen im 7er-Zahlensystem. Geben Sie anschließend die oben genannte Anzahl vollständig geimpfter Personen im 7er-Zahlensystem an. (2 PP)
$$7⁰=1$$
$$7^1=7$$
$$7^2=49$$
$$7^3=343$$
$$7^4=2401$$
$$7^5=16,807$$
$$7^6=117,649$$
$$7^7=823,543$$
$$7^8=5,764,801$$
$$7^9=40,353,607$$
$$7^{10}=282,475,249$$
$$7^{10}>55,158,070\Rightarrow\text{ man kann diese Zahl mit 10 Stellen im 7er System schreiben.}$$
$$(1*7^9+2*7^8+3*7^7+6*7^6+5*7^5+5*7^4+6*7^3+4*7^2+6*7^1+2*7^0)_{10}$$
$$=(1236556462)_7$$
d) Wie viele vollständige Impfungen liegen in einer Woche vor, wenn jeden Tag 96 472 Impfdosen verabreicht werden, wovon 53 693 Erstimpfungen 3 sind? Führen Sie alle Rechnungen im 7er-Zahlensystem durch. Konvertieren Sie dafür zunächst alle benötigten Zahlen in das 7er-Zahlensystem. (3,5 PP)
$$(96472)_{10}=(5*7^5+5*7^4+1*7^3+1*7^2+5*7^1+5*7^0)_{10}=(551155)_{7}$$
$$(53693)_{10}=(3*7^5+1*7^4+2*7^3+3*7^2+5*7^1+3*7^0)_{10}=(312353)_{7}$$
Ab jetzt sind alle Rechnungen im 7er System, weshalb auf die $7$ bei $x_7$ verzichtet wird.
$$551155$$
$$-312353$$
$$\_\_\_\_\_\_\_$$
$$235502$$
Als nächstes müssen wir mit $7_{10}$ multiplizieren, also $(10)_7$, was wie bei jeder Multiplikation mit dem Wert der Basis ein Anhängen einer $0$ rechts von der Ursprungszahl bedeutet.
Alternativ ist ein weiterer Weg die Addition:
$$235502$$
$$+235502$$
$$\_\_\_\_\_\_\_$$
$$504304$$
Womit wir den Wert für $2$ Tage haben.

$$504304$$
$$+504304$$
$$\_\_\_\_\_\_\_$$
$$1311611$$
Der Wert für $4$ Tage.

$$1311611$$
$$+504304$$
$$\_\_\_\_\_\_\_$$
$$2116215$$
Der Wert für $6$ Tage.

$$2116215$$
$$+235502$$
$$\_\_\_\_\_\_\_$$
$$2355020$$
$$2355020=10\cdot 235502$$
Der Wert für $(10)_7$ Tage

Um die Datenraten bei der Übertragung aktualisierter Impfungen an unser Einlasssystem möglichst gering halten zu können, wird lediglich die Gesamtzahl neuer verabreichter Impfdosen und die Anzahl an Erstimpfungen übertragen. Zur Vermeidung von Übertragungsfehlern soll eine Längs- und Querparität verwendet werden.
Dem Einlasssystem wurden 93 185 insgesamt verabreichte Impfdosen und 57 849 Erstimpfungen übermittelt. Tragen Sie die Binärdarstellung der insgesamt verabreichten Impfdosen in die erste Zeile in folgender Tabelle ein und die Binärdarstellung der Erstimpfungen in die zweite Zeile. Die empfangenen Längs- und Querparitätsbits sind jeweils in der unteren Zeile und der rechten Spalte eingetragen. Lag ein Übertragungsfehler vor? Wenn ja, markieren Sie das betroffene Bit und nennen Sie die korrekte Dezimalzahl.

| 1            | 0            | 1            | 1            | 0            | 1            | 1            | 0            | 0            | 0            | 0       | 0            | 0            | 0            | 0            | 0            | 1            | 0   | $\checkmark$ |
| ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ------- | ------------ | ------------ | ------------ | ------------ | ------------ | ------------ | --- | ------------ |
| 0            | 1            | 1            | 1            | 0            | 0            | 0            | 0            | 1            | 1            | ***1*** | 1            | 1            | 1            | 0            | 0            | 1            | 1   | X            |
| 1            | 1            | 0            | 0            | 0            | 1            | 1            | 0            | 1            | 1            | 0       | 1            | 1            | 1            | 0            | 0            | 0            | -   | -            |
| $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | X       | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | $\checkmark$ | -   | -            |

In dieser Aufgabe erstellen Sie einen Dekodierer für ein Display zur Darstellung von Dezimalzahlen. Der studentische Filmkreis der TU Darmstadt denkt allerdings auch weiter in die Zukunft und möchte das Display des Einlasssystems nach der Pandemie zur Anzeige von Filmtiteln verwenden. Da eine übliche 7-Segmentanzeige nur mit Einschränkungen Buchstaben anzeigen kann, kommt eine 16-Segmentanzeige (vgl. Abbildung 1) zum Einsatz. 
a) Folgende Tabelle gibt an, welche Segmente bei welcher Ziffer beleuchtet sind. Eine Ziffer wird mit x 0 x 1 x 2 x 3 binär kodiert. Vervollständigen Sie die Tabelle, indem Sie sich an den Segmentnamen und Zuweisungen in Abbildung 1 orientieren. (2,5 PP)

    

| Ziffer | $x_0$ | $x_1$ | $x_2$ | $x_3$ |     | $a$ | $b$ | $c$ | $d$ | $e$ | $f$ | $g_1$ | $g_2$ | $h$ | $i$ | $j$ | $k$ | $l$ | $m$ | $dp$ | $dk$ |
| ------ | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | ---- | ---- |
| 0      | 0     | 0     | 0     | 0     |     | 1   | 1   | 1   | 1   | 1   | 1   | 0     | 0     | 0   | 0   | 1   | 1   | 0   | 0   | 0    | 0    |
| 1      | 0     | 0     | 0     | 1     |     | 0   | 1   | 1   | 0   | 0   | 0   | 0     | 0     | 0   | 0   | 1   | 0   | 0   | 0   | 0    | 0    |
| 2      | 0     | 0     | 1     | 0     |     | 1   | 1   | 0   | 1   | 1   | 0   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 3      | 0     | 0     | 1     | 1     |     | 1   | 1   | 1   | 1   | 0   | 0   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 4      | 0     | 1     | 0     | 0     |     | 0   | 1   | 1   | 0   | 0   | 1   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 5      | 0     | 1     | 0     | 1     |     | 1   | 0   | 1   | 1   | 0   | 1   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 6      | 0     | 1     | 1     | 0     |     | 1   | 0   | 1   | 1   | 1   | 1   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 7      | 0     | 1     | 1     | 1     |     | 1   | 1   | 1   | 0   | 0   | 0   | 0     | 0     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 8      | 1     | 0     | 0     | 0     |     | 1   | 1   | 1   | 1   | 1   | 1   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |
| 9      | 1     | 0     | 0     | 1     |     | 1   | 1   | 1   | 1   | 0   | 1   | 1     | 1     | 0   | 0   | 0   | 0   | 0   | 0   | 0    | 0    |


b) Geben Sie zu den Segmenten c, d, e, f und g 1 die zugehörige vollständige disjunktive Normalform (DNF) oder konjunktive Normalform (KNF) an, je nachdem welche weniger Minterme bzw. Maxterme benötigt. Sofern gleich viele Minterme/Maxterme benötigt werden, geben Sie die DNF an. (2,5 PP)

$$c=x_0+x_1+\bar{x_2}+x_3$$
$$d=(x_0+x_1+x_2+\bar{x_3})
*(x_0+\bar{x_1}+x_2+x_3)
*(x_0+\bar{x_1}+\bar{x_2}+\bar{x_3})$$
$$e=\bar{x_0}\bar{x_1}\bar{x_2}\bar{x_3}
+\bar{x_0}\bar{x_1}x_2\bar{x_3}
+\bar{x_0}x_1x_2\bar{x_3}
+x_0\bar{x_1}\bar{x_2}\bar{x_3}$$
$$f=(x_0+x_1+x_2+\bar{x_3})
*(x_0+x_1+\bar{x_2}+x_3)
*(x_0+x_1+\bar{x_2}+\bar{x_3})
*(x_0+\bar{x_1}+\bar{x_2}+\bar{x_3})$$
$$g_1=(x_0+x_1+x_2+x_3)
*(x_0+x_1+x_2+\bar{x_3})
*(x_0+\bar{x_1}+\bar{x_2}+\bar{x_3})$$
c) Die aus Teilaufgabe b) resultierenden DNFs und KNFs können noch weiter vereinfacht werden. Nutzen Sie Karnaugh Diagramme um die DNFs bzw. KNFs zu minimieren. Betrachten Sie nicht verwendete Kodierungen (10 -15) als “Don’t Cares”. Verwenden Sie das folgende dargestellte Karnaugh Diagramm. (2,5 PP)
$$c=x_1+\bar{x_2}+x_3$$
$$d=x_0+\bar{x_1}x_2+x_2\bar{x_3}+x_1\bar{x_2}x_3+\bar{x_1}\bar{x_3}$$
$$e=\bar{x_1}\bar{x_3}+x_2\bar{x_3}$$

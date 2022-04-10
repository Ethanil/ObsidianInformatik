---
aliases: 
---
# Gedächtnisprotokolle WS2021
[Quelle](https://demo.hedgedoc.org/Sqq8CdneR7GaUkZvdqXWnA)
Version vom 09.03.2022 13:45:
# Gedächtnisprotokoll - DT (WS2021)
###### ***[Aufgabe 1/10]*** 
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc13.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc14.png)
#### a) Wieviele Bits sind in 2 Nibble und wieviele Zustände lassen sich damit kodieren
> "4Bits x 2 = 8 Bits => 2^8 = 256"
#### b) min (und max) Darstellung in Vorzeichen-Betrag für b = 4, k = 3
> Formel $-(b^{k-1}-1)$
> $-(4^{3-1}-1)$=-15
#### c) Sicher das es c gab ?? 

> 
#### d) nenne 2 möglichkeiten dezimal in binär umzurechnen
> - Halbieren mit Rest (Horner-Schema)
> - Maximale Zweierpotenz abziehen (polyadisches Verfahren)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc15.png)
#### Tabelle mit dezimal binär und hexadezimal ausfüllen (Vorzeichenlos oder?)(3 Zeilen)
> "Erste Zeile: 126 in dezimal gegeben. In binär und hexa konvertieren"

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc16.png)
#### 33 zur Basis 5 - 66 zur Basis 9.  Rechnen in Oktal addieren 
> "Ergebnis = 78 (dezimal) beides erst in Oktal umwandeln - 33(5) = 18(dez) = 22(oktal)
> 66 (9) = 60 (dez) = 74(octal)"

----
###### ***[Aufgabe 2/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc18.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc1b.png)
#### a) Was ist der unterschied zwischen Transistoren und Logikgattern ?
> "Antwort"


#### b) Warum ist Transmissionsgatter besser als CMOS-Transistoren?
> Da sowohl 1 als auch 0 gut geleitet werden kann.


#### c) Was ist ein Pseudo-nMOS ? 
> Pull up Netz ist durch einen dauerhaft eingeschalteten pMos ersetzt.  
> Wird benutzt um große Anzahl an Transistoren zu verhindern.


![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc1a.png)
#### a) Wahrheitswertetabelle ausfüllen für $\overline{A+C}\oplus(AB+BC)$
> "Antwort"

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc1c.png)

#### a) CMOS beschriften und vervollständigen, pMOS war gegeben $(\overline{X} + \overline{Y} + \overline{Z})$. Funktion $\overline{((A + C) B)}$
> Antwort

#### (Tabelle ausfüllen für die Schaltung (fängt mit D-Latch/Flipflop? an. endet mit JK-Latch. Zwischen ein AND gate, Eingänge A = 0, B = 0, 3 Takte)) Glaube das ist am falschen Ort
> "Antwort"

----
###### ***[Aufgabe 3/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc1d.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc1e.png)
#### a) "Frage" (nicht sicher das es hier gehört): Was ist der Unterschied zwischen sequentiell und kombinatorisch (Bin mir sicher, dass man hier nur zu komb. Logik was erklären musste. Oder? xD). 

Das kam so weit ich weiß später <-- Genau, das sagt mir auch meine Erinnerung// Das ist in Aufgabe 6 
>.

#### c) Definiere Maxterm
>.

#### d) 2 Methode zum Beweis Theorem
>- Wahrheitswerttabelle
>- Umformungen mittels anderer Theoreme/Axiome

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc1f.png)

#### a) Boole'schen Ausdruck $\overline{(A + \overline{AB} + \overline{A} *\overline{B)}} + \overline{(A + B)}$ mit Axiomen und Theoremen vereinfachen zu $\bar{A} \bar{B}$.
> .

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc20.png)
#### a) "Frage" Karnaugh-Diagram mit 3 Eingänge (Maxterme bei 0,1,2,4) und Don't Cares bei 5,6)

> $\overline{Y}=\overline{B}+\overline{C}$
> $Y=BC$

//falscher Ort#### "Frage / glaub war was mit Decoder in Multiplexer umwandeln "
> "Antwort"

----
###### ***[Aufgabe 4/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc21.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc23.png)
#### a) Vor- Nachteile algorithmischer Logikminimierung mit "Exakt". 
> - Nachteil: Rechenzeit steigt exponentiell
> - Vorteil: Minimalste Lösung

#### b) Wobei ist Bubble Pushing hilfreich bei Logikminimierung? 2 Vorteile
> Weniger Inverter 
> Weniger Literale
> Wenige unterschiedliche Gatter (Einfacherere Zellbibliothek)
#### c) Was ist Störimpulse und wie lässt es sich erkennen (Nicht sicher ob am richtigen Ort)
> Karnaugh Diagramme und Timing Diagramme

#### d) Espresso lesen und in Funktion angeben. 
> Vorsicht!!! Wenn .ilb A B C D steht, muss die Wahrheitstabelle von rechts nach links gelesen werden. 
> Also wäre $10--$ nicht $A\overline{B}$ sondern $D\overline{C}$ .

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc24.png)
#### "Frage Zweistufige Logik. Gegeben ist eine Wahrheitstabelle. Daraus muss man dann eine Schaltung in zweistufiger Logik zeichnen.
> Also die DNF zeichnen.

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc25.png)

#### "Dekoder B3 -> B8, Eingänge A, B, C & Y = -A-BC + -ABC, A-BC, AB-C mit einem MUX B3 * B8 -> B darstellen"
> "Antwort"

----
###### ***[Aufgabe 5/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc2b.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc2f.png)
#### a) Stellen sie $11⋅x$ so da, dass es nur mit Shifts und möglichst wenigen Addierern realisierbar ist .
> "((2^3) +2^1 +2^0 )Shift x "
#### b) RCA sind langsam. Warum?  Warum ist ein CSA schneller?  
> Da der kritische Pfad des RCA sehr lang ist. Deshalb muss jeder Volladdierer auf den Übertrag des Vorherigen warten.
> Bei dem CSA wird jedes mögliche Ergebnis vorberechnet und dann nur noch was für diesem Fall richtige ausgewählt.
### c)
####  Wie kann man "A < B mit nur RCA und Invertern darstellen?"
> " Allgemein RCA darstellen und B Eingang invertieren. Wenn Ergebnis Negativ, dann A<B, wenn positiv A>B "
> A-B>0

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc33.png)
####  SystemVerilog Modul 

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc34.png)
#### "SystemVerilog das modul multi implementiern, input A,B als 2 bit breite vectoren output Y als 4 bit vektor *-Operator darf nicht verwendet werden"
> "Antwort"

----
###### ***[Aufgabe 6/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc36.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc37.png)
#### a) Was ist der Vorteil eines D-latch gegenüber SR-latch ? 
> "der fehlerhafte S=R=1 Zustand wird behoben bzw. existiert nicht im D-Latch"
> bzgl. der Version aus der Vorlesung: D-Latch ist durch CLK getaktet -> zeitliche Speichersteuerung

#### b) Warum lassen sich nicht alle Schaltungen kombinatorisch darstellen ?  
> - Da man kombinatorisch nichts speichern kann.
> - Zyklen können nicht dargestellt werden
> - kann nicht beliebig lang werden

#### c) 
> .


![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc39.png)
#### a) Schaltung mit JK-latch und SR-latch gegeben und man sollte für zwei Takte die Zustände von den latche und Y angeben. Nicht eher D-Latch? Dessen D-Eingang war a nand/nor b.
> Startzustände: a = 0,b=0,y=1  

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc3a.png)
#### a) D-latch mittels JK-Latch realisieren und Wahrheitstabelle ausfüllen
> "Antwort"

----
###### ***[Aufgabe 7/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc3c.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc3d.png)
#### a)Was ist Metastabilität
>undefinierter Zwischenzustand zwischen 0 und 1

#### b) Warum sollten Pipeline Stufen möglichst gleich lang sein ? 
>Latenz und maximale Clockfrequenz sind von der längsten Pipeline-Stufe abhängig


![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc3e.png)
#### Gegeben ist Schaltung in Pipelinestufen und durch Parallelität die Stufen minimieren.
> "Antwort"

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc3f.png)

#### Sequentielle Schaltung mit rechts links Registern gegeben. 
#### a) $t_{cd}$  berechnen
> "Antwort"
#### b)  $t_{pd}$ berechnen
> 250ps?
#### c) Timing-Bedingung prüfen thold
> war erfüllt?
#### d) Frequenz berechnen und in GHz angeben
> t_CLK >= 400ps -> f<=2.5GHz?

----
###### ***[Aufgabe 8/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc40.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc41.png)
#### a) Wobei sind Mealy-Automaten besser als Moore- (zwei Beispiele gefordert)
>in der Regel weniger Zustände nötig
>erkennt Signale in der Regel früher
#### b) Zwei Verfahren zur Kodierung von Zuständen. 
>binär (inkrementierend): S0=000, S1=001, S2=010, S3=011, ...
>One-Hot: S0=0001, S1=0010, S2=0100, S3=1000, ...
#### c) Beschrifte die allgemeine Zeichnung eines Moore Automaten 
> Wie auf der Folie im Skript. 
> Beschriftung mit next state logic, output logic

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc42.png)
#### a) Moore FSM zeichnen aus Code (3 Zustände. Y erfüllt in Zusatand 0)
> "module fsm( input logic A, B, input logic CLK, RST, output logic Y)
//sehr ähnlich zu Übung 8.1
> "

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc43.png)
#### a) Zustandsübergangs und Ausgangstabelle von gegebenem Mealy
> "Antwort"

----
###### ***[Aufgabe 9/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc44.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc45.png)
#### a) Klammern richtig setzen. 2 Funktionen  <<< A== B & C && ~& D? 
> "Antwort"
#### b) Zu welchem Zeitpunkt werden $always_{comb}$ ausgeführt. 
> .

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc46.png)
#### Parität Eingang A, Parameter W = 8, Ausgang Y. *-Operator darf nicht verwendet werden // das war doch bei der aufgabe mit dem A mit B multipizieren
> "Antwort"

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc47.png)
#### "Testbench aus Timing Diagramm?"
> "Antwort"

----
###### ***[Aufgabe 10/10]***
![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc48.png)

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc4a.png)
#### a) DRAM vs SRAM: Wie werden Daten gespeichert.
> " ca. sowas wie 
> DRAM: Durch Kondensatoren
> SDRAM: Durch kreuzgekoppelte invertierer "
#### b) "FPGA vs. ASIC. Ist Performance FPGA = Asic? "
> .
#### c) Berechnen wie viel Bit ein Speicherfeld speichern kann und in kibibyte angeben (10 Bit Addresse 8 Bit Wortlänge).


![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc4b.png)
#### "Punkte Bestimmen ROM im Logikfeld "
> "Antwort"

![](https://codimd.s3.shivering-isles.com/demo/uploads/82b70e92b64394561a287cc4c.png)
#### "LUT mit DECODE2 in Verilog implementieren und danach die Schaltung mit Nands umsetzen" 
> "Antwort"

----



---
aliases: 
---
# Gedächtnisprotokoll - CSS (WS2021/22)

## Aufgabe 1
### 1.1 
Multiple Choice (Richtig oder Falsch)
- ist DH Schlüsseltransferprotokoll?
- Ist die hybride Kryptographie lediglich die Kombinierung zweier kryptogrpahischen Verfahren
- Ist statische Redundanz, dass N Systeme laufen, N-1 davon im Standby und im Fehlerfall umgeschalet wird?
- Ist dynamische Redundanz, dass N Systeme laufen, und die Lösung durch Mehrheitsfindung bestimmt wird?
- Ist checkpointing, dass in regelmäßigen Abständen fehlererkennende Codes gespeichert werden?
- steht NONCE für "Non Changable Entity" (oder so ähnlich)
#
Reliabilityfunction herausfinden zu einem Graphen (1 zu 1 Aufgabe 8.1.1 aus SS 20, wenn ich micht nicht täusche)
#
Reliabilityfunction mit exponentiellem Modell zusammenfassen (1 zu 1 Aufgabe 8.1.2 aus SS 20, wenn ich micht nicht täusche)
#
Paritätsbits (entweder 1 zu 1 oder eine sehr ähnliche Aufgabe zu  8.1.2 aus SS 18) 
#
Availability bestimmen mit gegebener MTTF und MTTR (1 zu 1 Aufgabe 8.1.1 aus SS 18, wenn ich micht nicht täusche)
MTTF=20h, MTTR=5h56
## Aufgabe 2
### 2.1 
3 Schutzziele nennen erklären und Beispiel dazu geben (1 zu 1  Aufgabe 1.1 aus SS 20, nur mit 3 statt 2 Schutzzielen)
## Aufgabe 3
### 3.1 
Signatur bestimmen zu Hashwert und privatem Schlüssel
#
Verschlüsseln Sie die Nachricht m = 4 mit dem RSA Kryptosystem. Verwenden Sie dazu den öffentlichen Schlüssel (5, 459). Geben Sie Ihren Rechenweg mit an! (SS 18)
#
Betrachten Sie die diophantische Gleichung 963x + 3 y = 5. Hat diese Gleichung eine ganzzahlige Lösung? Begründen Sie Ihre Antwort! (aus SS 20)
#
Bestimmen Sie ein gültiges Schlüsselpaar ((e, n), (d, n)) für das RSA Kryptosystem mit den Parametern p = 5 und q = 11. Sie müssen keinen Rechenweg angeben sondern nur Ihre Ergebnisse für n, φ(n), e und d. Die Werte e = 1, d = 1 sind hierbei ausgeschlossen! (WS 19/20)
#
Bestimmen Sie in der zyklischen Gruppe Z^x_11 den diskreten Logarithmus von 4 zur
Basis 5. Zeigen Sie, dass Ihr Ergebnis korrekt ist. (aus SS 20)
# 
Bestimmen Sie mit dem erweiterten Euklidischen Algorithmus eine ganzzahlige Lösung
der diophantischen Gleichung 70x + 231 = 28. Geben Sie dabei Ihren Rechenweg mit
an. Ohne Rechenweg gibt es keine Punkte! (aus dem SS 18, schön copy pasted, ohne den Fehler zu korrigieren, mein persänliches Highlight der Klausur)
## Aufgabe 4
### 4.1 
CBC Blockchiffre (sieht fast 1 zu 1 nach Ausgabe 3.1.1 SS 20 aus)
#
Nennen und erläutern Sie jeweils einen Vorteil und einen Nachteil des CBC-Modus gegenüber des Electronic-Codebook-Modus (ECB-Modus) (kam unter anderem im SS 20 dran)
# 
Erläutern Sie die Bestandteile eines symmetrischen Kryptosystems (M, K, C, e, d) (auch aus SS 20)
# 
Was soll bei einem symmetrischen Kryptosystem für unterschiedliche Schlüssel k1 != k2
aber gleiche Nachricht m gelten? (aus aus SS 20)
# 
Auf welchem mathematischem Problem beruht die Schwierigkeit von RSA? Wie kann
RSA angegriffen werden, wenn dieses Problem gebrochen ist? (kam unter anderem auch im SS 20 dran)
# 
Auf welchem mathematischen Problem beruht die Schwierigkeit vom Diffie–Hellman?Wie kann  DH angegeriffen werden wenn dieses Problem gebrochen ist?
## Aufgabe 5
### 5.1 
Hasse-Diagramm
# 
Annahme: RBAC-Zugriffskontrolle
Gegeben: Hasse-Diagramm(????)
Bestimmen ob, eine Visualisierung eine partielle Ordnung ist und falls ja was sagt dies über die Rechte von A und B aus.
## Aufgabe 6
### 6.1 
Dynamische und statische Token erklären plus jeweils Beispiel
# 
TLS-Zertifikat, Challenge Response Protokoll und No-Write-Down und No-Readup-Regel (Bell La Padula) den Schutzzielen zuordnen
# 
bedeutet ein TLS Zertifikat, dass der entsprechende Server wirklich vertrauenswürdig ist?
## Aufgabe 7
### 7.1 
iterativen Auflösen DNS beschreiben anhand von Domain (welcher Nameserver wird von Resolver kontaktiert)
- Resolver will mit leerem Cache theoceancleanup.com kontaktieren. Welche Nameserver muss er dafür kontaktieren?
- Resolver will direkt danach die IP Adresse zu mx.theoceancleanup.com haben. Welchen Nameserver muss er dafür kontaktieren? begründen sie.
# 
alle 7 OSI-Schichten in richtiger Reihenfolge nennen können
# 
Beschreiben, ob DNS Cache poisoning im lokalen Wifi eines Restaurants möglich ist
## Aufgabe 8
### 8.1 SQL
#### 8.1.1
Als Bob anmelden ohne das man das Passwort kennt.
#### 8.1.2
Alle IDs aus der Relation ausgeben.
#### 8.1.3
Schwachstelle von DB nennen, die Passwörter im Klartext speichert und Verbesserungsmaßnahme (z.B. nen Salt)
### 8.2
XSS durchführen
Gegenmaßnahme zu XSS
persistent XSS skizzieren und Schritte erklären
### 8.3 (maybe)
- Was ist das besondere an Polymorphen Viren?
- Nennen sie eine technik um polymorphe Viren zu erzeugen
- ´Wieso sind polymorphe Viren schwerer zu erkennen als "normale" (oder so ähnlich)
### 8.4? maybe
BGP Routing. AS1 announced 1.1.0.0/16, AS3 hat route zu AS1 die über AS2 und AS4 geht (gleich lang, oder Route die über AS2 ging war sogar kürzer).
Welche Route & Prefixes muss AS4 announcen, damit sicher aller traffic von AS3 nach AS1 über AS4 geleitet wird?
die Reihenfolge der Aufgaben ist übrigens geraten, das passt nicht alles


## Links
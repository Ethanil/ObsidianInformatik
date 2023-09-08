---
aliases: 
---
# Char Encoding 
## Single Byte encoding
### American Standard Code for Information Interchange (ASCII)
Bei ASCII hat jeder char(aus der Tabelle) einen korrespondierenden 7-bit langen Binärcode. Es verwendet also immer genau 1 Byte, kann aber nicht alle chars encoden.
Das 1. bit in jedem byte ist eine 0
### ISO 8859-x / Windows Code pages (CP)
Verwendet die selben Zeichen wie ASCII, allerdings hat die obere Hälfte (mit 1. bit  = 1) auch eine Bedeutung
## Multi Byte encoding
### Unicode
Die Idee hinter unicode ist ein character set zu haben, das alle chars beschreiben kann.
Dabei werden ***21*** signifikante bits verwendet, also 4 bytes.
### UTF-32/UCS-4 Encoding
Jeder char wird genau mit 4 bytes encoded, korrespondierend zu seinem unicode-code

### UCS-2 Encoding
Jeder char wird genau mit 2 bytes encoded. Dadurch können nur die "häufigsten" chars encoded werden (nur die Basic Multilingual Plane(BMP))

## Variable length encoding
### UTF-16 Encoding
Jeder char wird hierbei mit 2-4 bytes encoded.
Es gibt eine direkte Korrespondenz zu unicode codes. Wenn dies nicht möglich ist, teilen wir den code in ein high und ein low surrogate auf.
Wir ziehen zuerst `1 0000 0000 0000 0000` (also `4*4` 0en und eine 1) von unserem unicode code ab
Dann teilen wir die hinteren `20` bit in `2*10` bit auf. Die vorderen sind dann Teil unseres high-surrogate und die hinteren Teil unseres low-surrogates.
vor den high surrogate schreiben wir dann noch `11011 0` und vor den low-surrogate `11011 1` und sind fertig.
### UTF-8 Encoding
Jeder char wird hiebrei mit 1-4 bytes encoded.
Es gibt eine direkte Korrespondenz zu ASCII, wobei nicht ASCII-chars weitere bytes benötigen.
Wir gehen wie folgt vor:
1. Wir überprüfen, ob es ein ASCII-code ist (also 7 bits)
	- Wenn ja übernehmen wir dies und sind fertig
2. Wenn nein, brauchen wir mindestens 2 byte, wobei wir 3 bit zum encoden der länge benötigen, also noch 5 bit "frei" haben in unserem linkesten byte
3. Wir "schneiden" die rechten 6 bit von unserem code raus, schreiben davor `10` und  und überprüfen ob die restlichen bit in unsrere "freien" bit passen
	- Wenn ja übernehmen wir diese

## Links
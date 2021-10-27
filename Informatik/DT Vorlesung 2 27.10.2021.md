# [[Digitaltechnik]] Vorlesung 2 27.10.2021
## Buch: Kapitel 1.4-1.5
## Zahlensysteme: Bitfolgen <-> (ganze) Zahlen
### Basen
#### Dual/Binär
$$0b11010011$$
#### oktal
$$0o323$$
#### dezimal
$$0d211$$
#### hexadezimal
$$0x49AF$$
### Zweierkomplement
Um Zahlen in Computern darzustellen (bspw einen [[integer]]) legen wir das erste Bit als eine sehr hohe negative Zahl fest $-1*a$, wobei $a$ die höchste mit einem Bit darstellbare Zahl ist, und addieren darauf alle anderen Zahlen, dadurch ist die 0 nicht doppelt belegt. 
#### Beispiel:
Eine 8-Bit Zahl kann damit Werte von $-2^8$ bis $2^8-1$ darstellen. 
$$1000 0000$$
wäre dann $-128$, größere negative Zahlen kann man dann wie folgt darstellen:
$$1000 1100$$
wäre $-128 + 12 = -116$
## Logikgatter: Einfache Boole'sche Funktionen

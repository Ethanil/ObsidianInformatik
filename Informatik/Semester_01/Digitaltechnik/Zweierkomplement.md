# Zweierkomplement
Um Zahlen in Computern darzustellen (bspw einen [[integer]]) legen wir das erste Bit als eine sehr hohe negative Zahl fest $-1*a$, wobei $a$ die höchste mit einem Bit darstellbare Zahl ist, und addieren darauf alle anderen Zahlen, dadurch ist die 0 nicht doppelt belegt. 
## Beispiel:
Eine 8-Bit Zahl kann damit Werte von $-2^8$ bis $2^8-1$ darstellen. 
$$1000\text{ }0000$$
wäre dann $-128$, größere negative Zahlen kann man dann wie folgt darstellen:
$$1000\text{ }1100$$
wäre $-128 + 12 = -116$, da $(1100)_2=12$. Um positive Zahlen darzustellen, lassen wir die erste Zahl "weg":
$$0100\text{ }0000$$
wäre $2^7=64$ um noch größere Zahlen darzustellen, füllen wir die restlichen Stellen mit Einsen auf:
$$0111\text{ }1111$$
Dies wäre $2^7+2^6+2^5+2^4+2^3+2^2+2^1+2^0=2^8-1=127$
## Addition
Durch das Zweierkomplement können wir intuitiv Zahlen miteinander addieren.
## Zahlen negieren
Um Zahlen zu negieren, "kippen" wir alle Bits einmalig:
$$(0000\text{ }0101)_2=5$$
$$(1111\text{ }1010)_2=-5$$
---
aliases: 
---
# Vorlesung 3 
## Perfekte Sicherheit

```ad-abstract
title:Definition - Perfekte Sicherheit
Bei gegenemen Chiffretext ist **jeder** Klartext gleichwahrscheinlich
```

```ad-abstract
title:Definition - Semantische Sicherheit
Es ist nicht wesentlich einfacher auf den Inhalt einer Nachricht zu schließen, wenn man die Länge der Nachricht+Chiffrat hat, als wenn man nur Länge der Nachricht hat.
```
## Chiffren
```ad-abstract
title:Definition - Vignere-Chiffre
Ceasar-Chiffre mit repetitierendem Key
```

```ad-abstract
title:Definition - Blockchiffren
| Name | Bedeutung |
| ---- | --------- |
|  ECB    | Blockchifre, wobei der key einfach auf jeden Block angewendet wird          |
|  CBC    |Wir haben noch einen init-vector(IV). Wir xor'n den block damit und verschlüsseln dann mit key. IV für nächsten Block ist der verschlüsselte Block.|
|  CTR    | Wir verschlüsseln Nonce+Counter und xorn das mit Block  |
```

```ad-abstract
title:Definition - Stromchiffre
Wir haben einen Strom aus Schlüsseln, mit denen wir jeweils Teile des Plaintextes verschlüsseln (CTR ist eine Stromchiffre)
```
## Links
[[Vorlesung 4]]
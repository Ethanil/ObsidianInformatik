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

```ad-abstract
title:Definition - Vignere-Chiffre
Cesar-Chiffre mit repetitierendem Key
```
## Blockchiffre
```ad-abstract
title:Definition - ECB
Blockchifre, wobei der key einfach auf jeden Block angewendet wird
```

```ad-abstract
title:Definition - CBC
Wir haben noch einen init-vector(IV). Wir xor'n den block damit und verschlüsseln dann mit key. IV für nächsten Block ist der verschlüsselte Block.
```

```ad-abstract
title:Definition - CTR
Wir verschlüsseln Nonce+Counter und xorn das mit Block
```

## Stromchiffre
Wir haben einen Strom aus Schlüsseln, mit denen wir jeweils Teile des Plaintextes verschlüsseln (CTR ist eine Stromchiffre)
## Links
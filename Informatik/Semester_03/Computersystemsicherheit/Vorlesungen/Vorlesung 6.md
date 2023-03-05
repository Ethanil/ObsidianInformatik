---
aliases: 
---
# Vorlesung 6 
```ad-abstract
title:Definition - Zertifikat
Beinhalten üblicherweise Öffi, Name, Gültigkeitszeitraum, Aussteller, ... und kommt von einer vertraueneswürdigen dritten Partei.

Wird mit einer digitalen Signatur versehen.
```

```ad-abstract
title:Definition - Web of Trust (PGP)
Jeder vertraut jedem, den er kennt und jedem den jeder kennt den er kennt.
```
## Needham-Schroeder
- $A \rightarrow T$: $A,B,N_{A}$
- $T \rightarrow A$: $\{N_{A},K,B,\{K,A\}_{K_{B}}\}_{K_{A}}$
- $A \rightarrow B$: $\{K,A\}_{K_{B}}$
- $B \rightarrow A$: $\{N_{B}\}_{K}$
- $A \rightarrow B$: $\{N_{B}-1\}_{K}$

## Links
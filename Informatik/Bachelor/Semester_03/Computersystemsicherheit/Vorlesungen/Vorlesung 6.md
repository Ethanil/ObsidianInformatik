---
aliases: 
---
# Vorlesung 6 
```ad-abstract
title:Definition - Zertifikat
Beinhalten üblicherweise Öffi, Name, Gültigkeitszeitraum, Aussteller, ... und kommt von einer vertraueneswürdigen dritten Partei.

Wird mit einer digitalen Signatur versehen.
CRL: Zertifikatsperrlisten (negativer check)
OCSP: Online Certificate status protocol (positiver check)
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
## Diffie-Hellman
Jeder hat eine geheime Farbe. Jetzt wird eine gemeinsame Farbe gewählt und diese jeweils mit der eigenen gemischt. Diese Farbmischung wird an den jeweils anderen übertragen (Annahme: Farben "ent"-mischen ist schwer). Jetzt einfach zur Farbmischung des anderen die eigene Farbe dazu und wir sind fertig. ${(g^{a})}^{b}=g^{a*b}={(g^{b})}^{a}$ 
## Station-to-Station
DH hat MITM-Problem, Lösung ist verschlüsselung durch asymetrische verschlüsselung+signatur
- $A \rightarrow B$: $g^{a}$
- $B \rightarrow A$: $g^{b},\{sig(sk_{B},(g^{a},g^{b}\}_{K}$
- $A \rightarrow B$: $\{sig(sk_{A},(g^{a},g^{b}))\}_{K}$
## Links
[[Vorlesung 7]]

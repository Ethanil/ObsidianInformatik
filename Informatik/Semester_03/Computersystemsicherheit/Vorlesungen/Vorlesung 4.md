---
aliases: 
---
# Vorlesung 4 
## RSA
$$\begin{align}
n &= p*q \\
\varphi(n) &= (p-1)*(q-1) \\
ggT(e,\varphi(n)) &= 1 \land 1 \neq e \\
e*d \text{ mod } \varphi(n) &= 1
\end{align}$$
## ElGamal
- nehme zyklische Gruppe $G$ mit Erzeuger $g$
- wähle $a$ aus dem Restklassenring (privater Schlüssel!)
- berechne $g^{a}= e$ => Öffentlicher Schlüssel ist $(G,g,e)$
- Verschlüsseln wähle Zahl $r$ aus $G$
- Berechne $g^r=R$, damit können wir verschlüsselt unser $r$ mitgeben 
- $K=e^r$ berechnen
- Berechne $C = m * K$ und gebe $(R,C)$ als Chiffrat mit
- Entschlüsseln: $K = R^a$ und $C*K^{-1} = m$

## HMAC
wir wählen
- opad ist $(0x5C)^{n}$ und ipad ist $(0x36)^{n}$ aus $\mathbb{Z}^{8n}_{2}$
- Einen Key $K$ abhängig vom übergebenem $k$(entweder fügen wir $0$'en hinzu, hashen $k$ oder übernehmen $k$ direkt als $K$)
- $x$ ist die zu hashende Nachricht, $H$ die Hashfunktion
```ad-abstract
title:Definition - HMAC
$$HMAC(x,k) = H(\text{conc}(K \oplus opad, H(\text{conc}(K \oplus ipad,x))))$$
```
## Links
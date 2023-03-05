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
## Links
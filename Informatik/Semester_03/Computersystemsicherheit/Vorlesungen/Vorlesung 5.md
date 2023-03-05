---
aliases: 
---
# Vorlesung 5 
## Angriffszeug
### Wissen
- Key-Only Attack: Angreifer kennt nur öffi
- Known Signature Attack: Angreifer kennt mehrere Signatur-Nachrichten-Paare
- Chosen Message Attack: Angreifer kann für selbstgewählte Nachrichten die Signatur generieren lassen
- Adaptive Chosen Message Attack Angreifer kann während des Angriffs noch für beliebige Nachrichten Signaturen erhalten
### Ziele
- Existential Forgery: Ein neues gültiges Nachrichten-Signaturen-Paar
- Selective Forgery: Gültige Signatur zu einzelnen neuen Nachrichten, wobei diese schon vor dem Angriff bekannt sind
- Universal Forgery: Gültige Signaturen zu jedem beliebigen Dokument
- Total Break: Angreifer bestimmt den geheimen Schlüssel

## DSA
### Parametergenerierung
- 2 Primzahlen $q$ und $p$ wählen, sodass $q|(p-1)$ gilt
- suche ein $g$ mithilfe von einem $h$, sodass $g:= h*\frac{p-1}{q}\text{ mod } p \neq 1$ gilt
### Schlüsselgenerierung
- Wähle privater Schlüssel $x$ mit $1<x<q$
- Berechne öffentlicher Schlüssel $y = g^{x}\text{ mod }p$
### Signieren
- Wähle $k$ mit $1<k<q$
- Bestimmte $r = (g^{k}\text{ mod }p)\text{ mod }q$ Falls $r = 0$, restart
- Bestimme $s = k^{-1}*(H(m) + r*x)\text{ mod }q$ Falls $s = 0$, restart
- Signatur ist $(r,s)$
### Verifizieren
- Ungültig, wenn $0<r<q$ oder $0<s<q$ nicht gilt
- Berechne $w = s^{-1}\text{ mod }q$
- Berechne $i_{1}=H(m)*w \text{ mod }q$
- Berechne $u_{2}=r*w \text{ mod }q$
- Berechne $v = (g^{u_{1}}*y^{u_{2}}\text{ mod }p)\text{ mod }q$
- Falls $v=r \Rightarrow$ akzeptiert
## Links
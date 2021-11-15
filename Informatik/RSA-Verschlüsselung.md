# RSA-Verschlüsselung

Mithilfe des [[Der kleine Satz von Fermat|kleinen Satzes von Fermat]] können wir eine relativ einfache Verschlüsselung durchführen die solange funktioniert, solange eine [[Primfaktorzerlegung]] großer Zahlen nicht schnell berechnet werden kann.

## Vorbereitung
1. Alice wählt zwei (große) Primzahlen $p$ und $q$ mit $p \neq q$ und brechnet $n=p\cdot q$ und $N=(p-1)\cdot (q-1)$
2. Alice wählt ein $e \in \mathbb{N}$ mit $ggT(e,N) = 1$ und bestimmt dann ein $x \in \mathbb{N}$ mit $ex\equiv 1 \ (mod \ N)$
3. Alice schickt unverschlüsselt und frei zugänglich das Zahlenpaar $(n,e)$ an Bob, das ist ihr sogennanter Public Key.
Damit können Nachrichten $M \in \mathbb{N}$ mit $M<n$ verschlüsselt werden.
## Verschlüsseln
Bob rechnet $M':=M^e \ mod  \ n$ und schickt das Ergebnis an Alice.
## Entschlüsseln
Alice rechnet $M'':=(M')^x \ mod \ n$
Zum Entschlüsseln verwendet Alice ihren Private Key $(n,x)$. Da nur sie diesen kennt, kann nur sie die Nachricht entschlüsseln.
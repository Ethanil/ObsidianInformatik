Wir wollen die maximale Hyperebene erzeugen, in der die Werte keiner Klasse zugeordnet werden.
Wir definieren hierbei die eine Klasse als $1$ und die andere Klasse als $-1$, woraus folgt, dass die Werte die keiner Klasse zugeordnet werden, den Wert $0$ erhalten.
Die Größe der beiden Grenzen $x_{1}$ und $x_{2}$ sollen also in abhängingkeit unserers Vektors $w$ $2$ ergeben, bzw $\frac{2}{||w||}$, falls wir den normalisierten Vektor $\frac{w}{||w||}$ verwenden.

Wir wollen also $\frac{2}{||w||}$ maximieren, während $y_{i}(<w,x_{i}>+b)\geq 1,\forall i$ wahr bleibt. Dies können wir zu einem minimierungs-Problem umformulieren, sodass wir $\frac{1}{2}||w||^{2}$ erhalten.

Unsere Daten sind idR nicht linear seperierbar, also müssen wir unsere Bedingung mithilfe von $\xi$ kontrolliert aufweichen, wir haben also als Bedingung nun $y_{i}(<w,x_{i}>+b)\geq 1-\xi_{i},\xi_{i}\geq 0,\forall i$, während wir so wenig Fehler wie möglich zulassen wollen, wir minimieren also zusätzlich noch den Durchschnitt von $\xi_{i}$
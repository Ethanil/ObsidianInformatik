Der Informationsgehalt einer Zufallsvariable $E$ mit der Auftrittswahrscheinlichkeit $P(E)$ ist
$$I(E) = \log \frac{1}{P(E)}=-\log P(E)$$
Das heißt, falls $P(E)=1$ dann folgt daraus $I(E)=0$, also $E$ trägt keine Information.

Die Entropie $H$ einer Quelle mit den Symbolen $i$ und deren Auftrittswahrscheinlichkeit $p_{i}$ ist nun dieser Informationsgehalt, allerdings aufsummiert für die ganze Quelle:
$$H = -\sum_{i}p_{i}\cdot \log_{2}(p_{i})$$

Mithilfe dieser Formel kann man die minimale Länge einer kodierten "Nachricht" herausfinden unter der Annahme, dass die verwendeten Symbole statistisch unabhängig sind.
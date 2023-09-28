Die Idee vom Huffman Code ist es Codewörter variabler Länge zu verwenden, anstatt einer fixer Länge. Dabei werden Zeichen, die häufiger vorkommen, also eine größere Wahrscheinlichkeit haben, mit kürzeren Codewörtern repräsentiert.
Den Code erzeugen wir, indem wir die Wahrscheinlichkeiten der Symbole so lange kombinieren, bis wir nurnoch 2 Wahrscheinlichkeiten übrig haben.
![[Pasted image 20230928111249.png# left 1/2 shadow|Wir kombinieren die Wahrscheinlichkeiten]]

Danach vergeben wir für jede Wahrscheinlichkeit jeweils einen Code:
![[Pasted image 20230928111349.png# left 1/2 shadow| wir gehen Rückwärts vor und vergeben jeweils einen Code]]
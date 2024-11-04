---
aliases: 
---
# IR Evaluation 
Bei der [[Information Retrieval]] Evaluation geht es darum einzuschätzen, wie gut das System ist.
Wir verwenden dafür zum einen die Präzision(Precision) und den Recall.
```ad-abstract
title:Definition - Precision
Präzision ist der Teil der Dokumente, der wirklich retrieved wurde und relevant für den Nutzer ist
$P = \frac{\text{retrieved } \cap \text{ relevant}}{\text{retrieved}}$
```
```ad-abstract
title:Definition - Recall
Recall ist der Teil der relevanten Dokumente, die retrieved wurden
$P = \frac{\text{retrieved } \cap \text{ relevant}}{\text{relevant}}$
```

## Confusion matrix
|               | Relevant | Irrelevant | $\Sigma$ |
| ------------- | -------- | ---------- | -------- |
| Retrieved     | TP       | FP         | SUM      |
| Not retrieved | FN       | TN         |          |
| $\Sigma$      | SUM      | SUM           |          |
TP = True Positives
FP = False Positives
TN = True Negatives
FN = False Negatives
## $F_{1}$ Score
Der $F_{1}$ Score beschreibt den gewichteten Durchscnitt von Präzision und Recall:
$F_{1} = \frac{2PR}{P+R}$
## Links
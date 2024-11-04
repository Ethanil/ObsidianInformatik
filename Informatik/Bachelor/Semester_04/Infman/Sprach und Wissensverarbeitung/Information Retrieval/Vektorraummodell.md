---
aliases: 
---
# Vektorraummodell 
Beim Vektorraummodell teilen wir jedem Dokument und jeder Query einen Vektor zu und vergleichen wie ähnlich diese sind. Daraufhin können wir ein [[Ranked Retrieval]] machen.

## Bag of Words vs Set of Words
Bei beiden ist die Reihenfolge, Grammatik oder Bedeutung egal, allerdings wird bei der Menge überprüft, ob ein Wort vorkommt oder nicht und beim Bag wie häufig der Term vorkommt.
## Vektorbildung
### Term Frequencies TF
Wie oft das Wort im Dokument vorkommt
### Normalized TF
$\log(tf_{d}(t))+1$
### Document Frequency
In wievielen Dokuemten das Wort mindestens einmal vorkommt.

### Inverse Document Frequency
$idf(t) = log(\frac{\text{\#documents}}{df(t)})$ 
### TF.IDF
$TF.IDF = \log(tf_{d}(t))+1 \times idf(t)$
## Links
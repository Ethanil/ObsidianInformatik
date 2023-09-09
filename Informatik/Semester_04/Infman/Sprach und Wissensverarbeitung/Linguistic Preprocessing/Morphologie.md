---
aliases: 
---
# Morphologie 
Wörter können häufig in kleinere Bestandteile aufgeteilt werden.
Morphologie ist die Lehre der Wortformen und der Wortbildung.
Der kleinste Bestandteil eines Wortes, in das er aufgeteilt werden kann, heißt Morphem.
## freie Morpheme
Ein freies Morphem ist ein Morphem, dass auch dann eine Bedeutung hat, wenn man es einzeln ausspricht. bspw. `frei`

## Gebundene Morpheme oder Affixe
Ein Affix ist ein Morphem, welches nicht frei ist und daher nur gebunden mit anderen Morphemen auftauchen kann `-e` von `frei-e`

| Art des Affix | Ort des Auftauchens      | Beispiel       |
| ------------- | ------------------------ | -------------- |
| Suffix        | hinter der Basis         | frei-e         |
| Prefix        | vor der Basis            | un-frei        |
| Infix         | innerhalb der Basis      | ein-ge-schoben |
| Circumfix     | Vor und hinter der Basis | ge-sag-t               |

## Wortbildung
Worte können auf verschiedene Arten gebildet werden.
### Derivation
Neue Wörter werden aus freien morphemen und einem affix gebildet, wie bspw schau-en
### Konversion
Ein Wortstamm wird ohne Änderung der Form in eine andere Wortart konvergiert wird: schauen -> die Schau
### Komposition
Neue worten werden aus mehreren freien Morphemen und Fugenlauten gebildet, wie bspw. Schnee-ball
#### Dekomposition
Bei der Dekomposition wird versucht die Komposition Rückgängig zu machen, allerdings ist dies nicht immer möglich:
Scheeball -> Schee und Ball
aber
Kulturteilen -> Kultur und teilen / Kult und Urteilen

## Normalisation
Da Wörter häufig [[Flexion|flexiert]] sind, müssen wir sie normalisieren um ihren Wortstamm zu finden.

### Stemming
Beim Stemming wird das Ende von Wörtern anhand von festgelegten Regeln entfernt.
Gestemmte Wörter müssen dabei keine wirklichen Wörter sein.
Es werden beispielsweise Endungen wie `e` oder `ity`entfernt.
#### Stemming Errors
Beim Stemming können verschiedene Fehler auftreten
##### Under-stemming
Hierbei werden Wörter die gestemmt werden nicht zum selben stamm verändert:
adhere -> adher
adhesion -> adhes
##### over-stemming
Hierbei kann das Stemming nicht zwischen wirklich unterschiedlichen Wörtern unterscheiden:
appendicitis -> append
append -> append
##### Mehrdeutigkeit
Wörter, die mehrere Bedeutungen haben, kann der Wortstamm nicht herausgefunden werden (saw(sehen) vs saw(säge))

### Lemmatisierung
Bei der Lemmarisierung machen wir die Flexion des Wortes rückgängig und erhalten so den wirklichen Wortstamm.
Dafür brauchen wir zusätzlich zu dem Wort auch mehr Kontext z.B. ob es ein Verb oder ein Nomen ist.
Außerdem muss es mit unregelmäßigen Formen zurecht kommen z.B. laufen -> lief

## Links
---
aliases: 
---
# Syntax 
Syntax beschreibt wie Wörter im Verhältnis zueinander vorkommen. Es gibt unendlich Möglichkeiten wie man mit Wörtern Sätze bilden kann und als Mensch können wir ohne Probleme Sätze verstehen, die wir zum ersten mal hören.
## Part of Speech Tagging(POS tagging)
Beim POS Tagging wird jedem Wort ein POS bzw Wortart-Marker hinzugefügt.

| Abkürzung | Ausgeschrieben | Beispiel           |
| --------- | -------------- | ------------------ |
| N         | Noun           | Stuhl              |
| V         | Verb           | studieren          |
| ADJ       | Adjective      | lila               |
| ADV       | Adverb         | krächzend          |
| P         | Preposition    | in, um             |
| PRO       | Pronoun        | Ich, Mich          |
| DET       | Determiner     | der, die, das, ein |

Die Menge an Tags ist unterschiedlich für unterschiedliche Sprachen.
POS-Tags geben wertvolle Informationen:
- Der Wortstamm: Wichtig für [[Morphologie#Lemmatisierung|Lemmatisierung]] oder andere Morphologische Analyse
- Das Wort und die möglichen Nachbarn: Wichtig für Sprachmodelle
- Die korrekte Aussprache: Wichtig für Sprachsynthese
- Der gemeinte Sinn: Wichtig bei Mehrdeutigkeit
- Der Sinn eines Satzes: Wichtig für Shallow parsing

### Umsetzung
#### Regelbasiertes Tagging
Verwende eine Tabelle in der Wörterbuchform -> pos tag steht. Verwende dann noch eine geordnete Menge an Transformationszegeln um die Genauigkeit zu verbessern. Für dann noch unbekannte Wörter verwenden wir die häufigsten Tags
#### Wahrscheinlichkeits Tagging
Schätze die Wahrscheinlichkeit, dass ein Wort ein spezifischer tag bekommen würde und nehme den wahrscheinlichsten. Die Wahrscheinlichkeiten wurden mittels manuell erstellten Trainingsdaten gelernt.
## Parsing
Beim parsing finden wir die grammatikalische Struktur eines Satzes heraus. 
Eine Art der Grammatik ist die Phrasenstrukturgrammatik, bei der ein Satz in Konstituente aufgeteilt wird. Eine Konstituente ist eine Gruppe von Wörtern die sich wie eine Einheit verhalten. In Phrasenstrukturgrammatik sind dies zumeist Phrasen.
### Phrasen

| Phrase                    | Beschreibung                  | Beispiel                 |
| ------------------------- | ----------------------------- | ------------------------ |
| Noun Phrase(NP)           | Hat ein Nomen als Kopf        | die schwarze ***Katze*** |
| Prepositional phrase (PP) | Hat eine Preposition als Kopf | ***in*** der Schule      |
| Verb Phrase(VP)           | Hat ein Verb als Kopf         | Er ***tanzt***           |
| Adjectival Phrase (AP)    | Hat ein adjektiv als Kopf     | ***voll*** mit Spielzeug |
| Adverbial phrase (AdvP)   | Hat ein Adverb als Kopf       | ***springend***                         |

#### Phrasenkopf vs Modifizierer
Ein Kopf einer Phrase ist das Schlüsselwort dieser phrase, wobei ein Modifizierer ein optionales Element der Phrase ist, welches diese modifiziert.

## Mehrdeutigkeit
### Attachment ambiguity
Ein Konstituent kann im parse-baum an verschiedenen Stellen stehen.
`ich hab den den Elefant in meinem Schlafanzug erschossen`
### Coordination ambiguity
Nicht eindeutiger scoope von konjunktionen.
`Schwarze Katzenund Hunde spielen gerne`

### Garden path sentences
Die offensichtliche 

## Links
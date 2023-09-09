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


## Links
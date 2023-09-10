---
aliases: 
---
# Text Corpus 
Ein Text Corpus ist eine Sammlung von texten mit dem ein System trainiert oder evaluiert wird.

## Beispiele für Text Corpus
### Brown Corpus
Der Brown Corpus ist eine Sammlung von Dokumenten aus 1961. Bestehend aus 15 Genres, 500 Texten und ~1kk Wörtern.
### Common Crawl
Hierbei wird das Internet gecrawled und dabei eine menge Daten(auch kopierrechtlich geschützte Daten) gesammelt.
## Parallel Corpora
Parallel Corpora ist eine besondere Art des Corpus, bei dem das Dokument in mehr als einer Sprache vorliegt. Dadurch können Übersetzungen ermöglicht werden.

| Parameter           | Beschreibung                                          | Beispiele                                         |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------- |
| Language            | Die Sprache des Corpus                                | Mono-/Multi-lingual/Parallel                      |
| Communication       | Die Art des Corpus                                    | Written/Spoken/Mix                                |
| Size                | Die Größe                                             | Joooaaa                                           |
| Annotations         | Hat es Annotations                                    | POS-Tagging                                       |
| Static vs. Dynamic  | Ob der Text sich nicht mehr ändert oder im wandel ist |                                                   |
| Genre/Text type     | Das Genre des Textes                                  | Nachrichten, Bücher, Social media text, Gespräche |
| Domain/Topic        | Das Umfeld in das der Corpus gehört                   | Biologie, Informatik, ...                         |
| Time of compilation | Die Zeit                                              | 1961, 2023, gestern                               |
## Corpus Annotation
Erweitern den Corpus um verschiedene Informationen. Diese kann man verschiedenen Leveln zuordnen
- Wörter (POS)
	- Benötigen die [[Segmentation]] des Textes
- Phrase (benannte Entitäten)
- Sentence (Satzgrenzen)
- Discourse (Koreferenz links)
Annotations zu erzeugen ist teuer und dauert viel Zeit (ist das nicht das gleiche?)

### Einfacher Erschaffungs Workflow
- Hole und speichere Quelldokumente
- Transformiere die Dokumente in Text, gleiche encodings an etc
- [[Segmentation]]
- Erschaffe annotations (manuell oder automatisch)
- Speichere die Erschaffenen Daten in einen wiederverwendbaren Format
- Analysiere oder verwende den Corpus

### Annotations speichern
Man kann Annotations auf verschiedene Arten speichern, inline(im selben text) oder stand-off(in einer seperaten datei) bspw.

### IOB Annotation
Wird verwendet um annotationen, die über mehrere Wörter gehen zu speichern, bspw [[Informatik/Semester_04/Infman/Sprach und Wissensverarbeitung/Linguistic Preprocessing/Syntax#Phrasen|Nomen-Phrasen]]. 

## Warum Korpora verwenden?
Korpora erlaube Beispiele aus der echten Welt zu verwenden und damit einen Blick auf was üblich ist. Unter der Annahme, dass alle Teile des Lebens gleichmäßig Dokumentiert werden ist es ein guter Blick auf eine Sprache und kürzliche Änderungen in dieser.

## Links
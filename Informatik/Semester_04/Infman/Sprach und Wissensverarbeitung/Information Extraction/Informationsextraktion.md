---
aliases: 
---
# Informationsextraktion 
Bei der Informationsextraktion soll bei einem gegebenen Dokument strukturiertes Wissen extrahiert werden.

## Extraktion vs [[Information Retrieval|Retrieval]]
Bei retrieval wird das Dokuemtn zurückgeliefert, was die relevanten Daten enthält, bei der Extraktion sollen strukturierte Muster erkannt werden.

| Extraktion                                                                           | Retrieval                                                                               |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Output ist eine Menge an strukturierten Fakten, die von Dokumenten extrahiert wurden | Output ist eine Liste relevanter Dokumente                                              |
| Schwerer als Retrieval                                                               | Einfacher als Extraktion                                                                |
| Domänen-Abhängig                                                                     | Domänen-unabhängig                                                                      |
| Vordefinierte Nachfrage-Typen([[Anfragesprache SQL\|SQL]])                           | meistens nicht vordefinierte Nachfrage-Typen                                            |
| Langsamer                                                                            | Schneller                                                                               |
| Effizienter für die unterstützten Nachfragetypen                                     | Weniger effizient, da der Nutzer zumeist Informationen und nicht Dokumente haben möchte |

## Probleme der Extraktion
- Entity vs Non-Entity
	- Mobile kann ein Telefon oder eine Stadt sein, was wenn wir infos zur Stadt geben wollen?
- Abdeckungs-Problem
	- Es ist unmöglich alles abzudecken
- Variations-Problem
	- Es gibt quasi unendliche Variationen von etwas (John Smith vs Mr. Smith)
- Mehrdeutigkeit
	- Darmstadt (Deutsche vs Amerikanische Stadt)
- Zeitabhängig
	- Wer ist Bundeskanzler? (Scholz, Merkel, wer ganz anderes?)
- Mehrwortausdrücke
	- Trennen wir die Wörter auf um sie zu extrahieren oder müssen sie zusammen bleiben?
- Metonymie
	- Wenn ein Wort in einem gewissen Kontext etwas anderes bedeutet, als es normalerweise bedeutet (Darmstadt hat das Spiel gewonnen -> Hier ist SV Darmstadt 98 gemeint)

## List Lookup Herangehensweise
Hierbei werden nur Entitäten berücksichtigt, die in gewissen Listen gespeichert sind.
### Vorteile
- Schnell
- Einfach
- Einfach anpassbar an andere Domäne
### Nachteile
- Sammeln und Instanthaltung der Listen
- Kann mit Namensvarianten und Abkürzungen nicht umgehen
- Kann Mehrdeutigkeit nicht auflösen

## Regel-basierte Herangehensweise
Hierbei werden gewisse Regeln verwendet um Daten zu extrahieren.
Anfangs wurden diese Regeln per Hand definiert, allerdings wird dies mittlerweile anders gemacht:
- Überwachtes Maschinenlernen
	- Hierbei wird ein Datenset mit labeln erschaffen und die Machine erlent anhand diesem das Extrahieren
- [[Text Corpus|Korpus]] basierte Wahrscheinlciehkeitsmodelle
	- Hierbei wird die Wahrscheinlichkeit anhand eines großen Text-Korpus geschätzt

## Speicherung
Nachdem wir die Informationen extrahiert haben, müssen wir diese speichern. Dies tun wir in einer `Knowledge base`, bspw in Form eines `Knowledge Graphen`.
In diesem ist eine Kollektion an Fakten. Fakten sind binäre Beziehungen.
### Knowledge Graph
#### Erschaffung
##### Curated approach
Die Tripel werden hierbei per Hand angelegt, was zu hoher Qualität aber niedriger Skalierbarkeit führt
##### Collaborative Herangehensweise
Die Tripel werden von einer offenen Gruppe an Freiwilligen angelegt, was zwar zu einer besseren Skalierbarkeit führt, diese ist aber immernoch limitiert.
##### Automatisierte, semistrukturierte Herangehensweise
Die Tripel werden hierbei automatisch von semi-strukturierten Texten extrahiert, was zu großen Graphen führt, allerdings nur einen kleinen Teil des Webs abdeckt
##### Automatisierte unstrukturierte Herangehensweise
Die Tripel werden hierbei automatisch von unstrukturiertem Text extrahiert, was zu riesigen Graphen führt!

## Links
---
aliases: 
---
# Boolean Retrieval 
Bool'sche Suche ist die simpleste Art und Weise für [[Information Retrieval]]. Ein Dokument wird hier als eine Menge an Wörtern betrachtet. 
Für die Suche wird in der Menge dann geschaut
- Enthält es das Wort?
- Enthält es das Wort nicht?
- Enthält es Wort1 und Wort2?
- Enthält es Wort1 oder Wort2?

## Scaling
Bool'sche Suche skaliert sehr schlecht, wenn wir naiv an das Problem herangehen und sowohl die enthaltenen, als auch die nicht enthaltenen Wörter, daher speichern wir nur die enthaltenen.

## Probleme von Bool'scher Suche
- Um zu suchen muss man die korrekte Syntax beherrschen
- Feast or Famine
	- Entweder erhalten wir zu wenige oder viel zu viele Antworten
	- Wird von [[Ranked Retrieval]] behoben
## Links
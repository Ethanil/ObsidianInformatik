---
aliases: 
---
# Segmentation 
Um [[Text]] besser verarbeiten zu können teilen wir diesen in Teile auf. Dies nennt man Segemantation.
## Tokenisation
Eine Art Text zu segmentieren nennt man tokenisation. Bei der Tokenisation wird ein input in eine geordnete Sequenz Tokens geteilt. Normalerweise korrespondiert ein Token dann einem [[Flexion|flexierten]] Wort. Ein System um inputs zu segmentiert nennt man "Tokenizer".
Das Problem ist hierbei, wo wir den Text segmentieren, da die Aufteilung nicht für jeden Text gleich ist.
- whitespace?
	- Führt dazu, dass wir Satzzeichen an unseren Wörtern dranhängen haben
	- können außerdem Teil einer einzigen Zahl sein
- Punkte?
	- passt meistens, allerdings können sie auch z.B. Teil von einer Abkürzung oder Zahlen sein, aber auch Sätze seperieren
- Komma?
	- Können Teil von Zahlen sein, aber auch Sätze seperieren
- Einfaches Anführungszeichen?
	- Kann teil eines Zitats sein, aber auch Teile von Wörtern seperieren
- Bindestrich?
	- verbinden meistens Wörter, aber kann auch Teil von einer Zahlenreichweite sein
- Doppelpunkt
	- Teilt meistens Sätze auf, aber kann auch vielleicht wie bspw. bei einer Zeitangabe Teil eines ganzen Tokens sein
## Links
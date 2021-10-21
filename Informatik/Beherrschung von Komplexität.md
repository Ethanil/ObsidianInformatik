# Beherrschung von Komplexität
## Abstraktion
```ad-note
title: Wichtiges und zentrales Konzept der Informatik
Wir verstecken alle unwichtigen Details, um das große, ganze zu sehen
Nur das was uns interessiert!
```
### Abstraktes Schichtenmodell eines Computers
| Prinzip            | Implementierung        |
| ------------------ | ---------------------- |
| Anwendungssoftware | Programme              |
| Betriebssysteme    | Gerätetreiber          |
| Architektur        | Befehle / Register     |
| Mikroarchitektur   | Datenpfade / Steuerung |
| Logik              | Addierer / Speicher    |
| Digitalschaltungen | Und Gatter / Inverter  |
| Analogschaltungen  | Verstärker / Filter    |
| Bauteile           | Transistoren / Dioden  |
| Physik             | Elektronen             |
Wesentliche Eigenschaften des Schichtenmodells
- Untere Schicht erbringt Dienstleistungen für die nächst höhere Schicht
- Obere Schicht nutzt nur die Dienste der **nächst** niederigere Schicht
- Eindeutige Schnittstelle zwischen den Schichten
- Vorteiler einer sauberen Schichtenstruktur
	- Austauschbarkeit einzelner Schicten, ohne benachbarte Schichten oder das gesamte System ändern zu müssen
	- Benutzer braucht nur die von ihm zu bearbeitende Schicht zu kennen
	- Darunterliegende Schicnten bilden fest definierte Funktionalität
	- Für manche Aufgaben ist genauere Kenntnis der unteren Schichten dennoch notwendig
- Nachteil ist ggf. eine geringere Leistungsfähigkeit des Systems
	- Wir gewinnen an Einfachheit
	- Wir verlieren an Leistung
## Disziplin
```ad-note
Wir beschränken uns auf die Ralisierungsmöglichkeiten
```
```ad-example
title: Digitale Entwurfsdisziplin
Arbeite mit diskreten statt mit stetigen Spannungspegeln
Digitalschaltungen sind einfacher zu entwefen als analoge
Folge: Erlaubt den Entwurf komplexerer Schaltungen
Digitale Systeme ersetzen zunehmend analoge:
	Digitalkamera, digitales Fernsehen, moderne Handys, CD, DVD
```
### Digitale Abstraktion
```ad-note
title: Die meisten physikalischen Gräßen haben stetige Werte
Elektrische Spannung
Frequenz einer Schwinnung
Position einer Masse
```
Berücksichtigen unendlich viele Werte der Größe
Digitale Abstraktion: Berücksichtig nur **endlich** viele Werte
## Wesentliche Techniken
```ad-example
title:Steinschlossgewehr
Hierarchie:
Schaft/Schloss/Lauf
-> Das Schloss kann noch in ander Module zerlegt werden
Hahn/Feuerstein/BAtterie/Batteriefeder/Abzug
Modularität:
Die einzelnen Teile haben diskrete Funktionen:
Durch den Abzug können wir den Schuss "aktivieren"
Regularität:
Wenn wir einen kürzeren Lauf haben wollen, können wir diesen ersetzten ohne die anderen Module zu beinflussen
```
### Hierarchie (Hierarchy)
Hierarchie heißt wir zerlegen das komplexe Modell in Module
### Modularität (Modularity)
Jedes Modul hat eine *unabhängige* Funktion, die durch eine *Schnittstelle* miteinander kommunizieren
### Regularität (Regularity)
Regularität heißt, wir können die einzelnen Module prinzipiell *austauschen*
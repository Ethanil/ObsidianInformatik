## Questmanager
Quests sind immer linear und haben eine bestimmte Anzahl objectives
Quests haben szenen, die additiv geladen werden
Sie werden graceful beendet, entweder wenn sie abgeschlossen werden oder wenn sie abgebrochen werden
Objektives sind complete wenn eine message gefired wird
- Wenn es noch objetives gibt wird ein ObObjectiveComplete invoked, wo niemand subscribed hat
## QuestData
- unbenutztes Institut (sollte das zur Kategorisierung verwendet werden?)
- Questname
- Questbeschreibung
- Questszene (+interner Szenenname)
- Das Objective Array
- Ein optionaler Hilfedialog (atm nur Textasset, vielleicht auch ein Scriptable objekt um person festzulegen, die anspricht?)
- IsCompleted und unbenutztes repeating
## ObjectiveData
- Name
- Beschreibung
- Enum der bestimmt, ob das Objetive fertig ist
- isCompleted bool
## FirstTimeGameStarter
Liest tutorial bool und startet entweder das Tutorial oder Teleportiert den Spieler in seinen Raum
## Questboard
Hat QuestNotes denen bei BecameVisible unterschiedliche Materialien zugeordnet werden und eventuell ein Partikelsystem (fehler wenn alle quests fertig sind, sollte keins mehr vorgeschlagen werden)
## Quest Note
Interactable und Speicherbar
Hoverable gespeichert
Bei Left down show Quest preview
Gespeichert wird nur, ob es repeatable ist ?
## Quest Log
leer?

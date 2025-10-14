Quests sind immer linear und haben eine bestimmte Anzahl objectives
Quests haben szenen, die additiv geladen werden
Sie werden graceful beendet, entweder wenn sie abgeschlossen werden oder wenn sie abgebrochen werden
Objektives sind complete wenn eine message gefired wird
- Wenn es noch objetives gibt wird ein ObObjectiveComplete invoked, wo niemand subscribed hat

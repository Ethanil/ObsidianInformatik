---
aliases: 
---
# Data Manipulation Language 
Mithilfe von Data Manipulation Language(DML) können wir
- Daten eintragen
- Daten ändern
- Daten entfernen
anders als die [[Data Definition Language]], die beschreibt wie die Tabelle aufgebaut ist.
## Einfügen neuer Tupel
```sql
insert into ProfessorIn values (2126, 'Russel', 'C4', 232)
insert into ProfessorIn(PersNr, Name, Rang) values(2126, 'Russel', 'C4');
```
## Löschen von Tupeln
Löschen aller Tupel:
```sql
delete from StudentIn;
```
Löschen von bestimmten Tupeln
```sql
delete from StudentIn
where Semester >13;
```
## Ändern von Tupeln
```sql
update StudentIn set Semester = Semester + 1;
update StudentIn set Semester = Semester +1
where MatrNr = 12345;
```

## Links
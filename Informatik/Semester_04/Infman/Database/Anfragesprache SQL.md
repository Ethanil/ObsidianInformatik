---
aliases:
  - SQL
---
# Anfragesprache SQL 
Structured English Query Language(SQL) ist eine deklarative(was nicht wie) Anfragesprache für [[Relationales Datenmodell|relationale Datenbanksysteme]] die Multimengen(ggf mit Duplikaten) zurückgibt, die sich in die Bereiche
- [[Data Query Language]]
- [[Data Definition Language]]
- [[Data Manipulation Language]]
- [[Data Control Language]]
einteilt.
## Sichten
Eine Sicht ist eine Tabelle die aus Teilen anderer Tabellen zusammengesetzt ist und keinen eigenen Speicher hat und idR read-only sind!
Sichtdefinition und Anfrage auf Sicht
```sql
create view StudProf (Sname, Semester, Titel, Pname) as
select s.Name, s.Semester, v.Titel, p.Name
from StudentIn s, hören h, ProfessorIn p, Vorlesung v
where s.MatrNr = h.MatrNr and
      h.VorlNr = v.VorlNr and
      v.PersNr = p.PersNr;

select * from StudProf where Titel = 'Der Wiener Kreis';
```
## Links
---
aliases: 
---
# Data Query Language 

## Einfache Anfragen
Eine einfache SQL Abfrage besteht aus 3 Teilen: 
```SQL
select Attribut1, Attribut2 
from Tabelle 
where Prädikat;
```
 ### Duplikate
 Duplikate können mit dem keyword `distinct` nach dem `select` eliminiert werden.
 ### Umbenennung
 Durch das Angeben eines weiteren Worts nach dem Attribut/Relation kann dieses umbenannt werden
 ```SQL
 select t.Attribut1 as A1, t.Attribut2 A2
 from Tabelle t
 where Prädikat;
 ```
 ### Sortierung
 Die Rückgabetabellen können sortiert werden:
 ```SQL
 select Attribut1, Attribut2
 from Tabelle
 where Prädikat
 order by Attribut1 asc/desc;
 ```

 ## Joins und Mengenoperationen
 ### Kartesisches Produkt
 Wenn wir mehrere Tabellen angeben wird von diesen das [[kartesisches Produkt]] gebildet
 ```SQL
 select Tabelle1.Attribut1, Tabelle2.Attribut2
 from Tabelle1, Tabelle2
 where Prädikat;
 ```
 ### Joins
 #### cross join
 [[kartesisches Produkt]] genau wie oben nur andere syntax
 #### join oder inner join
 Um 2 Tabellen über ein spezifisches Attribut zu verbinden
 Alle Studierenden, die in eine Vorlesung gehen:
 ```SQL
 select s.Name, v.Titel from StudentIn s
 join hören h on s.MatrNr = h.MatrNr
 join Vorlesung v on h.VorlNr = v.VorlNr;
 ```
Kann auch über das Kartesische Produkt modeliert werden:
```SQL
 select s.Name, v.Titel 
 from StudentIn s, hören h,  Vorlesung v
 where s.MatrNr = h.MatrNr and h.VorlNr = v.VorlNr;
```
 #### outer join
 Um alle Spalten einer Tabelle zu behalten, auch wenn sie nicht mit dem Attribut der anderen matchen verwendet man einen outerjoin
 Alle Studierenden, auch ohne Vorlesung:
```SQL
select s.Name, v.Titel from StudentIn s
left outer join hören h on s.MatrNr = h.MatrNr
left outer join Vorlesung v on h.VorlNr = v.VorlNr;
```
### Mengenoperationen
#### union (all)
[[Vereinigung]] ohne(mit) Duplikaten:
Gebe alle Namen aller AssistentInnen und ProfessorInnen ohne Duplikate aus
```SQL
select Name
from AssistentIn
union
select Name
from ProfessorIn;
```
#### intersect (all)
[[Schnittmenge]] ohne(mit) Duplikate:
Gebe die Namen aller AssistentInnen aus, die einen gemeinsamen Namen mit mindestens einer ProfessorIn hat mit Duplikaten aus:
```SQL
select Name
from AssistentIn
intersect all
select Name
from ProfessorIn;
```
#### minus/except (all)
[[Mengendifferenz]] ohne(mit) Duplikaten:
Gebe die NAmen aller AssistentenInnen aus, die keinen gemeinsamen Namen mit einer ProfessorIn haben ohne Duplikate:
```SQL
select Name
from AssistentIn
minus
select Name
from ProfessorIn;
```
## Aggregation und Gruppierung
Mithilfe von Aggregation fasst man große Ergebnismengen zusammen. Man verwendet dabei Aggregationsfunktionen:
- `sum`
- `avg`
- `max`
- `min`
- `count(distinct)`
Man kann optional noch Zeilen im Ergebnis nach der angegebenen Spalte gruppieren (mittels `group by`)
Summe der SWS aller ProfersorInnen (Name und PersNr):
```SQL
select sum(sws), name, PersNr
from ProfessorIn, Vorlesung
where gelesenVon = PersNr
group by Name, PersNr;
```
### Filter
Mithilfe von having kann man die Gruppierung filtern
Summe der SWS für alle C4-ProfessorInnen mit einem Durchschnitt von mehr als 3 SWS
```SQL
select sum(sws), Name, PersNr
from ProfessorIn, Vorlesung
where gelesen = PersNr and Rang = 'C4'
group by Name, PersNr
having avg(sws) > 3;
```
## Links
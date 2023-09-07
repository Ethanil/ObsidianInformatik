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
### Between and in
```sql
select *
from StudentIn
where Semester between 1 and 4;

selct *
from StudentIn
where Semester in (1,2,3,4);
```
### Like (Pattern Matching in Strings)
Mithilfe von `like` können wir mit Strings pattern matchen, dabei haben wir die wildcards `_`(genau 1 beliebiges Zeichen) und `%`(0 bis unendlich beliebige Zeichen)
Studierende deren Namen mit M anfängt:
```sql
select *
from StudentIn
where name like 'M%';
```

### case .. when ...
Prüfung mit einer textuellen Bewertung
```sql
select MatrNr, (case when Note < 1.5 then 'sehr gut'
			   when Note < 2.5 then 'gut'
			   when Note < 3.5 then 'befriedigend'
			   when Note <= 4.0 then 'ausreichend'
			   else 'nicht bestanden' end)
from prüfen;
```
### limit
Beste 5 Prüfungsergebnise
```sql
select *
from prüfen
order by Note 
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
## Unteranfragen
Unteranfragen sind an allen Stellen möglich:
- Select-Klausel
- From-Klausel
- Where-Klausel
- Group-by-Klausel
- Having-Klausel
ProfessorInnen und deren Lehrbelastung
```sql
select PersNr, (select sum(v.SWS) 
				from Vorlesung v
				where v.gelesen = p.PersNr)
from ProfessorIn p;
```
Studierende mit mehr als zwei Vorlesungen
```sql
select stud.MatrNr, stud.Name, stud.VorlAnzahl
from (select s.MatrNr, s.Name, sum(*) as VorlAnzahl
	 from StudentIn s, hören h
	 where s.MatrNr = h.MatrNr
	 group by s.MatrNr, s.Name) stud
where stud.VorlAnzahl > 2;
```
Welche Prüfungen sind besser als durchschnittlich verlaufen
```sql
select *
from prüfen
where Note < (select avg(Note) from prüfen);
```
```ad-caution
title:Achtung
Hier muss die Unteranfrage einen skalaren Wert zum Vergleichen liefern
```
### Where Operatoren
Bisher bekannte Operatoren können nur auf skalare Werte angewand werden. Damit man in der Where-Klausel auch mit ganzen Tabellen vergleichen kann benötigt man weitere
- `exists T`: ergibt True, wenn `T` nicht leer ist
- `s IN T`: ergibt True wenn `s` in `T` vorkommt
- `s > ALL T`: ergibt True wenn `s` größer als jeder Wert in `T` ist
- `s > ANY T`: ergibt True, wenn `s` größer als mindestens ein Wert in `T` ist
## Relationale Division durch count-Aggregation
[[Relationale Abfragesprachen#$ div $ Relationale Division|Relationale Division]] kann einfach durch eine count-Aggregation ausgedrückt werden
```sql
select h.MatrNr, count(*)
from hören h, Vorlesung v
where v.VorlNr = h.VorlNr and v.sws = 4
group by h.MatrNr
having count(*) = 
(select count(*) from Vorlesung where sws = 4);
```
## Null-Werte
Ein Null Wert ist ein Unbekannter bzw kein Wert. Durch Null-Einträge können sehr überraschende Anfrageergebnisse zustandekommen
```ad-caution
title:Achtung!
Durch manche Anfrageauswertungen können auch null-Werte entstehen!
```
### Null in arithmetischen Ausdrücken
Sobald ein Operand Null ist, ist das Ergebnis auch immer Null
### Null in Filter Prädikaten (where/having)
SQL hat eine [[dreiwertige Logik]]. Vergleichsoperationen liefern unkown wenn mindestens eines der Argumente null ist.
### Null in Aggregation
| Funktion    | Verhalten                 |
| ----------- | ------------------------- |
| count       | Null wird nicht migezählt |
| sum         | Null wird ignoriert       |
| avg         | sum/count                 |
| min und max | Null wird ignoriert                          |
Ausnahme: (sum, avg, min, max): Wenn null der ***einzige*** Wert in der Gruppe ist, dann ist das Ergebnis null.
## Links
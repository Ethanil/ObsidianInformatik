---
aliases: 
---
# Anfragesprache SQL 
Structured English Query Language(SQL) ist eine deklarative(was nicht wie) Anfragesprache für [[Relationales Datenmodell|relationale Datenbanksysteme]] die Multimengen(ggf mit Duplikaten) zurückgibt, die sich in die Bereiche
- Data Query Language
- Data Definition Language
- Data Manipulation Language
- Data Control Language
einteilt.
## Einfache Anfragen
Eine einfache SQL Abfrage besteht aus 3 Teilen: 
```SQL
select Attribut1, Attribut2 
from Tabelle 
where Prädikat
```
 ### Duplikate
 Duplikate können mit dem keyword `distinct` nach dem `select` eliminiert werden.
 ### Umbenennung
 Durch das Angeben eines weiteren Worts nach dem Attribut/Relation kann dieses umbenannt werden
 ```SQL
 select t.Attribut1 as A1, t.Attribut2 A2
 from Tabelle t
 where Prädikat
 ```
 ### Sortierung
 Die Rückgabetabellen können sortiert werden:
 ```SQL
 select Attribut1, Attribut2
 from Tabelle
 where Prädikat
 order by Attribut1 asc/desc
 ```
 ## Joins und Mengenoperationen
 ### Kartesisches Produkt
 Wenn wir mehrere Tabellen angeben wird von diesen das [[kartesisches Produkt]] gebildet
 ```SQL
 select Tabelle1.Attribut1, Tabelle2.Attribut2
 from Tabelle1, Tabelle2
 where Prädikat
 ```
 
## Links
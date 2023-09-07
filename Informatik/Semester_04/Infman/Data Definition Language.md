---
aliases: 
---
# Data Definition Language 
Data Definition Language (DDL) Befehle dienen dazu, Tabellen
- anzulegen
- zu ändern
- zu entfernen
aber nicht neue [[Daten]] hinzuzufügen, dafür dient [[Data Manipulation Language]]
## Anlegen einer Tabelle
Um eine Tabelle anzulegen verwenden wir `create table`
```SQL
create table (if not exists) ProferssorIn
(PersNr integer,
 Name   varchar(30),
 Rang   character(2)
);
```
### Datentypen
- smallint, int, ..., float, double,...
- numeric(p,s) oder decimal(p,s)
- character(n), char(n)
- character varying(n), varchar(n)
- date
- blob [sehr große binäre daten]
- clob [sehr große Strings]

Eine Tabelle direkt mit Primärschlüssel anlegen:
```SQL
create table ProfessorIn 
(PersNr integer primary key,
 Name   varchar(30),
 Rang   char(2)
);
```
bzw
```SQL
create table ProfessorIn 
(PersNr integer,
 Name   varchar(30),
 Rang   char(2),
 primary key(PersNr)
);
```
## Links
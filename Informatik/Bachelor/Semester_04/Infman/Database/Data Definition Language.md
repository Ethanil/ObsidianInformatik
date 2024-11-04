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
bei einem zusammengesetztem PK kann nur die 2. Variante verwendet werden
## Automatisch inkrementierende PKs
mithilfe von `create sequence` können wir automatisch inkrementierende Primärschlüssel modellieren
```sql
create sequence PersNrSeq;
create sequence PersNrSeq start with 1 increment by 1;
```
alternativ direkt bei Erstellung
```sql
create table ProfessorIn(
PersNr serial primary key,
Name varchar(30),
Rang char(2)
);
```
## Entfernen einer Tabelle
Um eine Tabelle zu entfernen, verwenden wir `drop table`
```SQL
drop table (if exists) ProfessorIn (cascade)
```
`cascade` entfernt auch alle abhängigen Objekte dieser Tabelle.
## Ändern einer Tabelle
Mithilfe von `alter table` können wir eine existierende Tabelle bearbeiten
Attribut hinzufügen:
```SQL
alter table ProfessorIn add column Raum integer
```
PK hinzufügen:
```SQL
alter table ProfessorIn add constraint primary key(PersNr)
```
## Datenintegrität
Beim hinzufügen von Spalten kann man diese mit Integritätsbedingungen belegen
### not null
Erzwingt, dass beim Einfügen von Tupeln der Attributwert angegeben werden muss
```SQL
create table ProfessorIn(
PersNr integer primary key,
Name varchar(30) not null,
Rang char(2)
);
```
PK's sind impliziert immer not null
### default
Ändert den default-Wert beim einfügen von `null` zum angegebenen Wert
```sql
create table AssistentIn(
PersNr integer primary key,
Name varchar(30) not null,
Fachgebiet varchar(200) default 'Informatik'
);
```
### check
Durch eine check-Bedingung kann der Datenbereich eingegrenzt werden
```sql
create table Polygon(
corner integer primary key,
sides integer not null,
name varchar(200)
check (corner >= 4 and sides >= 4)
);
```
In einer check-Bedingung können vollständige SQL-Anfragen angegeben werden.
### unique
Die Unique-Bedingung erzwingt Eindeutigkeit für alle Werte eines Attributs
```sql
create table ProfessorIn(
PersNr integer primary key,
Name varchar(30) not null,
TelefonNr integer unique
);
```
Es kann mehrere unique Spalten geben.
```ad-caution
title:Vorsicht
Unique erlaubt einen einzigen null wert, anders als PK
```
## [[Relationales Datenmodell#Referenzielle Integrität|Referenzielle Integrität]]
In SQL kann referentielle Integrität mittels `foreign key` modeliert werden
```sql
create table ProfersorIn(
PersNr integer primary key,
...
);
create table Vorlesung(
VorlNr integer priamry key,
PersNr integer not null,
foreign key(PersNr) references ProfessorIn(PersNr)
);
```
### automatisches weiterleiten von Änderungen
mittels `on delete` bzw `on update` können Änderungen beim FK verarbeitet werden
```sql
create table Vorlesung(
VorlNr integer priamry key,
PersNr integer not null,
foreign key(PersNr) references ProfessorIn(PersNr)
[on delete {set null | cascade | restrict}]
[on update {set null | cascade | restrict}]
);
```

## Links
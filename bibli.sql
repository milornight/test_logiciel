-- sqlite3 bibli.db
-- .read bibli.sql
-- commandes de destruction des tables
DROP TABLE IF EXISTS Utilisateur;


-- commandes de creation des tables
CREATE TABLE Utilisateur (
    username varchar(10) PRIMARY KEY NOT NULL check (len(username)>=3),
    password varchar(20) NOT NULL check (len(password)>= 8, ),
    spublickey char(128) check (len(spublickey)= 128),
    sprivatekey char(128) check (len(sprivatekey)= 128),
    epublickey char(128) check (len(epublickey)= 128),
    eprivatekey char(128) check (len(eprivatekey)= 128),
    CHECK (username NOT LIKE '%[^A-Z0-9_/#-]%' ), --'%[^A-Z0-9#^!@]%'
    CHECK (password LIKE '%[A-Z]%' AND password LIKE '%[a-z]%' AND password LIKE '%[0-9]%'
        AND password LIKE '%[!#$^&-_=.,;:~]%' AND password LIKE '%[@%*()+|"]%')
    );

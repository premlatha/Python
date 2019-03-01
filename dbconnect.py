import sqlite3
conn=sqlite3.connect('trackdb.sqlite')
cur=conn.cursor()

def dropTables():
    cur=conn.cursor()
    drop_Album='Drop table if exists Album'
    drop_Artist='Drop table if exists Artist'
    drop_Genre='Drop table if exists Genre'
    drop_Track='Drop table if exists Track'
    cur.execute(drop_Album)
    cur.execute(drop_Artist)
    cur.execute(drop_Genre)
    cur.execute(drop_Track)

def createTables():
    create_Album='CREATE TABLE Album (    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,  artist_id  INTEGER,  title   TEXT UNIQUE)'
    create_Artist='CREATE TABLE Artist (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name    TEXT UNIQUE)'
    create_Genre='CREATE TABLE Genre (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,  name    TEXT UNIQUE)'
    create_Track='CREATE TABLE Track (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,title TEXT  UNIQUE,    album_id  INTEGER,genre_id  INTEGER,len INTEGER, rating INTEGER, count INTEGER)'
    cur.execute(create_Album)
    cur.execute(create_Artist)
    cur.execute(create_Genre)
    cur.execute(create_Track)

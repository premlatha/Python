import dbconnect
import xml.etree.ElementTree as ET

dbconnect.dropTables()
dbconnect.createTables()

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre=lookup(entry,'Genre')

    if name is None or artist is None or album is None : 
        continue

    print(name, artist, album, count, rating, length,genre)

    dbconnect.cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    dbconnect.cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = dbconnect.cur.fetchone()[0]

    dbconnect.cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    dbconnect.cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = dbconnect.cur.fetchone()[0]

    if genre is not None:
         dbconnect.cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', ( genre, ) )
         dbconnect.cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
         genre_id = dbconnect.cur.fetchone()[0]

    dbconnect.cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id,genre_id, len, rating, count) 
        VALUES ( ?, ?, ?,?, ?, ? )''', 
        ( name, album_id,genre_id, length, rating, count ) )

    dbconnect.conn.commit()

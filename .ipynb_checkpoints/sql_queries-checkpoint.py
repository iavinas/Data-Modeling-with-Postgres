# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songsplay (song_title varchar, artist_name varchar, year int, album_name varchar, single Boolean);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS user
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS song ('song_id' varchar, 'title' varchar, 'artist_id' varchar, 'duration' double)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist ('artist_id' varchar, 'artist_name' varchar, 'artist_location' varchar, 'artist_latitude' double, 'artist_longitude' double)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("INSERT INTO songs ('song_id', 'title', 'artist_id', 'duration') values (%s, %s, %s, %s)")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

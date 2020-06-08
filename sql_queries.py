# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (
songplay_id SERIAL PRIMARY KEY,
start_time TIMESTAMP REFERENCES time(start_time),
user_id VARCHAR(100) REFERENCES users(user_id),
level VARCHAR(100),
song_id VARCHAR(100) REFERENCES songs(song_id),
artist_id VARCHAR(100) REFERENCES artists(artist_id),
session_id BIGINT,
location VARCHAR(500),
user_agent TEXT)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id VARCHAR(100),
firstName VARCHAR(100),
lastName VARCHAR(100),
gender VARCHAR(10))
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id VARCHAR(100) PRIMARY KEY,
title VARCHAR(100),
artist_id VARCHAR(100),
duration DOUBLE)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artist (
artist_id VARCHAR(100) PRIMARY KEY,
artist_name VARCHAR(100),
artist_location VARCHAR(100),
artist_latitude DOUBLE,
artist_longitude DOUBLE)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time TIMESTAMP PRIMARY KEY,
hour INT,
day INT,
week_of_year INT,
month INT,
weekday BOOLEAN)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay
(songplay_id, start_time, user_id, level, song_id, artist_id, session_id,
location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, firstName, lastName, gender) VALUES(%s, %s, %s, %s)
""")

song_table_insert = ("""
INSERT INTO songs ('song_id', 'title', 'artist_id', 'duration') VALUES (%s, %s,
%s, %s)
""")

artist_table_insert = ("""
  INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude,
    artist_location) VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

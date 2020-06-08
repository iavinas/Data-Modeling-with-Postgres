# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplay (
songplay_id SERIAL PRIMARY KEY,
start_time TIMESTAMP NOT NULL,
user_id VARCHAR(100) NOT NULL,
level VARCHAR(100),
song_id VARCHAR(100) NOT NULL,
artist_id VARCHAR(100) NOT NULL,
session_id BIGINT,
location VARCHAR(500),
user_agent TEXT
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id VARCHAR(100),
firstName VARCHAR(100),
lastName VARCHAR(100),
gender VARCHAR(100)
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id VARCHAR(100) PRIMARY KEY,
title VARCHAR(100),
artist_id VARCHAR(100),
duration DOUBLE PRECISION);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id VARCHAR(100) PRIMARY KEY,
artist_name VARCHAR(100),
artist_location VARCHAR(100),
artist_latitude DOUBLE PRECISION,
artist_longitude DOUBLE PRECISION);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time TIMESTAMP PRIMARY KEY,
hour INT,
day INT,
week INT,
month INT,
year INT,
weekday VARCHAR(20));
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay
(start_time, user_id, level, song_id, artist_id, session_id,
location, user_agent) VALUES (to_timestamp(%s), %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, firstName, lastName, gender) VALUES(%s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, duration) VALUES (%s, %s,
%s, %s);
""")

artist_table_insert = ("""
  INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude,
    artist_longitude) VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
  INSERT INTO time (start_time, hour, day, week, month, year, weekday)
  VALUES(to_timestamp(%s), %s, %s, %s, %s, %s, %s)
  ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
  SELECT songs.song_id, artists.artist_id FROM
  (songs JOIN artists ON songs.artist_id=artists.artist_id)
  WHERE songs.title=%s AND artists.artist_name=%s and songs.duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

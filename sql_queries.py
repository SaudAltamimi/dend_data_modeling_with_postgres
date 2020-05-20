# DROP TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

#Fact Table
#songplays - records in log data associated with song plays i.e. records with page NextSong

#songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


# CREATE TABLES
songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
(
    songplay_id SERIAL,
    start_time TIMESTAMP REFERENCES time(start_time),
    user_id VARCHAR REFERENCES users(user_id),
    level VARCHAR,
    song_id VARCHAR REFERENCES songs(song_id),
    artist_id VARCHAR REFERENCES artists(artist_id),
    session_id BIGINT,
    location VARCHAR,
    user_agent TEXT,
    PRIMARY KEY (songplay_id)
)
""")

#Dimension Table
#users - users in the app
#user_id, first_name, last_name, gender, level

user_table_create = ("""
CREATE TABLE users
(
    user_id VARCHAR,
    firstName VARCHAR,
    lastName VARCHAR,
    gender VARCHAR,
    level VARCHAR,
    PRIMARY KEY (user_id)
)
""")

#Dimension Table
#songs - songs in music database
#song_id, title, artist_id, year, duration

song_table_create = ("""
CREATE TABLE songs
(
    song_id VARCHAR,
    title VARCHAR,
    artist_id VARCHAR,
    year INTEGER,
    duration DOUBLE PRECISION,
    PRIMARY KEY (song_id)
)
""")

#Dimension Table
#artists - artists in music database
#artist_id, name, location, latitude, longitude

artist_table_create = ("""
CREATE TABLE artists
(
    artist_id VARCHAR,
    name VARCHAR,
    location VARCHAR,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    PRIMARY KEY (artist_id)
)
""")
#Dimension Table
# time - timestamps of records in songplays broken down into specific units
# start_time, hour, day, week, month, year, weekday
# The values in this table are autogenerated so we do not need no constraint
time_table_create = ("""
CREATE TABLE time(
    start_time TIMESTAMP,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER,
    PRIMARY KEY (start_time)
)
""")

# INSERT RECORDS
songplay_table_insert = (
    """
    INSERT INTO songplays
    (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
 """)

user_table_insert = (
    """INSERT INTO users 
    (user_id, firstName, lastName, gender, level) 
    VALUES (%s, %s, %s, %s, %s) 
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level 
""")

song_table_insert = (
    """INSERT INTO songs 
    (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
    """)

artist_table_insert = ("""
        INSERT INTO artists 
        (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (artist_id) 
        DO UPDATE SET 
        location=EXCLUDED.location, latitude=EXCLUDED.latitude, 
        longitude=EXCLUDED.longitude 
""")

time_table_insert = ("""
        INSERT INTO time 
        (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS BY SONG_ID AND ARTIST_ID
song_select = ("""SELECT songs.song_id, artists.artist_id 
                  FROM songs 
                  JOIN artists ON  songs.artist_id=artists.artist_id
                  WHERE songs.title=%s AND artists.name=%s AND songs.duration=%s;
                  """)



# QUERY LISTS
create_table_queries = [song_table_create, 
                         user_table_create,
                        artist_table_create,
                       time_table_create,
                       songplay_table_create]

drop_table_queries = [user_table_drop,
                      song_table_drop, 
                      artist_table_drop, 
                      time_table_drop, 
                      songplay_table_drop]
# Project: Data Modeling with Postgres
One of the udacity data engineering nano-degree projects, where we need to implement a simple ETL (OLAP data modeling) to simplify analysing the required data for the business.

---
## Raw data
### Song Dataset
The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID.


### Log Dataset
The second dataset consists of log files in JSON format generated by this event simulator (https://github.com/Interana/eventsim) based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset we will be working with are partitioned by year and month.


---
## New Schema
Using the song and log datasets, we need to create a `star schema` optimized for queries on song play analysis. This includes the following tables.

### Fact Table
1. **songplays** - records in log data associated with song plays i.e. records with page NextSong
> songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

### Dimension Tables
1. **users** - users in the app
> user_id, first_name, last_name, gender, level

2. **songs** - songs in music database
> song_id, title, artist_id, year, duration

3. **artists** - artists in music database
> artist_id, name, location, latitude, longitude

4. **time** - timestamps of records in songplays broken down into specific units
> start_time, hour, day, week, month, year, weekday

---
### To create the same environment (PostgreSQL relational database):
`Using Docker`
> Pull Postgres official image: `docker pull postgres` 

> run `docker run -d -e POSTGRES_PASSWORD=student -e POSTGRES_DB=studentdb -e POSTGRES_USER=student -p 5432:5432 -t postgres`

---
## How to create the database and populate data?

### Create Tables
1. Write `CREATE` statements in `sql_queries.py` to create each table.
2. Write `DROP` statements in `sql_queries.py` to drop each table if it exists.
3. Run `create_tables.py` to create your database and tables.
4. Run `test.ipynb` to confirm the creation of your tables with the correct columns. 

## Build ETL Processes
The `etl.ipynb` notebook was used to develop and document ETL processes for each table. Run `test.ipynb` to confirm that records were successfully inserted into each table. Remember to rerun `create_tables.py` to reset your tables before each time you run this notebook.

## Build ETL Pipeline
The complete pipeline are in etl.py, it will process the entire datasets. Remember to run `create_tables.py` before running `etl.py` to reset your the tables. Run `test.ipynb` to confirm your records are successfully inserted into each table.

import psycopg2



# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from "Artist" table
# cursor.execute('SELECT * FROM "Artist"') # psql = SELECT * FROM "Artist";

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"') # psql = SELECT "Name" FROM "Artist";

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"]) # psql = SELECT * FROM "Artist" WHERE "Name" = 'Queen';

# Query 4 - select only "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51]) # psql = SELECT * FROM "Artist" WHERE "ArtistId" = 51;

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51]) # psql = SELECT * FROM "Album" WHERE "ArtistId" = 51;

# Query 6 - select all tracks where the composer is "Queen" from "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"]) # psql = SELECT * FROM "Track" WHERE "Composer" = 'Queen';

# Query 7 (challenge)
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"]) # psql = SELECT * FROM "Track" WHERE "Composer" = 'AC/DC';

# Query 8 (challenge)
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"]) # psql = SELECT * FROM "Track" WHERE "Composer" = 'test';

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
#Temp Config
your_rapidapi_key = "f1b94bda20mshfc448b87ed832f1p1a9785jsn76236c066d8d"
DBusername = 'plexuser'
DBpassword = 'plexpass'
moviespath = 'C:/Users/frank/Documents/GoogleDrive/Dev/Plexensus/SampleMovies'

import mysql.connector

def headerrequest() -> dict:
    headers = {
        'x-rapidapi-key': your_rapidapi_key,
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }
    return headers

dbconfig = { 'host': '127.0.0.1',
             'user': DBusername,
             'password': DBpassword,
             'database': 'localmoviesdb', }

#Default pass was reset to the old one
class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    
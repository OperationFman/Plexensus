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
    

def fresh_data() -> dict:
    """grabs a new movie with its name, year and poster from the DB"""
    print('Hello World')

#Working on this last, trying to get match to set to 1 or 0 
def update_database_match(moviename: str, moviematch: int) -> None:
    with UseDatabase(dbconfig) as cursor:
        _SQL = """update moviedata 
                set moviematch = %s where name = %s
                values
                (%s, %s)"""
        cursor.execute(_SQL, (moviematch, moviename))
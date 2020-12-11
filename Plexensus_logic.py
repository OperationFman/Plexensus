import mysql.connector
import random
from Plexensus_config import *

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
    
def total_db_records() -> int:
    """Queries the db and gets the total number of records (rows)"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select count(*) from moviedata"""
        cursor.execute(_SQL)
        contents = cursor.fetchone()
        return contents[0]

def fresh_data() -> dict:
    """Grabs a new movie with its name, year and poster from the DB"""
    totalmovies = total_db_records()
    random_movie = random.randint(1, totalmovies)
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select nomatch, disliked from moviedata where id=%s"""
        cursor.execute(_SQL, (random_movie,))
        contents = cursor.fetchone()
        nomatch = contents[0]
        disliked = contents[1]
        if nomatch == 1:
            return fresh_data()
        elif disliked == 1:
            return fresh_data()
        else:
            with UseDatabase(dbconfig) as cursor:
                _SQL = """select name, year, poster from moviedata where id=%s"""
                cursor.execute(_SQL, (random_movie,))
                confirmed_contents = cursor.fetchall()
                return confirmed_contents


def update_database_match(moviename: str, moviematch: int) -> None:
    """Allows the match to change from true/false (1/0) via the movie name"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """update moviedata set moviematch =%s where name =%s"""
        cursor.execute(_SQL, (moviematch, moviename))

def update_database_dislike(moviename: str, disliked: int) -> None:
    """Allows the dislike to change from true/false (1/0) via the movie name"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """update moviedata set disliked =%s where name =%s"""
        cursor.execute(_SQL, (disliked, moviename))

def reset_matches() -> None:
    """Resets all matches in the DB to 0 (False)"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """update moviedata set moviematch =0"""
        cursor.execute(_SQL)

def reset_dislikes() -> None:
    """Resets all dislikes in the DB to 0 (False)"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """update moviedata set disliked =0"""
        cursor.execute(_SQL)

def match_check(moviename) -> None:
    """Returns True if the last movie was already setup to match with, False if not"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select moviematch from moviedata where name =%s"""
        cursor.execute(_SQL, (moviename, ))
        result = cursor.fetchall()
        if result[0][0] == 1:
            return True
        else:
            return False
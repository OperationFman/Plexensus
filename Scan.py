import requests
from Plexensus_logic import *
import os
import numpy as np
import ast

def api_request(movie: str) -> dict:
    """Using RapidAPI sends a query string and returns the movies dict with relevant info"""
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":movie,"page":"1","r":"json"}
    headers = headerrequest()
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

def insert_movie(addname: str, addyear: int, addposter: str, nomatchresult: int) -> None:
    """SQL inserts the movie into the DB"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into moviedata
                (name, year, poster, moviematch, nomatch)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (addname, addyear, addposter, 0, nomatchresult))
#insert_movie('Ready Player One', 2018, 'https://m.media-amazon.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_UX182_CR0,0,182,268_AL_.jpg', 0)

def local_scan() -> dict:
    """Scans local movie files and removes junk. Returns the result from imdb"""
    moviefile = os.listdir(moviespath)
    onboarding_movies = set()
    for moviename in moviefile:
        #Trim 1080p/720p
        if moviename.find('1080p'):
            moviename = moviename.replace('1080p', '')
        elif moviename.find('720p'):
            moviename = moviename.replace('720p', '')
        #Remove the year from the end
        if '(' and ')' in moviename:
            moviename = moviename.strip()
            moviename = moviename[:-6]
        moviename = moviename.strip()
        onboarding_movies.add(moviename)
    return onboarding_movies


def load_database() -> list:
    """Returns a list of every movie name in the database"""
    with UseDatabase(dbconfig) as cursor:
        _SQL = """select name from moviedata"""
        cursor.execute(_SQL)
        contents = [item[0] for item in cursor.fetchall()]
        return contents

def perform_scan() -> None:
    """When activated will scan local movies, check the db for any missing. If missing, the api fills the db"""
    local_movies = list(local_scan())
    database_movies = load_database()
    new_movies = np.setdiff1d(local_movies,database_movies) #Find local movies not appearing in the DB
    for i in new_movies:
        api_result = api_request(i)
        converted_literal = ast.literal_eval(api_result)
        state = converted_literal['Response']
        insert_movie(i, 1999, "None", 1)
        if state == 'True':
            searched_movie = converted_literal['Search']
            selected_movie = searched_movie[0]
            get_title = selected_movie['Title']
            get_year = selected_movie['Year']
            get_poster = selected_movie['Poster']
            insert_movie(get_title, get_year, get_poster, 0)
    print('****Database Scan Complete!****')
    
perform_scan()
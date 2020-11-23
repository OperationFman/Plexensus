import requests
from Plexensus_logic import *

def api_request(movie: str) -> dict:
    """Using RapidAPI sends a query string and returns the movies dict with relevant info"""
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":movie,"page":"1","r":"json"}
    headers = headerrequest()
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
#print(api_request("Avengers: Endgame"))



def insert_movie(addname: str, addyear: int, addposter: str, nomatchresult: int) -> None:
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into moviedata
                (name, year, poster, moviematch, nomatch)
                values
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (addname, addyear, addposter, 0, nomatchresult))
#insert_movie('Ready Player One', 2018, 'https://m.media-amazon.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_UX182_CR0,0,182,268_AL_.jpg', 0)

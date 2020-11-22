import requests
from Plexensus_config import *

def apirequest(movie: str) -> dict:
    """Using RapidAPI sends a query string and returns the movies dict with relevant info"""
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":movie,"page":"1","r":"json"}
    headers = headerrequest()
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

print(apirequest("Avengers: Endgame"))
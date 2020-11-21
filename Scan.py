import requests

def apirequest(movie: str) -> dict:
    """Using RapidAPI sends a query string and returns the movies dict with relevant info"""
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":movie,"page":"1","r":"json"}
    headers = {
        'x-rapidapi-key': "f1b94bda20mshfc448b87ed832f1p1a9785jsn76236c066d8d",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text

print(apirequest("Avengers: Endgame"))
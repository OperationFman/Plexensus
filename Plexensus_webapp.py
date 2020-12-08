from flask import Flask, render_template, url_for, jsonify, json, request, make_response
from Scan import perform_scan
from Plexensus_logic import *

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    starter_movie = 'Shrek 2'
    starter_year = '2004'
    starter_poster = 'https://m.media-amazon.com/images/M/MV5BMDJhMGRjN2QtNDUxYy00NGM3LThjNGQtMmZiZTRhNjM4YzUxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'
    return render_template('index.html', 
                            the_moviename=starter_movie,
                            the_movieyear=starter_year,
                            the_poster='<img id="movieposter" src=' + starter_poster + ' alt="name">',
                            the_moviename_form = '<input type="hidden" id="hiddenmoviename" value="' + starter_movie + '">',
                            the_movieyear_form = '<input type="hidden" id="hiddenmovieyear" value="' + starter_year + '">',
                            the_movieposter_form = '<input type="hidden" id="hiddenmovieposter" value="' + starter_poster + '">')

@app.route('/_swipe_no', methods=['POST'])
def swipe_no():
    req = request.get_json()
    update_database_match(req['name'], 0)
    #here

    #PLACEHOLDER Send new stuff to front end
    res = make_response(jsonify({
        "newMovieName": "Narnia",
        "newMovieYear": "2010",
        "newMoviePoster": "https://m.media-amazon.com/images/M/MV5BMTc0NTUwMTU5OV5BMl5BanBnXkFtZTcwNjAwNzQzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg"
    }), 200)
    return res

if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.214")
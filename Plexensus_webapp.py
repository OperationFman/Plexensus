from flask import Flask, render_template, url_for, jsonify, json, request, make_response
from Scan import perform_scan
from Plexensus_logic import *

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    starter_movie = 'Tap the Tick or Cross'
    starter_year = 'To Get Started'
    starter_poster = 'static/images/welcomeposter.png'
    return render_template('index.html', 
                            the_moviename=starter_movie,
                            the_movieyear=starter_year,
                            the_poster='<img id="movieposter" src=' + starter_poster + ' alt="name">',
                            the_moviename_form = '<input type="hidden" id="hiddenmoviename" value="Shrek 2">',
                            the_movieyear_form = '<input type="hidden" id="hiddenmovieyear" value="2004">',
                            the_movieposter_form = '<input type="hidden" id="hiddenmovieposter" value="https://m.media-amazon.com/images/M/MV5BMDJhMGRjN2QtNDUxYy00NGM3LThjNGQtMmZiZTRhNjM4YzUxL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg">')

@app.route('/_swipe_no', methods=['POST'])
def swipe_no():
    req = request.get_json()
    update_database_dislike(req['name'], 1)
    new_data = fresh_data()
    res = make_response(jsonify({
        "newMovieName": new_data[0][0],
        "newMovieYear": new_data[0][1],
        "newMoviePoster": new_data[0][2],
        "matchStatus": "false"
    }), 200)
    return res

@app.route('/_swipe_yes', methods=['POST'])
def swipe_yes():
    req = request.get_json()
    check_match = match_check(req['name'])
    update_database_match(req['name'], 1)
    new_data = fresh_data()
    if check_match == True:
        res = make_response(jsonify({
            "newMovieName": req['name'],
            "newMovieYear": req['year'],
            "newMoviePoster": req['poster'],
            "matchStatus": "true"
        }), 200)
        return res 
    else:
        res = make_response(jsonify({
            "newMovieName": new_data[0][0],
            "newMovieYear": new_data[0][1],
            "newMoviePoster": new_data[0][2],
            "matchStatus": "false"
        }), 200)
        return res


@app.route('/_refresh', methods=['POST'])
def swipe_refresh():
    reset_matches()
    reset_dislikes()
    return 'nada'


if __name__ == '__main__':
    app.run(debug=True, host="192.168.0.214")
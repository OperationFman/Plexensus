var view = {
    changePoster: function(poster_url) {
        return document.getElementById("movieposter").src = poster_url;
    },
    changeHiddenPoster: function(poster_url) {
        return document.getElementById("hiddenmovieposter").value = poster_url;
    },
    changeYear: function(year) {
        return document.getElementById("movieyear").innerHTML = year;
    },
    changeHiddenYear: function(year) {
        return document.getElementById("hiddenmovieyear").value = year;
    },
    changeName: function(name) {
        return document.getElementById("moviename").innerHTML = name;
    },
    changeHiddenName: function(name) {
        return document.getElementById("hiddenmoviename").value = name;
    }
};

function loadMovieData(dataparam) {
    newMovieName = dataparam['newMovieName'];
    newMovieYear = dataparam['newMovieYear'];
    newMoviePoster = dataparam['newMoviePoster'];
    view.changeName(newMovieName);
    view.changeHiddenName(newMovieName);
    view.changeYear(newMovieYear);
    view.changeHiddenYear(newMovieYear);
    view.changePoster(newMoviePoster);
    view.changeHiddenPoster(newMoviePoster);
};

$(function(){
	$("button[name='like-button']").click(function(){
        console.log('You Liked');
    });
});

$(function(){
	$("button[name='dislike-button']").click(function(){
        var currentMovie = document.getElementById("hiddenmoviename").value;
        var currentYear = document.getElementById("hiddenmovieyear").value;
        var currentPoster = document.getElementById("hiddenmovieposter").value;
        currentMovieObject = {
            name: currentMovie,
            year: currentYear,
            poster: currentPoster
        };

        fetch(`${window.origin}/_swipe_no`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(currentMovieObject),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        .then(function(response) {
            response.json().then(function (data) {
                loadMovieData(data);
            })
        })
    });
});

$(function(){
	$("button[name='refresh-button']").click(function(){
        console.log('You Refreshed');
    });
});

function init() {};
window.onload = init;
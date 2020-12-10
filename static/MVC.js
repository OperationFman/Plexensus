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
    },
    matchedMovie: function() {
        document.querySelector(".alert h1").innerHTML = 'Match!';
        document.querySelector(".alertmsg p").innerHTML = "Go again?";
        document.getElementsByClassName('ModalOverlay')[0].style.visibility = 'visible'
        document.getElementsByClassName('alert')[0].style.visibility = 'visible'
        document.getElementsByName('no-refresh')[0].style.visibility = 'hidden';
        document.getElementsByName('yes-refresh')[0].style.visibility = 'hidden';
        document.getElementsByName('modal-refresh')[0].style.visibility = 'visible';
        document.querySelector(".alert").style.height = '40%';
        document.getElementById('modal-buttons').style.visibility = 'hidden';
    }
};

var controller = {
    loadMovieData: function(dataparam) {
        newMovieName = dataparam['newMovieName'];
        newMovieYear = dataparam['newMovieYear'];
        newMoviePoster = dataparam['newMoviePoster'];
        view.changeName(newMovieName);
        view.changeHiddenName(newMovieName);
        view.changeYear(newMovieYear);
        view.changeHiddenYear(newMovieYear);
        view.changeHiddenPoster(newMoviePoster);
        if (newMoviePoster == 'N/A') {
            newMoviePoster = 'static/images/errorposter.png'
            view.changePoster(newMoviePoster);
        }
        else {
            view.changePoster(newMoviePoster);
        }
    },
    resetAll: function() {
        junkObject = {
            "junk": "junk",
            "junk": "junk"
        };
        fetch(`${window.origin}/_refresh`, {
            method: "POST",
            credentials: "include",
            body: JSON.stringify(junkObject),
            cache: "no-cache",
            headers: new Headers({
                "content-type": "application/json"
            })
        })
        document.getElementsByName('no-refresh')[0].style.visibility = 'hidden';
        document.getElementsByName('yes-refresh')[0].style.visibility = 'hidden';
        document.getElementsByName('modal-refresh')[0].style.visibility = 'hidden';
        document.querySelector(".alert h1").innerHTML = '';
        document.querySelector(".alertmsg p").innerHTML = "<br><br>Won't Be Long..";
        setTimeout(window.location.reload(), 300000);
    }
};

$(function(){
	$("button[name='modal-refresh']").click(function(){
        controller.resetAll()
    });
});


$(function(){
	$("button[name='like-button']").click(function(){
        var currentMovie = document.getElementById("hiddenmoviename").value;
        var currentYear = document.getElementById("hiddenmovieyear").value;
        var currentPoster = document.getElementById("hiddenmovieposter").value;
        currentMovieObject = {
            name: currentMovie,
            year: currentYear,
            poster: currentPoster
        };

        fetch(`${window.origin}/_swipe_yes`, {
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
                var matchStatus = data['matchStatus'];
                if (matchStatus == 'true') {
                    view.matchedMovie();
                }
                else {
                    controller.loadMovieData(data);
                }
            })
        })
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
                controller.loadMovieData(data);
            })
        })
    });
});

$(function(){
	$("button[name='refresh-button']").click(function(){
        document.querySelector(".alert h1").innerHTML = 'Refresh?';
        document.querySelector(".alertmsg p").innerHTML = "Are you sure you want to reset all matches and dislikes?";
        document.getElementsByClassName('ModalOverlay')[0].style.visibility = 'visible'
        document.getElementsByClassName('alert')[0].style.visibility = 'visible'
    });
});

$(function(){
	$("button[name='no-refresh']").click(function(){
        document.getElementsByClassName('ModalOverlay')[0].style.visibility = 'hidden'
        document.getElementsByClassName('alert')[0].style.visibility = 'hidden'
    });
});

$(function(){
	$("button[name='yes-refresh']").click(function(){
        controller.resetAll()
    });
});

function init() {};
window.onload = init;
var view = {
    changePoster: function() {
        return document.getElementById("movieposter").src = "https://m.media-amazon.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_SX300.jpg";
        //Remember, Youre pulling data from a database, NOT the API
    },
    changeYear: function() {
        return document.getElementById("movieyear").innerHTML = "2018";
    },
    changeName: function() {
        return document.getElementById("moviename").innerHTML = "Ready Player One";
    }
};

function init() {
    view.changeName();
    view.changeYear();
    view.changePoster();
};

window.onload = init;
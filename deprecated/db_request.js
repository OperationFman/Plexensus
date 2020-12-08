const mysql = require('mysql'); //Sets up as node.js or something

const con = mysql.createConnection({ //Connect to db
  host: '127.0.0.1',
  user: 'root',
  password: 'password',
  database: 'localmoviesdb'
});

function iWonder(digi) {
    con.connect(function(err) {
        if (err) throw err;
        con.query("SELECT * FROM moviedata", function (err, result, fields) {
        if (err) throw err;
        meme = result[digi].name; //selects name from the outputed object, below your randoly generting how that's done
        console.log(meme)

        con.end((err) => {
        });
        });
    });
}

function gener8() {
    x = Math.floor((Math.random() * 10) + 1); //Max number is 10, this is how you can grab by id I think
    return x
  }

function doIt() {
    n = gener8();
    iWonder(n);
}

doIt();

//This get you getting data, figure out how to incorporate this into your site, no idea how you'll get this node.js script displaying on the dom but the heavy lifting is done kinda. Remember it's okay not to use flasks built in method for displaying the site
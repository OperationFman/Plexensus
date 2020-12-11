When you think Plexensus, think 'Tinder for Netflix' (But for your own personal movie files)
This was a small app I built using basic Python and Javascript skills.

How to install:
1. Clone or download this repo somewhere you plan to keep the files on your machine
2. Ensure you have Python 3 and pip installed, guide here: https://phoenixnap.com/kb/install-pip-windows
3. Install the following python packages using Pip: flask, ast and numpy. 
    Alternatively Visual Studio can detect the missing packages and install them for you if you open the folder inside it
4. Open the file 'Plexensus_config.py' in your preferred text editor
5. After 'moviespath', enter the directory of your movies. Be sure you use '/' not '\'
6. Install mysql installer for windows AND connector/python from here: https://dev.mysql.com/downloads/
7. Open MySQL command line client and login/register
8. Create a database wiith this command: CREATE DATABASE localmoviesDB;
9. Paste the following command: CREATE TABLE moviedata (id AUTO_INCREMENT, name varchar(256), year int(4), poster varchar(256), moviematch tinyint(1), nomatch tinyint(1), disliked tinyint(1), PRIMARY KEY (id));
10. Paste this too, swapping the login and pasword to one of your choice: CREATE LOGIN <user> WITH PASSWORD = '<password>'; 
11. Enter the user and password into the 'Plexensus_config.py' on the db user and password fields
12. Lastly sign up for this rapid api, it's free: https://rapidapi.com/rapidapi/api/movie-database-imdb-alternative
13. Click on the 'endpoints' tab, under code snippets open the drop down menu, selects 'Python' then 'Requests'
14. Test your Endpoint to make sure it's all good
15. Copy the 50 character 'x-rapidapi-key' and paste it in the 'Plexensus_config.py file under your api key
16. Open command prompt and type 'ipconfig', hit enter
17. Copy the numbers after IPV4
18. Open 'Plexensus_webapp.py' in your favorite text editor, scroll to the very bottom
19. Replace '192.168.0.214' with your numbers and delete 'debug=true, '
20. Nearly done! Finally shift-rightclick the folder you installed everything into and 'open in powershell'
21. Paste this 'python Plexensus_webapp.py runserver' and press enter
22. Follow the prompt to open the app in your browser. If you're on a PC press F12, at the top to the left there's a small square on a big square for mobile mode
23. As if you did all this lol, good luck

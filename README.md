# Python-Radical-Projects
1 - Make a quiz solver bot with logistic regression (sci-kit learn, datetime, json, and typing, theme : Machine Learning) :
Create a quick game of quiz where a bot gets elections as numpy arrays and selects based on probabilty of acerts, if copmleted, saves on the pickle database for training, also, there is a log of wins and loses for each play session, detailed by date and time.

2 - Show the powers of a number with colored display on cells (pandas, openpypxl and typing, theme : Excel files) :
Create an excel of powers of a number, colored by the settings you want (monochrome and rainbow), there's no limit here.

3 - Extract youtube profile photos (requests and re, theme : Scraping) :
Get page of youtube user based in its name, then, process and look for profile photo using "re" module, after found, copy its bytes and recreating it in local storage, the user can pass the folder where would be stored.

4 - Get roblox avatar of user and friends (request, re, theme : Scraping :
Search the user by id, then, getting his model and avatar data from the official roblox api, specifically, https://thumbnails.roblox.com/v1/users/avatar-3d?userId=1894484118 (this is only an example of where is located), it must be remembered that it needs a cookie to work, you can get one by accesing the .ROBLOXSECURITY cookie in cookies part (You can't share it to nobody because it's possible to access your account with that, the one im using here its from a trashable account, so you can use it, i know some people doesn't have roblox), returing to the description, after accesing the model and avatar json, it searchs for the link to its ubication in the database, then, tests all combinations of the link (because roblox locates it on t1.roblox, t2.roblox, t3.roblox, etc), after the correct one is found, recreates it with bytes on your locale storage and then, searchs for another, it has a wait time because roblox request limit.

5 - Convert scratch games of user to a turbowarp embed link :
Convert scratch page of games of a user to a turbowarp embed link, this is efficient if you want to make a page of all your games, remember, it only extracts the link, not the project file.

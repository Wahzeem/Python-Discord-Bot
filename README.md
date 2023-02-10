# Python-Discord-Bot
A custom Discord bot developed using python that executes several forward slash commands. The commands range from a simple greeting to language translations using external apis.

#Commands
/hello : Tags your Discord username and greets you.

/say : The bot prints out whatever you pass in as an argument. Prefixed by "@username says:".

/dog : Sends a request to an external api and posts a random image of a dog. API = https://dog.ceo/dog-api

/steam_search : Takes in a text argument and searches the steam api for the top result. It then returns the url link for that game. 
API = https://rapidapi.com/psimavel/api/steam2/

/translate_text : Takes in two parameters, language and source text. The bot then uses an external api to translate the source text and posts it within the chat channel. API = https://rapidapi.com/dickyagustin/api/text-translator2/

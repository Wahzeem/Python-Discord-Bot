# Python-Discord-Bot
A custom Discord bot developed using python that executes several forward slash commands. The commands range from a simple greeting to language translations using external apis.

## Commands ##
__/hello__ : Tags your Discord username and greets you.

__/say__ : The bot prints out whatever you pass in as a parameter. Prefixed by "@username says:".

__/dog__ : Sends a request to an external api and posts a random image of a dog. API = https://dog.ceo/dog-api

__/steam_search__ : Passes keywords as parameters to search through the steam API and returns the first game found. 
API = https://rapidapi.com/psimavel/api/steam2/

__/translate_text__ : Takes in two parameters, language and source text. The bot then uses an external api to translate the source text and posts it within the chat channel. API = https://rapidapi.com/dickyagustin/api/text-translator2/

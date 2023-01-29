from flask import Flask
#from flask_cors import CORS
from flask import request
import requests
import json
import re
import destination_media

app = Flask(__name__)

temp_movie_placeholder = "Spider-Man: 3"
movie_set_locations = {"starwars":"Death Valley, CA", "spiderman":"New York, NY", "strangerthings":"Stockbridge, GA", "lordoftherings":"Manawatu-Wanganui, New Zealand", "batman":"Chicago, IL" }

@app.route('/movies/<movie_title>')
def find_set_locations(movie_title):
    destination = ""
    tmp = re.sub(r'[^a-zA-Z]', '', tmp)
    tmp = tmp.lower()
    for location in movie_set_locations:
        if(tmp.__contains__(location)):
            destination = movie_set_locations[tmp]
            return destination
    return "movie/tv show not in database"    

@app.route('/data/<arrival>&<destination>')
def main(destination):
    searchText = destination
    response_API = requests.get(f'https://api.themoviedb.org/3/search/multi?api_key=c5980cbfba7b53631154f2347a5c2464&language=en-US&query={searchText}&page=1&include_adult=false')
    data = response_API.text
    parse_json = json.loads(data)

    movies = []
    tv_shows = []
    persons = []

    for mediaObjectNum in range(len(parse_json['results'])):
        results = parse_json['results']
        CurrentResult = results[mediaObjectNum]
        resultData = None
        if(CurrentResult['media_type']=="tv"):
            tv_shows.append(CurrentResult)
        if(CurrentResult['media_type']=="movie"):
            movies.append(CurrentResult)
        if(CurrentResult['media_type']=="Person"):
            persons.append(CurrentResult)

    



#print(find_set_locations(temp_movie_placeholder))
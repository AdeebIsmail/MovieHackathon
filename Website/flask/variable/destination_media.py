import requests
import json


def main(dest):
    searchText = dest
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

    for movie in movies:
        print(str(movie).replace(",","\n"))

    for tv in tv_shows:
        print(str(tv).replace(",","\n"))

import requests
from werkzeug.exceptions import BadRequest
import json
import pathlib


class Ghibli(object):
    BASE_URL = 'https://ghibliapi.herokuapp.com'
    MOVIES_URL = '/films?fields=id,title&limit=250'
    PEOPLE_URL = '/people?fields=id,name,films&limit=250'
    PEOPLE_LIST = {}
    MOVIES_LIST = {}

    @classmethod
    def get_movies_list(cls):
        """
        {
        id: "58611129-2dbc-4a81-a72f-77ddfc1b1b49",
        title: "My Neighbor Totoro",
        description: "Two sisters move to the country with their father in order to be closer to their hospitalized mother, and discover the surrounding trees are inhabited by Totoros, magical spirits of the forest. When the youngest runs away from home, the older sister seeks help from the spirits to find her.",
        director: "Hayao Miyazaki",
        producer: "Hayao Miyazaki",
        release_date: "1988",
        rt_score: "93",
        people: [
        "https://ghibliapi.herokuapp.com/people/986faac6-67e3-4fb8-a9ee-bad077c2e7fe",
        "https://ghibliapi.herokuapp.com/people/d5df3c04-f355-4038-833c-83bd3502b6b9",
        ],
        species: [
        ],
        locations: [
        ],
        vehicles: [
        ],
        }
                :return:
        """
        response = requests.get(cls.BASE_URL + cls.MOVIES_URL)
        try:
            if response:
                movie_list = json.loads(response.text)
                for movie in movie_list:
                    cls.MOVIES_LIST[movie.get("id")] = {"name": movie.get("title"), "people": []}
        except Exception as e:
            raise BadRequest(e)

    @classmethod
    def get_people_list(cls):
        """[
        {
        "id": "3031caa8-eb1a-41c6-ab93-dd091b541e11",
        "name": "Tatsuo Kusakabe",
        "gender": "Male",
        "age": "37",
        "eye_color": "Brown",
        "hair_color": "Dark Brown",
        "films": [
        "https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49"
        ],
        "species": "https://ghibliapi.herokuapp.com/species/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
        "url": "https://ghibliapi.herokuapp.com/people/3031caa8-eb1a-41c6-ab93-dd091b541e11",
        "length": null
        }
        ]"""
        response = requests.get(cls.BASE_URL + cls.PEOPLE_URL)
        try:
            if response:
                people_list = json.loads(response.text)
                cls.get_movies_list()
                for people in people_list:
                    if people.get("films"):
                        for movie in people.get("films"):
                            movie_id = cls.get_last_fragment(movie)
                            actors = cls.MOVIES_LIST[movie_id].get("people")
                            actors.append(people.get("name"))
                return cls.MOVIES_LIST
        except Exception as e:
            raise BadRequest(e)

    @classmethod
    def get_last_fragment(cls, input):
        return pathlib.PurePath(input).name

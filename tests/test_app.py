import sys
import unittest

from mock import patch

from app import app

sys.path.append("../")


class SennderGhibliTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.get_movies_list = {'2baf70d1-42bb-4437-b551-e5fed5a87abe': {'name': 'Castle in the Sky', 'people': []},
                                '12cfb892-aac0-4c5b-94af-521852e46d6a': {'name': 'Grave of the Fireflies',
                                                                         'people': []},
                                '58611129-2dbc-4a81-a72f-77ddfc1b1b49': {'name': 'My Neighbor Totoro', 'people': []},
                                'ea660b10-85c4-4ae3-8a5f-41cea3648e3e': {'name': "Kiki's Delivery Service",
                                                                         'people': []},
                                '4e236f34-b981-41c3-8c65-f8c9000b94e7': {'name': 'Only Yesterday', 'people': []},
                                'ebbb6b7c-945c-41ee-a792-de0e43191bd8': {'name': 'Porco Rosso', 'people': []},
                                '1b67aa9a-2e4a-45af-ac98-64d6ad15b16c': {'name': 'Pom Poko', 'people': []},
                                'ff24da26-a969-4f0e-ba1e-a122ead6c6e3': {'name': 'Whisper of the Heart', 'people': []},
                                '0440483e-ca0e-4120-8c50-4c8cd9b965d6': {'name': 'Princess Mononoke', 'people': []},
                                '45204234-adfd-45cb-a505-a8e7a676b114': {'name': 'My Neighbors the Yamadas',
                                                                         'people': []},
                                'dc2e6bd1-8156-4886-adff-b39e6043af0c': {'name': 'Spirited Away', 'people': []},
                                '90b72513-afd4-4570-84de-a56c312fdf81': {'name': 'The Cat Returns', 'people': []},
                                'cd3d059c-09f4-4ff3-8d63-bc765a5184fa': {'name': "Howl's Moving Castle", 'people': []},
                                '112c1e67-726f-40b1-ac17-6974127bb9b9': {'name': 'Tales from Earthsea', 'people': []},
                                '758bf02e-3122-46e0-884e-67cf83df1786': {'name': 'Ponyo', 'people': []},
                                '2de9426b-914a-4a06-a3a0-5e6d9d3886f6': {'name': 'Arrietty', 'people': []},
                                '45db04e4-304a-4933-9823-33f389e8d74d': {'name': 'From Up on Poppy Hill', 'people': []},
                                '67405111-37a5-438f-81cc-4666af60c800': {'name': 'The Wind Rises', 'people': []},
                                '578ae244-7750-4d9f-867b-f3cd3d6fecf4': {'name': 'The Tale of the Princess Kaguya',
                                                                         'people': []},
                                '5fdfb320-2a02-49a7-94ff-5ca418cae602': {'name': 'When Marnie Was There', 'people': []}}
        self.html_movies = b'<!DOCTYPE html>\n<html lang="en">\n\n<head>\n\t<meta charset="UTF-8">\n\t<title>Sennder Application</title>\n</head>\n<style type="text/css">\ntable {\n\tmargin: 0 auto;\n}\n\ntable.one {\n\tborder-collapse: collapse;\n}\n\ntable.two {\n\tborder-collapse: separate;\n}\n\ntd.a {\n\tborder-style: dotted;\n\tborder-width: 1px;\n\tborder-color: #000000;\n\tpadding: 5px;\n\tfont-weight: bold;\n\ttext-align: center;\n}\n\ntd.b {\n\tborder-style: solid;\n\tborder-width: 1px;\n\tborder-color: #333333;\n\tpadding: 5px;\n}\n</style>\n\n<body>\n\t<div class="one">\n\t\t<table id="server_side_push">\n\t\t\t<tr>\n\t\t\t\t<td class="a">Movie Name</td>\n\t\t\t\t<td class="a">Actors</td>\n\t\t\t</tr>\n\t\t\t<tr> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Castle in the Sky</TD>\n\t\t\t\t<TD class="b">Colonel Muska</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Grave of the Fireflies</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">My Neighbor Totoro</TD>\n\t\t\t\t<TD class="b">Satsuki Kusakabe,Mei Kusakabe,Tatsuo Kusakabe,Yasuko Kusakabe,Granny,Kanta Ogaki,Totoro,Chu Totoro,Chibi Totoro,Catbus</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Kiki&#39;s Delivery Service</TD>\n\t\t\t\t<TD class="b">Jiji</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Only Yesterday</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Porco Rosso</TD>\n\t\t\t\t<TD class="b">Porco Rosso</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Pom Poko</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Whisper of the Heart</TD>\n\t\t\t\t<TD class="b">Renaldo Moon aka Moon aka Muta,Baron Humbert von Gikkingen</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Princess Mononoke</TD>\n\t\t\t\t<TD class="b">Ashitaka,San,Eboshi,Jigo,Kohroku,Gonza,Hii-sama,Yakul,Shishigami,Moro</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">My Neighbors the Yamadas</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Spirited Away</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">The Cat Returns</TD>\n\t\t\t\t<TD class="b">Renaldo Moon aka Moon aka Muta,Cat King,Yuki,Haru,Baron Humbert von Gikkingen,Natori</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Howl&#39;s Moving Castle</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Tales from Earthsea</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Ponyo</TD>\n\t\t\t\t<TD class="b">Sosuke</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">Arrietty</TD>\n\t\t\t\t<TD class="b">Niya</TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">From Up on Poppy Hill</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">The Wind Rises</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">The Tale of the Princess Kaguya</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR> \n\t\t\t<TR>\n\t\t\t\t<TD class="b">When Marnie Was There</TD>\n\t\t\t\t<TD class="b"></TD>\n\t\t\t</TR>  </tr>\n        <tr>\n\t\t\t\t<td class="a">For Demo</td>\n\t\t\t\t<td class="a">Added Extra Row</td>\n\t\t\t</tr>\n\n\t\t</table>\n\t</div>\n</body>\n<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n<script>\nvar server_push_messages = new EventSource(\'/stream\');\nserver_push_messages.onmessage = function(event) {\n\tif(event.data) {\n\t\t$(\'#server_side_push\').replaceWith(event.data);\n\t}\n};\n</script>'

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/movies')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    @patch('apis.ghibli.Ghibli')
    def test_get_movies_list(self, MockGhibli):
        MockGhibli.get_movies_list.return_value = self.get_movies_list
        self.assertEqual(self.get_movies_list, MockGhibli.get_movies_list.return_value)

    def test_home_movies_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/movies')
        # assert the status code of the response
        self.assertEqual(result.data, self.html_movies)
        self.assertEqual(result.status_code, 200)

    def get_app(self):
        return app

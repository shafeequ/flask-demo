import hashlib
import json
import sys

from apis.ghibli import Ghibli
import flask
from flask import Flask, render_template
from flask_cors import CORS

sys.path.append("./apis/")

app = Flask(__name__)
CORS(app)  ## To allow direct AJAX calls


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movies', methods=['GET'])
def home():
    """This API End Point used to return the Actors and their movies against to it"""
    response = Ghibli.get_people_list()
    write_response_hash(response)
    return render_template('movies.html', response=response)


def write_response_hash(response):
    """Write the hash of the response in reality it should be the ETag of the response so that we will not make
    unnecessary call to Ghili API unless there is any changes in the Movies or Actors
    """
    people_list_hash = hash_response(response)
    with open("api_response.hash", "w") as file:
        file.write(people_list_hash)


def get_response_hash():
    """ COmpare the response hash , in reality it will will be ETag"""
    with open("api_response.hash", "r") as file:
        return file.read()


def hash_response(response):
    """Generates the Hash of the response"""
    res = json.dumps(response)
    return hashlib.md5(res.encode()).hexdigest()


def get_message():
    '''Make REST Head call to check if the server state has changed if yes then make call and get it based on ETag'''
    response = Ghibli.get_people_list()
    previous_api_call_response = get_response_hash()
    current_api_call_response = hash_response(response)
    if previous_api_call_response != current_api_call_response:
        write_response_hash(current_api_call_response)
        return response

    # return response
    return {}


def get_table_rows(data):
    """Prepare the response in Table format"""
    trs = '<tr><td class="a">Movie Name</td><td class="a">Actors</td></tr>'
    for key, record in data.items():
        trs += '<TR><TD class="b">{}</TD><td class="b">{}</TD></TR>'.format(record.get("name"),
                                                                            ",".join(record.get("people")))
    return trs


@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            r = get_message()
            if r:
                yield 'data: {}\n\n'.format(get_table_rows(r))
            else:
                yield 'data:'

    return flask.Response(eventStream(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True, port=8000, threaded=True)
# Not giving more config options , because i want this to be plug and play

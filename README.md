**Why Flask?**

Python has a number of web frameworks that can be used to create web apps and APIs.(Django very popular) I have
 selected Flask because Flask applications tend to be written on a blank canvas being light weight and micro framework
suited to a contained application such as our Task for building Web-APIs and non enterprise applications**

#### System Architechture used for building 
```sh
# uname -a
# Linux AMD 5.3.0-51-generic #44~18.04.2-Ubuntu SMP Thu Apr 23 14:27:18 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

```

####Dependencies / prerequiste

```sh
apt-get install python3 
```


### Implementation  Logic
- I have used the Server Sent Events logic
- Server make an Ghibli API call , stores the  content/hash in local file and sends the content to client
- After the page is loaded the content from server the connection is kept active and listen for incoming events from
 server
- server makes an API call to the Ghibli API (every minute) to check if there are any changes in server state (Actor
/movies
 Modification) ( ideally this can be done throug ETag but Ghibli API has not implemented that we need to make an
  actual API call to see the content has changed by checking the hashed response)
- if there is any changes then write the new hash to the file and return the fresh contents to the client if there is
 no changes then do not send the content to client
 
- if there is any content coming from server then the client will refresh its view with the latest content otherwise not

- NOTE: to make the network  load and optimized call. I am only requesting the fields i am interested in the
 displaying and hence other data is not requested 
- All application is grouped and categorized in very well structure


### Application Tests
```shell script
(env) shafeequ-ahmed@AMD:~/demo/sennder$ python -m unittest tests/test_app.py -vv
test_get_movies_list (tests.test_app.SennderGhibliTests) ... ok
test_home_movies_data (tests.test_app.SennderGhibliTests) ... ok
test_home_status_code (tests.test_app.SennderGhibliTests) ... ok

----------------------------------------------------------------------
Ran 3 tests in 3.183s

OK
(env) shafeequ-ahmed@AMD:~/demo/sennder$ 

```
### Installation

- Option#1 Setup through Script 
```sh
source setup.sh 
```

- Option#2  Manually setup
```sh
$ copy the sennder folder any where on your system
$  cd sennder
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python app.py  # will yield the following


 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 271-060-571

127.0.0.1 - - [21/May/2020 20:45:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [21/May/2020 20:45:42] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [21/May/2020 20:46:53] "GET /api/v1/ui/ HTTP/1.1" 200 -
127.0.0.1 - - [21/May/2020 20:46:54] "GET /api/v1/swagger.json HTTP/1.1" 200 -
```


- Step#2
> Your are already done Hurray :-) , Just  Click [Localhost](http://127.0.0.1:8000/movies) For Validating your
> requirement
>
> Author Details [Localhost](http://127.0.0.1:8000/)


### Application Structure
```shell script
├── api_response.hash
├── apis
│   ├── ghibli.py
│   └── __init__.py
├── app.py
├── __init__.py
├── README.md
├── requirements.txt
├── setup.sh
├── static
│   └── stream.js
├── templates
│   ├── index.html
│   └── movies.html
└── tests
    └── test_app.py

4 directories, 12 files

```

### Working Demo
> https://bit.ly/sennder_demo
>
>
### Improvemnets
- the Gibli API is not implemnetd as per the REST Standard , it should provide header options ETag so that
the client can cache data and make calls only if the serve rstate has change dby Requesting the ETag header options
- the gibli api shoul provide the format to filter the results
- Ghibli API is not stable and yields results not in the json content type but text type

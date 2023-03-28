# Assignment 2 - Adding a Database and Dockerize
### Author: Ginger Ciaburri

### Requirements
Python Version: 3.9

Requirements can be found in requirements.txt

### Start the Flask webserver
First run:
```bash
$ python ner_flask_webserver.py
```
To access the website, point a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

This website contains a form on the home page. Enter the desired text to be processed by Spacy. 
Pressing Submit will show you the NER processing on a second page. There is also the option to 
see all of the entities ever entered by clicking List from either the Home page or the NER 
Results page.


### Build image and run Docker container
To build the image, run:
```bash
$ docker build -t assignment2 .
```
To run the Docker container which will start the webserver, run:
```bash
$ docker run --rm --detach -p 5000:5000 --name=webserver assignment2
```
To access the website, point a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).
To close the container, run:
```bash
$ docker container stop webserver
```

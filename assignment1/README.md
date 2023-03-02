# Assignment 1 - Web Services
### Author: Ginger Ciaburri

### Requirements
Python Version: 3.9

Requirements can be found in requirements.txt


### RESTful API using Flask
To run this restful service that responds to both a GET and a POST request at the same URL:

First run:
```bash
$ python ner_restfulAPI.py
```
In a separate terminal, run the follow two commands for the GET and POST requests.
```bash
$ curl http://127.0.0.1:5000/api
$ curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```


### Flask webserver
First run:
```bash
$ python ner_restfulAPI.py
```
To access the website, point a browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

This website contains a form on the home page. Enter the desired text to be processed by Spacy. 
Pressing Send to Spacy will show you the NER processing on a second page. 


### Streamlit
First run:
```bash
 $ streamlit run ner_streamlit.py
```
To access the website, point the browser at [http://localhost:8501/](http://localhost:8501/). 
After pressing run, you will be able to see options for seeing the NER results as well as POS Tagging. 





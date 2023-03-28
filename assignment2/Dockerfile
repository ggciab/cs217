FROM python:3.9-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 5000
CMD ["python", "ner_flask_webserver.py"]

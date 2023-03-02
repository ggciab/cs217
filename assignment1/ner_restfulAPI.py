from flask import Flask, request
from flask_restful import Resource, Api
from ner import SpacyDocument

app = Flask(__name__)
api = Api(app)


class ProcessNER(Resource):
    def get(self):
        return {'NER Service': 'This NER service takes in a .txt and returns the '
                               'NER results from Spacy'}

    def post(self):
        text = request.get_data(as_text=True)
        sd = SpacyDocument(text)
        return {'returning': sd.get_entities()}, 201


api.add_resource(ProcessNER, '/api')


if __name__ == '__main__':
    app.run(debug=True)

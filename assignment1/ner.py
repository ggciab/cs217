"""ner.py

Run spaCy NER over an input string and insert XML tags for each entity.

"""

import io
from collections import Counter

import spacy
nlp = spacy.load("en_core_web_sm")

COLORS = {"PERSON": "#aa9cfc", "ORG": "#7aecec", "GPE": "#feca74", "LOC": "#ff9561", "FAC": "#ddd",
          "NORP": "#c887fb", "EVENT": "#ffeb80", "DATE": "#bfe1d9", "TIME": "#bfe1d9",
          "CARDINAL": "#e4e7d2", "ORDINAL": "#e4e7d2", "QUANTITY": "#e4e7d2", "PERCENT": "#e4e7d2",
          "MONEY": "#e4e7d2", "LANGUAGE": "#ff8197", "PRODUCT": "#bfeeb7", "WORK_OF_ART": "#f0d0ff"}


class SpacyDocument:
    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    def get_tokens(self):
        return [token.lemma_ for token in self.doc]

    def get_pos_tags(self):
        return [token.pos_ for token in self.doc]

    def get_entities(self):
        entities = []
        for e in self.doc.ents:
            entities.append((e.start_char, e.end_char, e.label_, e.text))
        return entities

    def get_entities_with_markup(self):
        entities = self.doc.ents
        starts = {e.start_char: e.label_ for e in entities}
        ends = {e.end_char: True for e in entities}
        buffer = io.StringIO()
        for p, char in enumerate(self.text):
            if p in ends:
                buffer.write('</entity>')
            if p in starts:
                buffer.write('<entity class="%s">' % starts[p])
            buffer.write(char)
        markup = buffer.getvalue()
        return '<markup>%s</markup>' % markup

    def get_percentages_for_labels(self):
        entities = self.doc.ents
        text = self.text
        percents = Counter()
        previous_end = 0
        num_entities = len(entities)
        for idx, e in enumerate(entities):
            percents["Unlabeled"] += e.start_char - previous_end
            percents[e.label_] += e.end_char - e.start_char
            previous_end = e.end_char
            if idx == num_entities - 1:
                percents["Unlabeled"] += len(text) - previous_end
        total = sum(percents.values())
        percents = {key: val/total*100 for key, val in percents.items()}
        return percents.keys(), percents.values()

    def get_entities_for_annotated_text(self, desired_entities):
        entities = self.doc.ents
        # make random colors: probably should have something hard coded so it's the same
        text = self.text
        annotated_text = []
        num_entities = len(entities)
        previous_end = 0
        for idx, e in enumerate(entities):
            if e.label_ in desired_entities:
                annotated_text.append(text[previous_end:e.start_char])  # Add middle text
                annotated_text.append((text[e.start_char:e.end_char], e.label_, COLORS.get(e.label_),))
                previous_end = e.end_char
            if idx == num_entities - 1:
                annotated_text.append(text[previous_end:])
        return annotated_text

    def get_POS_tags_for_annotated_text(self, desired_tags):
        annotated_text = []
        for token in self.doc:
            if token.pos_ in desired_tags:
                annotated_text.append((token.lemma_ + " ", token.pos_,))
            else:
                annotated_text.append(token.lemma_ + " ")
        return annotated_text



if __name__ == '__main__':

    example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

    doc = SpacyDocument(example)
    print(doc.get_tokens())
    for entity in doc.get_entities():
        print(entity)
    print(doc.get_entities_with_markup())

from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
import spacy

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        if not 'sentence' in query_params:
            self.send_error(400,'No sentences provided')
            return

        sentences = query_params['sentence']
        sentence = sentences[0]

        doc = nlp(sentence)
        lems=[token.lemma_ for token in doc]

        response = {'lemmas':lems}

        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
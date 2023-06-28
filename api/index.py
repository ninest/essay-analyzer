from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
from analyzer.repeated_words import get_repeated_word_map
from analyzer.readability import get_readability


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        query_params = parse_qs(url.query)

        if not "sentence" in query_params:
            self.send_error(400, "No sentences provided")
            return

        sentences = query_params["sentence"]
        sentence = sentences[0]

        repeated_words = get_repeated_word_map(sentence)
        readability = get_readability(sentence)

        response = {
            "repeated_words": repeated_words.to_dict(),
            "readability": readability.to_dict(),
        }

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))
        return

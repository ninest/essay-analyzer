import json


class JSON:
    def to_json(self):
        return json.dumps(self.__dict__)

import json
import re


class JSON:
    def to_dict(self):
        result = {}
        for key, value in self.__dict__.items():
            camel_case_key = re.sub(
                r"_([a-z])", lambda match: match.group(1).upper(), key
            )
            result[camel_case_key] = value
        return result

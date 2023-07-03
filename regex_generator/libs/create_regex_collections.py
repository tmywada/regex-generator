import json
import re


class CreateRegexCollections:
    def __init__(self):
        file_path_definition = (
            "./regex_generator/config/definition__regex.json"
        )
        self.definitions = json.load(open(file_path_definition, "r"))
        self.categories = list(self.definitions.keys())
        self.category_name_base = "base"
        self.regexes = []
        self.regex_id = 0

    def load_regexes_base(self):
        _regexes = []
        for k, v in self.definitions[self.category_name_base].items():
            _pattern = f"[{v}]"
            _regexes.append(
                {
                    "category": self.category_name_base,
                    "name": k,
                    "tags": [k],
                    "pattern": _pattern,
                    "regex": re.compile(_pattern),
                    "regex_id": self.regex_id,
                }
            )
            self.regex_id += 1
        return _regexes

    def load_regexes_other(self, category: str):
        """ """

        def _load_regex_ids(regexes: list):
            return {v["name"]: v["regex_id"] for v in regexes}

        _regexes = []
        _dict_regex_ids = _load_regex_ids(self.regexes)
        for k, v in self.definitions[category].items():
            _pattern = "["
            for regex_type in v:
                _idx = _dict_regex_ids[regex_type]
                _obj = self.regexes[_idx]
                _pattern += _obj["pattern"][1:-1]  # exclude squre brackets
            _pattern += "]"
            _regexes.append(
                {
                    "category": category,
                    "name": k,
                    "tags": v,
                    "pattern": _pattern,
                    "regex": re.compile(_pattern),
                    "regex_id": self.regex_id,
                }
            )
            self.regex_id += 1
        return _regexes


def ingest_definition():
    crc = CreateRegexCollections()

    # --- base
    crc.regexes.extend(crc.load_regexes_base())

    # --- other (except base)
    categories = [v for v in crc.categories if v != crc.category_name_base]
    for category in categories:
        crc.regexes.extend(crc.load_regexes_other(category=category))
    return crc.regexes

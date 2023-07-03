class SelectRegex:
    def __init__(self, collections: dict, regex_types: list):
        self.regex_selected = {}
        self.collections = collections
        self.regex_types = regex_types

    def select_regex(self):
        for collection in self.collections:
            if collection["name"] in self.regex_types:
                _idx = collection["regex_id"]
                _regex = collection["regex"]
                _pattern = collection["pattern"]
                self.regex_selected[_regex] = {
                    "idx": _idx,
                    "pattern": _pattern,
                }

    def add_regex(self, name: str):
        for collection in self.collections:
            if collection["name"] == name:
                _idx = collection["regex_id"]
                _regex = collection["regex"]
                _pattern = collection["pattern"]
                self.regex_selected[_regex] = {
                    "idx": _idx,
                    "pattern": _pattern,
                }
                break

    def remove_regex(self, name: str):
        self.regex_selected.pop(name)

import json
import re


class Utilities:

    def __init__(self, file_path_definition, categories):
        self.definitions = json.load(open(file_path_definition, 'r'))
        self.category_name_base = 'base'
        self.regexes = {}
        self.regex_id = 0
        self.dict_regex_ids = {}

    def load_regexes_base(self):
        _regexes = {}
        _dict_regex_ids = {}
        for k,v in self.definitions[self.category_name_base].items():
            _pattern = f'[{v}]'
            _regexes[self.regex_id] = {
                'category': self.category_name_base,
                'name': k,
                'tags': [k],
                'pattern': _pattern,
                'regex': re.compile(_pattern)
            }
            _dict_regex_ids[k] = self.regex_id
            self.regex_id += 1
        return (_regexes, _dict_regex_ids)        

    def load_regexes_per_category(self, category: str):
        """ """
        _regexes = {}
        _dict_regex_ids = {}
        for k,v in self.definitions[category].items():
            _pattern = '['
            for regex_type in v:
                _idx = self.dict_regex_ids[regex_type]
                _obj = self.regexes[_idx]
                _pattern += _obj['pattern'][1:-1] # exclude squre brackets
            _pattern += ']'
            _regexes[self.regex_id] = {
                'category': category,
                'name': k,
                'tags': [k],
                'pattern': _pattern,
                'regex': re.compile(_pattern)
            }
            _dict_regex_ids[k] = self.regex_id
            self.regex_id += 1
        return (_regexes, _dict_regex_ids)

    
def ingest_definition(file_path_definition: str, categories: list):
    utils = Utilities(file_path_definition, categories)
    for category in categories:
        if category == utils.category_name_base:
            _regexes, _dict_regex_ids = utils.load_regexes_base()
        else:
            _regexes, _dict_regex_ids = utils.load_regexes_per_category(
                category=category
            )
        utils.regexes.update(_regexes)
        utils.dict_regex_ids.update(_dict_regex_ids)
    return (utils.regexes, utils.dict_regex_ids)

import re
import json
from itertools import groupby
from src.DefinitionIngestor import ingest_definition


class RegexGenerator:
    def __init__(self, file_path_config):
        config = json.load(open(file_path_config, 'r'))
        _regexes, _dict_regex_ids = ingest_definition(
            file_path_definition=config['file_path_definition'],
            categories=config['categories']
        )
        self.regexes = _regexes
        self.dict_regex_ids = _dict_regex_ids
        self.regex_types_coase = config['regex_types_coase']
        self.regex_selected_coase = self.select_regex_coase()
        self.regex_unrecognized_ch = '.'

    def select_regex_coase(self):
        res = {}
        for regex_type in self.regex_types_coase:
            _idx = self.dict_regex_ids[regex_type]
            _regex = self.regexes[_idx]['regex']
            res[_regex] = _idx
        return res

    def encode_string(self, string: str):
        indices = []
        for ch in string:
            found_regex = False
            for regex,idx in self.regex_selected_coase.items():
                if re.match(regex, ch):
                    indices.append(str(idx)) # string conversion is needed to concatenate
                    found_regex = True
                    break
            if found_regex == False:
                indices.append('A')
        return indices
    
    def compress_encoded_string(self, string: str):
        """
        ref: https://stackoverflow.com/a/59183023
        """
        return (
            (x, sum(1 for _ in y)) for x, y in groupby(self.encode_string(string))
        )
   
    def generate_regex_coase(self, string: str):
        _regex = ''
        for k,v in self.compress_encoded_string(string):
            try:
                _idx = int(k)
                _regex += self.regexes[_idx]['pattern']
            except:
                _regex += self.regex_unrecognized_ch
            if v > 1:
                _regex += f"{{{v}}}"
        return _regex

    def generate_regexes_coase(self, values: list):
        return [self.generate_regex_coase(v)for v in values]

# def is_ascii(s):
#     return all(ord(c) < 128 for c in s)

# def isascii(s):
#     """Check if the characters in string s are in ASCII, U+0-U+7F."""
#     return len(s) == len(s.encode())



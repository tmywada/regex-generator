import re
from itertools import groupby


class Generator:
    def __init__(self, regexes):
        self.regexes = regexes
        self.map_idx_pattern = {
            v["idx"]: v["pattern"] for _, v in regexes.items()
        }
        self.regex_unrecognized_ch = "."

    def encode_string(self, string: str):
        indices = []
        for ch in string:
            found_regex = False
            for regex, vs in self.regexes.items():
                if re.match(regex, ch):
                    indices.append(
                        str(vs["idx"])
                    )  # string conversion is needed to concatenate
                    found_regex = True
                    break
            if found_regex is False:
                indices.append("A")
        return indices

    def compress_encoded_string(self, string: str):
        """
        ref: https://stackoverflow.com/a/59183023
        """
        return (
            (x, sum(1 for _ in y))
            for x, y in groupby(self.encode_string(string))
        )

    def generate_regex(self, string: str):
        _regex = ""
        for k, v in self.compress_encoded_string(string):
            try:
                _idx = int(k)
                _regex += self.map_idx_pattern[_idx]
            except Exception:
                _regex += self.regex_unrecognized_ch
            if v > 1:
                _regex += f"{{{v}}}"
        return _regex

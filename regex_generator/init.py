from regex_generator.libs import SelectRegex
from regex_generator.libs import Generator
from regex_generator.libs import generate_collections


def init():
    collections, regex_types = generate_collections()
    sr = SelectRegex(collections=collections, regex_types=regex_types)
    sr.select_regex()
    return Generator(sr.regex_selected)

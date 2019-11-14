"""
db less objects for simulation
"""

import json


class Blockchain(object):
    def __init__(self, blocks):
        self.blocks = blocks

    @classmethod
    def from_file(cls, file_name: str) -> "Blockchain":
        with open(file_name) as fp:
            blocks = json.load(fp)
        return Blockchain(blocks)


class Block(object):
    def __init__(self, time, index, target=None, special_min=False, **kwargs):
        self.time = time
        self.index = index
        self.target = target
        self.special_min = special_min

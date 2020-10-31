# Author: Huikang Zhang(huikang@deepmotion.ai)

import json
from typing import List,Union,Callable

class JsonInterf(object):

    def __init__(self):
        pass

    @staticmethod
    def save(content:dict,path:str):
        with open(path, 'w') as output_file:
            output_file.write(json.dumps(content, indent=4))

    @staticmethod
    def read(path:dir)->dict:
        return json.loads(open(path).read())
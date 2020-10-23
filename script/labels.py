# -*- coding: utf-8 -*-
import yaml
from pathlib import Path

class labels:

    script_location = Path(__file__).absolute().parent
    
    def __init__(self, FilePath = script_location / 'labels.yml'):

        # Load the yml config file
        with open(FilePath, encoding='utf-8') as ymlfile:
            self.data = yaml.load(ymlfile)
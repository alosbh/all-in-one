# -*- coding: utf-8 -*-
import yaml

class FI:

    def __init__(self, FilePath = "FI.yml"):

        # Load the yml config file
        with open(FilePath, 'r') as ymlfile:
            self.data = yaml.load(ymlfile);


        
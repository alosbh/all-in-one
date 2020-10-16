# -*- coding: utf-8 -*-
import yaml

class labels:

    def __init__(self, FilePath = "labels.yml"):

        # Load the yml config file
        with open(FilePath, 'r') as ymlfile:
            self.data = yaml.load(ymlfile);


        
# -*- coding: utf-8 -*-
import yaml

class labels:

    def __init__(self, FilePath = "C:/www/all-in-one/script/labels.yml"):

        # Load the yml config file
        with open(FilePath, encoding="utf8") as ymlfile:
            self.data = yaml.load(ymlfile);


        
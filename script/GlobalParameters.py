# -*- coding: utf-8 -*-
import yaml
import os
from pathlib import Path

class GlobalParameters:

    script_location = Path(__file__).absolute().parent

    def __init__(self, FilePath = script_location / 'GlobalParameters.yml'):

        # Load the yml config file
        with open(FilePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile);

        # Set the display parameters
        self.Screen_Width = cfg['Screen']['Width'];
        self.Screen_Height = cfg['Screen']['Height'];
        self.Screen_FullSreen = cfg['Screen']['FullSreen'];

        # Set the thread parameters
        self.BadgeReader_MininumGoodReads = cfg['BadgeReader']['MinimumGoodsReads'];
        self.BadgeReader_ThreadTime = cfg['BadgeReader']['BadgeReadFrequency'];

        # Set the All in One Current Version
        self.AIO_Version = cfg['Version']['Actual'];
        
# -*- coding: utf-8 -*-
import yaml

class GlobalParameters:

    def __init__(self, FilePath = "C:/www/all-in-one/script/GlobalParameters.yml"):

        # Load the yml config file
        with open(FilePath, encoding="utf8") as ymlfile:
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
        
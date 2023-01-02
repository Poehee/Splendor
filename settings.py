# settings
# Plagiated from https://alexandra-zaharia.github.io/posts/python-configuration-and-dataclasses/
# Data "class" :-) : https://realpython.com/python-data-classes

from configparser import ConfigParser
from dataclasses import dataclass

@dataclass
class Sections:
    raw_sections: dict

    def __post_init__(self):
        for section_key, section_value in self.raw_sections.items():
            setattr(self, section_key, SectionContent(section_value.items()))

@dataclass
class SectionContent:
    raw_section_content: dict

    def __post_init__(self):
        for section_content_k, section_content_v in self.raw_section_content:
            # print( section_content_k, section_content_v)
            #  
            setattr(self, section_content_k, int(section_content_v))

class Config(Sections):
    def __init__(self, raw_config_parser):
        Sections.__init__(self, raw_config_parser)

conf = ConfigParser()
conf.read('./settings.ini')
config = Config(conf)

if __name__ == "__main__":
    new_config = Config(conf)
    print ("new_config.constants.nr_of_rares:", new_config.chipcount.rares)
    print ("new_config.constants.board_size:", new_config.constants.board_size)
    print (type(new_config.chipcount.rares))

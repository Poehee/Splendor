# settings
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
            setattr(self, section_content_k, section_content_v)

class Config(Sections):
    def __init__(self, raw_config_parser):
        Sections.__init__(self, raw_config_parser)


conf = ConfigParser()
conf.read('./settings.ini')

if __name__ == "__main__":
   constants = ConfigParser()
   constants.read("./settings.ini")
   print( repr( constants) )
   print( constants.get("constants", "nr_of_rares") )

new_config = Config(conf)
# [mysection]
# mykey = 1
print (new_config.constants.nr_of_rares)

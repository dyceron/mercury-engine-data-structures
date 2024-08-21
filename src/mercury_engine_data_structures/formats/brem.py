import construct

from mercury_engine_data_structures.formats import standard_format
from mercury_engine_data_structures.formats.base_resource import BaseResource
from mercury_engine_data_structures.game_check import Game


class Brem(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> construct.Construct:
        return standard_format.game_model('CEnvironmentMusicPresets', "4.0.2")

from typing import Type

from mercury_engine_data_structures.formats.base_resource import BaseResource
from mercury_engine_data_structures.formats.pkg import Pkg

AssetType = str
AssetId = int

ALL_FORMATS = {
    "PKG": Pkg,
}


def format_for(type_name: AssetType) -> Type[BaseResource]:
    return ALL_FORMATS[type_name.upper()]

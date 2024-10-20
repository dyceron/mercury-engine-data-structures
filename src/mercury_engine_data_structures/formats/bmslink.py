from __future__ import annotations

from typing import TYPE_CHECKING

import construct
from construct import Construct
from construct.core import (
    Byte,
    Const,
    Int32ul,
    LazyBound,
    PrefixedArray,
    Struct,
)

from mercury_engine_data_structures.base_resource import BaseResource
from mercury_engine_data_structures.common_types import Float, StrId, VersionAdapter

if TYPE_CHECKING:
    from mercury_engine_data_structures.game_check import Game

UnkStruct = Struct(
    unk1=StrId,
    unk2=Byte,
    unk3=Float,
    unk4=StrId,
    unk5=StrId,
    unk6=Float,
    unk7=Byte,
    unk8=construct.core.If(
        construct.this.unk5 != "Portal",
        StrId,
    ),
    children=PrefixedArray(Int32ul, LazyBound(lambda: UnkStruct)),
)

Item = Struct(
    name=StrId,
    type=StrId,
    unk1=StrId,
    unk2=Float,
    unk3=StrId,
    unk4=Float,
    unk5=StrId,
    unk6=Byte,
    unk7=Byte,
    unk8=StrId,
    unk9=Byte,
    unk10=Byte,
    unk11=Byte,
    unk12=Float,
    unk13=UnkStruct,
)

LocationStruct = Struct(name=StrId, items=PrefixedArray(Int32ul, Item))

BMSLINK = Struct(
    _magic=Const(b"LINK"),
    version=VersionAdapter("1.31.0"),
    unk_bool=Byte,
    location=LocationStruct,
)


class Bmslink(BaseResource):
    @classmethod
    def construct_class(cls, target_game: Game) -> Construct:
        return BMSLINK

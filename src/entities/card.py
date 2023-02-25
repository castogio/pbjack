""" 
    PBJack -- play black jack on your CLI
    Copyright (C) 2023 Gioacchino Castorio

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. 
"""

from enum import StrEnum, IntEnum
from dataclasses import dataclass

class Suit(StrEnum):
    DIAMOND = 'DIAMOND'
    CLUB = 'CLUB'
    HEART = 'HEART'
    SPADE = 'SPADE'

class Rank(IntEnum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

@dataclass
class Card:
    rank: Rank
    suit: Suit



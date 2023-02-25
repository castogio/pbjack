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

from dataclasses import dataclass
from enum import StrEnum
from .wallet import Wallet
from .carddeck import PlayerDeck

class PlayerType(StrEnum):
    HUMAN = 'human'
    CPU = 'cpu'

@dataclass
class Player:
    type: PlayerType
    wallet: Wallet
    deck: PlayerDeck

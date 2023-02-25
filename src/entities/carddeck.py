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

from .card import Card
import random

class DealerDeck:

    def __init__(self) -> None:
        self._cards: list[Card] = list()
    
    def shuffle(self) -> None:
        random.shuffle(self._cards)
    
    def take_cards(self, amount: int = 1) -> list[Card]:
        taken = self._cards[-amount:]
        del self._cards[-amount:]
        return taken
    
    def is_empty(self) -> bool:
        return not bool(self._cards)
    
class PlayerDeck:
        
    def __init__(self) -> None:
        self._cards: list[Card] = list()


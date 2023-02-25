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

from src.entities.card import Card, Rank, Suit
from src.entities.carddeck import DealerDeck, PlayerDeck
from src.entities.player import Player, PlayerType
from src.entities.wallet import Wallet


if __name__ == '__main__':

    deck = DealerDeck()
    deck._cards.append(Card(Rank.ACE, Suit.HEART))
    deck._cards.append(Card(Rank.JACK, Suit.DIAMOND))
    deck._cards.append(Card(Rank.ACE, Suit.CLUB))
    deck._cards.append(Card(Rank.SEVEN, Suit.SPADE))

    deck.shuffle()

    taken = deck.take_cards(amount=10)
    print(taken)
    print(deck._cards)
    print(deck.is_empty())

    player = Player(type=PlayerType.HUMAN, wallet=Wallet(), deck=PlayerDeck())
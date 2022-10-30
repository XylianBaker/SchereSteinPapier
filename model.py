# Model for rock paper scissors game to manage the player and the computer, moves, current round of the game,
# current score and the game itself
# Authors: Jan Kammellander
# Date: 30.10.2022 Version: 1.0

import random


class Player:
    def __init__(self, name):
        self.name = name
        self.move = None
        self.score = 0
        self.round = 0

    def set_move(self, move):
        self.move = move

    def set_score(self, score):
        self.score = score

    def set_round(self, round):
        self.round = round


class Computer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def set_move(self, move):
        self.move = move

    def get_move(self):
        self.move = random.choice(['rock', 'paper', 'scissors'])
        return self.move


class Game:
    def __init__(self):
        self.player = Player('Player')
        self.computer = Computer('Computer')
        self.round = 1
        self.winner = None

    def set_round(self, round):
        self.round = round

    def set_winner(self, winner):
        self.winner = winner

    def get_winner(self):
        return self.winner

    def get_round(self):
        return self.round

    def get_computer_move(self):
        return self.computer.get_move()

    def get_player_move(self):
        return self.player.move

    def get_computer_score(self):
        return self.computer.score

    def get_player_score(self):
        return self.player.score

    def get_player_name(self):
        return self.player.name

    def get_computer_name(self):
        return self.computer.name

    def set_computer_score(self, score):
        self.computer.score = score

    def set_player_score(self, score):
        self.player.score = score

    def set_player_move(self, move):
        self.player.move = move

    def set_computer_move(self, move):
        self.computer.move = move

    def is_tie(self):
        if self.player.move == self.computer.move:
            return True
        else:
            return False

    def is_player_winner(self):
        if self.player.move == 'rock' and self.computer.move == 'scissors':
            return True
        elif self.player.move == 'paper' and self.computer.move == 'rock':
            return True
        elif self.player.move == 'scissors' and self.computer.move == 'paper':
            return True
        else:
            return False

    def get_round_winner(self):
        if self.is_player_winner():
            return self.player.name
        elif self.is_computer_winner():
            return self.computer.name
        else:
            return None

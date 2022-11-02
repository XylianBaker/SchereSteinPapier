# Controller for the qt gui for the rock paper scissors game
# Authors: Jan Kammellander
# Date: 30.10.2022 Version: 1.0

import sys
from PyQt6.QtWidgets import QApplication
import model
import view


class Controller:
    def __init__(self):
        self.model = model.Game()
        self.view = view.View(self)
        self.view.show()

    def execute(self):
        self.model.set_player_move(self.view.get_player_move())
        self.model.set_computer_move(self.model.get_computer_move())
        # self.view.set_text_player_move(self.model.get_player_move())
        # self.view.set_text_computer_move(self.model.get_computer_move())
        self.view.set_image(self.model.get_player_move(), self.model.get_computer_move())
        if self.model.is_tie():
            self.view.set_text_statusbar('Unentschieden')
        elif self.model.is_player_winner():
            self.model.set_player_score(self.model.get_player_score() + 1)
            self.view.set_text_player_score(str(self.model.get_player_score()))
            self.view.set_text_statusbar('Spieler gewinnt')
        else:
            self.model.set_computer_score(self.model.get_computer_score() + 1)
            self.view.set_text_computer_score(str(self.model.get_computer_score()))
            self.view.set_text_statusbar('Computer gewinnt')
        self.model.set_round(self.model.get_round() + 1)
        self.view.set_text_round(str(self.model.get_round()))

    def reset(self):
        self.model.set_round(1)
        self.model.set_player_score(0)
        self.model.set_computer_score(0)
        self.view.reset()


if __name__ == '__main__':
    app = QApplication([])
    c = Controller()
    c.view.show()
    sys.exit(app.exec())

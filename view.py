# View for the qt gui for the rock paper scissors game
# Authors: Jan Kammellander
# Date: 30.10.2022 Version: 1.0
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from PyQt6 import uic

from controller import Controller


class View(QMainWindow):
    move: QComboBox
    player_move: QLabel
    computer_move: QLabel

    def __init__(self, c: Controller):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.move.addItems(['rock', 'paper', 'scissors'])
        self.pB_execute.clicked.connect(c.execute)
        self.pB_reset.clicked.connect(c.reset)

    def reset(self) -> None:
        self.move.setCurrentIndex(0)
        self.round.setText('1')
        self.player_score.setText('0')
        self.computer_score.setText('0')
        self.player_move.setText('Spielzug des Players')
        self.computer_move.setText('Spielzug des Computers')
        self.set_text_statusbar('Sarte mit dem ersten Spielzug')

    def set_text_statusbar(self, text: str) -> None:
        self.statusbar.showMessage(text)

    def set_text_round(self, text: str) -> None:
        self.round.setText(text)

    def set_text_player_score(self, text: str) -> None:
        self.player_score.setText(text)

    def set_text_computer_score(self, text: str) -> None:
        self.computer_score.setText(text)

    def set_text_player_move(self, text: str) -> None:
        self.player_move.setText(text)

    def set_text_computer_move(self, text: str) -> None:
        self.computer_move.setText(text)

    def get_player_move(self) -> str:
        return self.move.currentText()

    def set_image_player_move(self, move: str) -> None:
        if move == 'rock':
            self.player_move.setPixmap(QPixmap('./images/rock.png'))
        elif move == 'paper':
            self.player_move.setPixmap(QPixmap('./images/paper.png'))
        else:
            self.player_move.setPixmap(QPixmap('./images/scissors.png'))

    def set_image_computer_move(self, move: str) -> None:
        if move == 'rock':
            self.computer_move.setPixmap(QPixmap('./images/rock.png'))
        elif move == 'paper':
            self.computer_move.setPixmap(QPixmap('./images/paper.png'))
        else:
            self.computer_move.setPixmap(QPixmap('./images/scissors.png'))

    def set_image_tie(self) -> None:
        self.player_move.setPixmap(QPixmap('./images/tie.png'))
        self.computer_move.setPixmap(QPixmap('./images/tie.png'))

    def reset_images(self) -> None:
        self.player_move.setPixmap(QPixmap(''))
        self.computer_move.setPixmap(QPixmap(''))

    def set_image(self, move_player: str, move_computer: str) -> None:
        self.reset_images()
        self.set_image_player_move(move_player)
        self.set_image_computer_move(move_computer)
        if move_player == move_computer:
            self.set_image_tie()
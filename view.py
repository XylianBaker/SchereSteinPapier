# View for the qt gui for the rock paper scissors game

from PyQt6.QtWidgets import *
from PyQt6 import uic

from controller import Controller


class View(QMainWindow):
    move: QComboBox

    def __init__(self, c: Controller):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
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

    def get_player_move(self) -> str:
        return self.move.currentText()

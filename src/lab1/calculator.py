"""
Calculator application using PyQt6 for basic arithmetic operations.

This module provides a graphical calculator with basic arithmetic functions,
including addition, subtraction, multiplication, division, and power operations.
"""

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton # pylint: disable=no-name-in-module


class Calculator(QMainWindow):
    """Main calculator class implementing the calculator UI and functionality."""
    def __init__(self):
        super().__init__()
        self.setFixedSize(367, 610)
        uic.loadUi("calculator.ui", self)
        base_style = """
        QPushButton {
            background-color: #2b2b2b;
            border-radius: 7px;
            font-size: 20px;
            color: white;
            border: none;
            min-width: 60px;
            min-height: 60px;
            margin: 2px;
        }
        QPushButton:hover {
            background-color: #1f1f1f;
        }
        QPushButton:pressed {
            background-color: #151515;
        }
        """
        self.main_value = self.findChild(QLabel, "label")
        self.main_value.setText("0")
        self.main_value.setStyleSheet(
            "background-color: #2b2b2b; border-radius: 0; font-size: 30px"
        )

        self.second_value = self.findChild(QLabel, "label_2")
        self.second_value.setStyleSheet(
            "background-color: #2b2b2b; border-radius: 0; font-size: 15px"
        )

        for button in self.findChildren(QPushButton):
            button.setStyleSheet(base_style)
            if button.text() in list(map(str, list(range(10)))):
                button.clicked.connect(
                    lambda _, x=button.text(): self.type_digit(x))
            elif button.text() == ".":
                button.clicked.connect(self.add_dot)
            elif button.text() == "+/-":
                button.clicked.connect(self.edit_value)
            elif button.text() == "=":
                button.clicked.connect(self.equally)
            elif button.text() == "CE":
                button.clicked.connect(self.clear)
            else:
                button.clicked.connect(
                    lambda _, x=button.text(): self.operation(x))

    def type_digit(self, value: str):
        """type new digit to display"""
        if self.main_value.text() == "0":
            self.main_value.setText(value)
        else:
            self.main_value.setText(self.main_value.text() + value)

    def add_dot(self):
        """append dot to display"""
        if "." not in self.main_value.text():
            self.main_value.setText(self.main_value.text() + ".")

    def edit_value(self):
        """to negative/positiv value"""
        value = -1 * float(self.main_value.text())
        if value == int(value):
            value = int(value)
        self.main_value.setText(str(value))

    def equally(self):
        """do math operation"""
        if self.second_value.text():
            if "^" in self.second_value.text():
                self.second_value.setText(
                    self.second_value.text().replace("^", "**"))
            self.main_value.setText(
                str(eval(self.second_value.text() + self.main_value.text())))
            self.second_value.setText("")

    def operation(self, operator: str):
        """add operation to display"""
        if not self.second_value.text():
            self.second_value.setText(self.main_value.text() + " " + operator)
            self.main_value.setText("0")

    def clear(self):
        """clear the display"""
        self.main_value.setText("0")
        self.second_value.setText("")


app = QApplication([])

window = Calculator()
window.show()
app.exec()

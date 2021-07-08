from .App import App
from .Calculator import Calculator
from .CLIInputParser import CLIInputParser
from .InputValidator import InputValidator


def factory():
    return App(
        CLIInputParser(),
        InputValidator(),
        Calculator(),
    )

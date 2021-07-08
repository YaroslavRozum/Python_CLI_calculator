from .App import App
from .Calculator import Calculator
from .CLIInputParser import CLIInputParser
from .InputTransformer import InputTransformer
from .InputValidator import InputValidator


def factory():
    return App(
        CLIInputParser(InputTransformer()),
        InputValidator(),
        Calculator(),
    )

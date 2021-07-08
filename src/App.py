from .types import Calculator, InputParser, InputValidator


class App():
    def __init__(
            self,
            input_parser: InputParser,
            input_validator: InputValidator,
            calculator: Calculator,
    ) -> None:
        self.input_parser = input_parser
        self.input_validator = input_validator
        self.calculator = calculator

    def __call__(self):
        parsed_input = self.input_parser.parse_input()
        valid_input = self.input_validator.validate_input(parsed_input)
        result = self.calculator.calculate(valid_input)
        return result

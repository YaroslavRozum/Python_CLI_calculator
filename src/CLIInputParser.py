import argparse
from typing import List

from .types import InputTransformer


class CLIInputParser():
    def __init__(self, input_transformer: InputTransformer):
        self.parser = argparse.ArgumentParser(
            'Making simple calculations',
            usage='python calc.py \'(2 + 4 + 1) * 4\'')
        self.parser.add_argument(
            'expression',
            type=str,
        )
        self.input_transformer = input_transformer

    def parse_input(self) -> List[str]:
        expression = self.parser.parse_known_args()[0].expression

        transformed_input_expression = self.input_transformer.transform_input(
            expression)

        return transformed_input_expression

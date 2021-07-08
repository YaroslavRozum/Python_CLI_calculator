import argparse
from typing import List

from .constants import close_bracket, open_bracket, operations, space


class CLIInputParser():
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            'Making simple calculations',
            usage='python calc.py \'(2 + 4 + 1) * 4\'')
        self.parser.add_argument(
            'expression',
            type=str,
        )
        self.current_number = ''

    def _check_and_add_to_input(self, transformed_input_expression: List[str]):
        if self.current_number == '':
            return
        transformed_input_expression += [self.current_number]
        self.current_number = ''

    def parse_input(self) -> List[str]:
        expression = self.parser.parse_known_args()[0].expression

        transformed_input_expression: List[str] = []
        for char in expression:
            if char == open_bracket:
                self._check_and_add_to_input(transformed_input_expression)
                transformed_input_expression += [char]
                continue
            if char == close_bracket:
                self._check_and_add_to_input(transformed_input_expression)
                transformed_input_expression += [char]
                continue

            if char in operations:
                self._check_and_add_to_input(transformed_input_expression)
                transformed_input_expression += [char]
                continue

            if char == space:
                self._check_and_add_to_input(transformed_input_expression)
                continue

            self.current_number += char

        self._check_and_add_to_input(transformed_input_expression)

        return transformed_input_expression

from typing import List

from .constants import (close_bracket, empty, open_bracket, operations, space,
                        sub_op, sum_op)


class InputTransformer():
    def __init__(self) -> None:
        self.current_number = empty
        self.non_numeric_chars = set([open_bracket] + [close_bracket] +
                                     [space] + list(operations), )

    def _check_and_add_to_input(self, transformed_input_expression: List[str]):
        if self.current_number == empty or self.current_number == sub_op:
            return
        transformed_input_expression += [self.current_number]
        self.current_number = empty

    def _register_non_number_char(self,
                                  transformed_input_expression: List[str],
                                  char: str):
        if char == space:
            return
        if char == sub_op:
            char = sum_op
            self.current_number = '-'
        transformed_input_expression += [char]

    def transform_input(self, expression: str) -> List[str]:
        transformed_input_expression: List[str] = []
        for char in expression:
            if char in self.non_numeric_chars:
                self._check_and_add_to_input(transformed_input_expression)
                self._register_non_number_char(transformed_input_expression,
                                               char)
                continue

            self.current_number += char

        self._check_and_add_to_input(transformed_input_expression)
        return transformed_input_expression

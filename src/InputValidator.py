from typing import List

from .constants import (close_bracket, dot, empty, open_bracket, operations,
                        sub_op)


class InputValidator():
    @staticmethod
    def _is_valid_number(str_number: str) -> bool:
        if len(str_number) == 0:
            return False
        splitted_str_number = str_number.split(dot)
        if len(splitted_str_number) > 2:
            return False
        return all([
            string.replace(sub_op, empty).isdigit()
            for string in splitted_str_number
        ])

    def validate_input(self, input_expression: List[str]) -> List[str]:
        balance = 0

        for position, expression_part in enumerate(input_expression):
            start_position = position == 0
            if start_position and (expression_part in operations
                                   or expression_part == close_bracket):
                raise ValueError('Wrong Input')
            last_position = position + 1 == len(input_expression)
            if last_position and (expression_part in operations
                                  or expression_part == open_bracket):
                raise ValueError('Wrong Input')
            if expression_part in operations \
                    and input_expression[position + 1] in operations:
                raise ValueError('Wrong Input')
            if expression_part == open_bracket \
                    and \
                    (input_expression[position + 1] == close_bracket
                        or input_expression[position + 1] in operations):
                raise ValueError('Wrong Input')
            if expression_part == close_bracket and not last_position \
                and (input_expression[
                    position + 1] not in operations
                        and input_expression[position + 1] != close_bracket):
                raise ValueError('Wrong Input')
            not_last_position = position < len(input_expression) - 1
            if not_last_position and expression_part[-1].isdigit(
            ) and input_expression[position + 1][-1].isdigit():
                raise ValueError('Wrong Input')
            if expression_part == open_bracket:
                balance += 1
                continue
            if expression_part == close_bracket:
                balance -= 1
                continue
            if expression_part not in operations \
                and not self._is_valid_number(
                    expression_part):
                raise ValueError('Wrong Input')

        if balance != 0:
            raise ValueError('Wrong Input')

        return input_expression

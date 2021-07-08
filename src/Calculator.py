from typing import Iterator, List, Union

from . import helpers
from .constants import close_bracket, div_op, mul_op, open_bracket, sum_op


class Calculator():
    def __init__(self) -> None:
        self.op_to_fn = {
            sum_op: self._sum,
            div_op: self._div,
            mul_op: self._mul,
        }

    @staticmethod
    @helpers.str_parameters_to_number
    def _mul(num1: Union[int, float],
             num2: Union[int, float]) -> Union[int, float]:
        return num1 * num2

    @staticmethod
    @helpers.str_parameters_to_number
    def _div(num1: Union[int, float],
             num2: Union[int, float]) -> Union[int, float]:
        return num1 / num2

    @staticmethod
    @helpers.str_parameters_to_number
    def _sum(num1: Union[int, float],
             num2: Union[int, float]) -> Union[int, float]:
        return num1 + num2

    def _get_next_value(self, iterator: Iterator[str], position_dict) -> str:
        value = next(iterator)
        position_dict['parameter_position'] += 1
        if value != open_bracket:
            return value
        balance = 1
        sub_expression = []
        while balance != 0:
            value = next(iterator)
            position_dict['parameter_position'] += 1
            if value == open_bracket:
                balance += 1
            if value == close_bracket:
                balance -= 1
            if balance != 0:
                sub_expression += [value]
        return str(self.calculate(sub_expression))

    def calculate(self, expression: List[str]) -> Union[int, float]:
        if len(expression) == 1:
            return helpers.strings_to_numbers(expression)[0]

        if len(expression) == 3:
            if expression[0] == open_bracket:
                return expression[1]
            operation = expression[1]
            return self.op_to_fn[operation](expression[0], expression[-1])

        iterator = iter(expression)
        position_dict = dict(parameter_position=0)

        while True:
            current_value = self._get_next_value(iterator, position_dict)
            if position_dict['parameter_position'] == len(expression):
                return current_value
            operation = self._get_next_value(iterator, position_dict)
            if operation == sum_op:
                return self.op_to_fn[operation](
                    current_value,
                    str(
                        self.calculate(
                            expression[position_dict['parameter_position']:])))
            if operation == mul_op or operation == div_op:
                operation_result = self.op_to_fn[operation](
                    current_value,
                    self._get_next_value(iterator, position_dict))
                expression = [
                    str(operation_result)
                ] + expression[position_dict['parameter_position']:]
                iterator = iter(expression)
                position_dict['parameter_position'] = 0
                if len(expression) == 1:
                    return helpers.strings_to_numbers(expression)[0]

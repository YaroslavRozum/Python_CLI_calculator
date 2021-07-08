import abc
from typing import List, Union


class Calculator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'calculate')
                 and callable(subclass.calculate)) or NotImplemented)

    @abc.abstractmethod
    def calculate(self, expression: List[str]) -> Union[int, float]:
        raise NotImplementedError


class InputValidator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'validate_input')
                 and callable(subclass.validate_input)) or NotImplemented)

    @abc.abstractmethod
    def validate_input(self, input_expression: List[str]) -> List[str]:
        raise NotImplementedError


class InputParser(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'parse_input')
                 and callable(subclass.parse_input)) or NotImplemented)

    @abc.abstractmethod
    def parse_input(self) -> List[str]:
        raise NotImplementedError


class InputTransformer(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return ((hasattr(subclass, 'transform_input')
                 and callable(subclass.transform_input)) or NotImplemented)

    @abc.abstractmethod
    def transform_input(self, expression: str) -> List[str]:
        raise NotImplementedError

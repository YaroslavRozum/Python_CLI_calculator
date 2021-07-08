from typing import List, Union


def is_arr_of_ints(str_num_array: List[str]) -> bool:
    for str_num in str_num_array:
        try:
            int(str_num)
        except Exception:
            return False

    return True


def strings_to_numbers(strings: List[str]) -> List[Union[float, int]]:
    if is_arr_of_ints(strings):
        return [int(string) for string in strings]
    return [float(string) for string in strings]


def str_parameters_to_number(fn):
    def decorator(str1: str, str2: str) -> Union[float, int]:
        num1, num2 = strings_to_numbers([str1, str2])
        return fn(num1, num2)

    return decorator

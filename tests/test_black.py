from functools import reduce
import math

numbers = [
    1, 2,
    3, 4, 5, 6]

example_dict = { "numbers": numbers,
    "numberSum": reduce(
        lambda a, b: a + b, 
        numbers),
    "sin": [
        math.sin(x) for x in numbers
    ],
}


def simple_sum(x,       y):
    return x + y


def get_trigonometry(angle):
    sin = math.sin(angle)
    cos = math.cos(angle)
    tan = math.tan(angle)
    return (sin, cos, tan)


def long_static_function(
    parameter1, parameter2, parameter3, parameter4, parameter5, parameter6
):
    result_string = (
        "Esta frase vemos que supera con creces el límite de los 80 caracteres!!"
    )
    return result_string

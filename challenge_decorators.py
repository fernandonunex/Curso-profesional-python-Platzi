from __future__ import division
from ast import arguments


def custom_operation(type_of_operation):

    def operation_structure(func):

        def wrapper(*args, **kwargs):
            print(f"\nThis operation is a {type_of_operation}")
            result = func(*args, **kwargs)
            print("Argumentos: -> ", end="")
            print(*args)
            print(f"The result is: {result}")
            print("--"*20)

        return wrapper
    return operation_structure


@custom_operation("Multiplication")
def mult(a, b, c):
    return a*b*c


@custom_operation("Sum")
def sum(a, b):
    return a+b

@custom_operation("Division")
def division(a,b):
    return a/b


def run():
    sum(10, 20)

    mult(5, 3, 2)

    mult(3, 3, 3)

    division(10,5)


if __name__ == "__main__":
    run()

from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Took: " + str(time_elapsed.total_seconds()) + " seconds")

    return wrapper


@execution_time
def random_func():
    for _ in range(1, 100):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return print(a + b)


@execution_time
def saludo(name="Pablo"):
    print("Hola" + name)


random_func()
sum(10, 10)
saludo()

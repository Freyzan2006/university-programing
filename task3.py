def decoration(a, b):
    def wrapper(f):
        def wrapper2(x, y):
            print(f"аргументы декоратора: a = {a}; b = {b}")
            print(f"аргументы функции которая под декоратором: x = {x}; y = {y}")
            result_d = f(a, b)
            result_f = f(x, y)
            print(f"результат функции с аргументами декоратора {result_d}")
            print(f"результат функции с аргументами самой функции {result_f}")
            return ( result_d, result_f )
        return wrapper2
    return wrapper

@decoration(5, 5)
def add(x, y) -> int:
    return x + y


def show_result() -> None:
    print(add(5, 10))
    pass 


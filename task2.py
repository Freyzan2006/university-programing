def fibonacci_number(end: int = 5) -> None:
    a, b = 0, 1
    for i in range(end):
        yield a + b
        a, b = b, a + b

def show_result() -> None:
    print("-----------task 2------------")
    for num in fibonacci_number(6):
        print(num)
    print("---------------")


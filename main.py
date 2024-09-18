from typing import List

def quadratic_formula(a: int, b: int, c: int) -> List[float]:
    
    d = b**2 - 4 * a * c 
    
    if d == 0:
        print("Один квадратный корень")
    elif d < 0:
        print("Нету действительных корней")
        return []
    else:
        print("Есть два корня")
    
    x1 = ((-1 * b) + (d**0.5)) / 2 * a 
    x2 = ((-1 * b) - (d**0.5)) / 2 * a 
    
    return [x1, x2]

def main():
    a = 1
    b = -3
    c = 2
    
    result: List[float] = quadratic_formula(a = a, b = b, c = c)
    print(f"Входные данные: a = {a}; b = {b}; c = {c}")
    print(f"результат: {result}")


if __name__ == "__main__":
    main()
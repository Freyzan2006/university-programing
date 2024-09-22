from typing import List

def quadratic_formula(a: float, b: float, c: float) -> List[float]:
    
    D = b**2 - 4 * a * c 
    if D<0:
        raise Exception("Нет действительных корней")
    elif a==0 and b==0 and c==0:
        raise Exception("не a, b, c = 0")
    elif D == 0:
        print("Один квадратный корень")
        x = -b / (2 * a) 
        return [x]
    else:
        x1 = ((-1 * D) + (D**0.5)) / 2 * a 
        x2 = ((-1 * D) - (D**0.5)) / 2 * a 
        return [x1, x2]

# 1, -5, 6 - два
# 1, 4, 4 - один

def main():
    while True:
        print("--------------------------")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
    
        try:
            result: List[float] = quadratic_formula(a, b, c)
            print(f"Входные данные: a = {a}; b = {b}; c = {c}")
            print(f"Результат: {result}")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
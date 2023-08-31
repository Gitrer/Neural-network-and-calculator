import sys

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Invalid expression"

# Получаем введенное выражение из аргумента командной строки
expression = sys.argv[1]

# Вычисляем результат и выводим его
result = calculate(expression)
print(result)
print(expression)

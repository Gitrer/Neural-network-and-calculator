import sys

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception:
        return "Invalid expression"

# Получаем введенное выражение из аргумента командной строки
raw_expression = sys.argv[1]

# Удаляем пробелы и другие символы справа и слева от выражения
expression = raw_expression.strip()

# Вычисляем результат и выводим его
result = calculate(expression)
print(result)

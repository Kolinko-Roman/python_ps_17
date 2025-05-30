from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats
from datetime import datetime

# Завдання 1: календар
calendar = UkrainianCalendar()
print("Свята України:", calendar.get_holiday_list())
date_input = input("Введіть дату (рррр-мм-дд): ")
date = datetime.strptime(date_input, "%Y-%m-%d")
print("Це робочий день?" , calendar.is_working_day(date))

# Завдання 2: калькулятор
calc = Calculator()
print("\nОберіть операцію: 1 - додавання, 2 - віднімання, 3 - множення, 4 - ділення")
choice = input("Ваш вибір: ")
a = float(input("Перше число: "))
b = float(input("Друге число: "))

if choice == "1":
    print("Результат:", calc.add(a, b))
elif choice == "2":
    print("Результат:", calc.subtract(a, b))
elif choice == "3":
    print("Результат:", calc.multiply(a, b))
elif choice == "4":
    print("Результат:", calc.divide(a, b))
else:
    print("Невірна операція")

# Завдання 3: аналіз тексту
text = input("\nВведіть текст для аналізу: ")
analyzer = TextStats(text)
print("Кількість слів:", analyzer.count_words())
common_letter = analyzer.most_common_letter()
if common_letter:
    print("Найпоширеніша літера:", common_letter[0], "—", common_letter[1], "раз(ів)")
else:
    print("Немає букв для аналізу.")

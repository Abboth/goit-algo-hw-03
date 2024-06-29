#task № 1 in first homework

from datetime import datetime, timedelta
import re


print("Добро пожаловать в программу по обчислению промежутков дней между датами")
user_date = input("Введите дату с которой будем сравнивать текущий день(формат ввода YYYY-MM-DD): ")

def get_days_from_today(str_date:str)->int: #находим промежуток дней между строкой заданой пользователем и текущим днем

    try:
        pattern = r"^\d{4}+\d{2}+\d{2}"
        if re.match(pattern, str_date):
            object_date = datetime.strptime(str_date, '%Y-%m-%d').date()
        else:
            str_date = re.sub(r"[\D]", "-",str_date)
            object_date = datetime.strptime(str_date, '%Y-%m-%d').date()
        today = datetime.now().date()
        return (today - object_date).days
    except ValueError:
        print(f"что то не так, убедитесь что дата :{user_date} введена привильно")

print(get_days_from_today(user_date))
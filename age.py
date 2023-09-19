from datetime import date

def calculate_age(birth_date):
    current_date = date.today()
    age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
    return age

print(calculate_age(date(2001, 2, 23)), "years")
      
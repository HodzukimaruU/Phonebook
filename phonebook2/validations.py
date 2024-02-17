from errors import IncorrectUserInputError
import re


# Валидация выбора пользователя
def validate_user_choice(user_choice: str) -> None:
    if not user_choice.isdigit():
        raise IncorrectUserInputError("Choice must be digit.")
    if user_choice not in map(str, range(1, 8)):
        raise IncorrectUserInputError("Choice must be from 1 to 7.")

# Валидация числа для генерации случайных данных
def validate_generation_number(number_of_lines: str) -> None:
    if not number_of_lines.isdigit():
        raise IncorrectUserInputError('A generation number must be a digit.')
    if int(number_of_lines) < 0 or int(number_of_lines) > 1000:
        raise IncorrectUserInputError('A generation number should be from 0 to 1000.') 

# Валидация названия организации
def validate_organization(organization: str) -> None:
    if not organization[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(organization) < 3 or len(organization) > 50:
        raise IncorrectUserInputError('The length of company name should be from 3 to 50.')
    for letter in organization:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация фамилии
def validate_last_name(last_name: str) -> None:
    if not last_name[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(last_name) < 2 or len(last_name) > 50:
        raise IncorrectUserInputError('The letters length should be from 2 to 50.')
    for letter in last_name:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')  

# Валидация имени
def validate_first_name(first_name: str) -> None:
    if not first_name[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(first_name) < 2 or len(first_name) > 50:
        raise IncorrectUserInputError('The letters length should be from 2 to 50.')
    for letter in first_name:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация отчества
def validate_middle_name(middle_name: str) -> None:
    if not middle_name[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(middle_name) < 2 or len(middle_name) > 50:
        raise IncorrectUserInputError('The letters length should be from 2 to 50.')
    for letter in middle_name:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация персонального номера телефона
def validate_personal_number(personal_phone: str) -> None:
    if not re.match(r'^\+\d{10,13}$', personal_phone):
        raise IncorrectUserInputError("The personal number must start with a plus and contain numbers and be between 10 and 12 characters long")

# Валидация рабочего номера телефона
def validate_work_number(work_phone: str) -> None:    
    if not re.match(r'^\d{6,13}$', work_phone):
        raise IncorrectUserInputError("The work number contain only numbers nd be between 6 and 12 characters long")

# Валидация названия организации при редактировании
def validate_organization_edit(organization: str) -> None:
    if organization.strip() == '':
        return  # Пропускаем валидацию, если введена пустая строка
    if not organization[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(organization) < 2 or len(organization) > 50:
        raise IncorrectUserInputError('The length of company name should be from 3 to 50.')
    for letter in organization:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация фамилии при редактировании
def validate_last_name_edit(last_name: str) -> None:
    if last_name.strip() == '':
        return  # Пропускаем валидацию, если введена пустая строка
    if not last_name[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(last_name) < 2 or len(last_name) > 50:
        raise IncorrectUserInputError('The letters length should be from 2 to 50.')
    for letter in last_name:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация имени при редактировании
def validate_first_name_edit(first_name: str) -> None:
    if first_name.strip() == '':
        return  # Пропускаем валидацию, если введена пустая строка
    if not first_name[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(first_name) < 2 or len(first_name) > 50:
        raise IncorrectUserInputError('The letters length should be from 2 to 50.')
    for letter in first_name:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация отчества при редактировании
def validate_middle_name_edit(middle_name: str) -> None:
    if middle_name.strip() == '':
        return  # Пропускаем валидацию, если введена пустая строка
    if not middle_name[0].isupper():
        raise IncorrectUserInputError('The input must contain letters and the first letter must be in uppercase.')
    if len(middle_name) < 2 or len(middle_name) > 50:
        raise IncorrectUserInputError('The letters length should be from 2 to 50.')
    for letter in middle_name:
        if not letter.isalpha():
            raise IncorrectUserInputError('The characters should be letters')

# Валидация персонального номера телефона при редактировании
def validate_personal_number_edit(personal_phone: str) -> None:
    if personal_phone.strip() == '':
        return  # Пропускаем валидацию, если введена пустая строка
    if not re.match(r'^\+\d{10,13}$', personal_phone):
        raise IncorrectUserInputError("The personal number must start with a plus and contain numbers and be between 10 and 12 characters long")
    
# Валидация рабочего номера телефона при редактировании
def validate_work_number_edit(work_phone: str) -> None:    
    if work_phone.strip() == '':
        return  # Пропускаем валидацию, если введена пустая строка
    if not re.match(r'^\d{6,13}$', work_phone):
        raise IncorrectUserInputError("The work number contain only numbers nd be between 6 and 12 characters long")

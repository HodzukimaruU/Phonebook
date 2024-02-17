from typing import List, Dict
from data_access_layer import (
    record_new_data_line,
    record_new_information,
    get_all_records
    )
from faker import Faker

# Получение страницы записей из файла phonebook.csv
def get_entries_page(page_number: int, records_per_page: int) -> List[Dict[str, str]]:
    data = get_all_records()
    start_index = (page_number - 1) * records_per_page
    end_index = start_index + records_per_page
    return data[start_index:end_index]

# Добавление новой записи
def add_new_entry(id: str, last_name: str, first_name: str, middle_name: str, organization: str, work_phone: str, personal_phone: str) -> bool:

    new_line = {"ID": id,
                "Last_Name": last_name,
                "First_Name": first_name,
                "Middle_Name": middle_name,
                "Organization": organization,
                "Work_phone": work_phone,
                "Personal_phone": personal_phone
                }
    
    record_new_data_line(new_line)
    return True

# Редактирование существующей записи
def edit_entry(id: str, last_name: str, first_name: str, middle_name: str, organization: str, work_phone: str, personal_phone: str) -> bool:
    data = get_all_records()
    updated_data = []
    for row in data:
        if id == row.get("ID"):
            row["Last_Name"] = last_name if last_name else row["Last_Name"]
            row["First_Name"] = first_name if first_name else row["First_Name"]
            row["Middle_Name"] = middle_name if middle_name else row["Middle_Name"]
            row["Organization"] = organization if organization else row["Organization"]
            row["Work_phone"] = work_phone if work_phone else row["Work_phone"]
            row["Personal_phone"] = personal_phone if personal_phone else row["Personal_phone"]
        updated_data.append(row)
    record_new_information(updated_data)
    return True

# Поиск записей по организации
def search_entries_by_organization(organization: str) -> List[Dict[str, str]]:
    data = get_all_records()
    result = []
    for row in data:
        if organization.lower() in row.get("Organization").lower():
            result.append({
                "Last_Name": row.get("Last_Name"),
                "First_Name": row.get("First_Name"),
                "Middle_Name": row.get("Middle_Name"),
                "Organization": row.get("Organization"),
                "Work_phone": row.get("Work_phone"),
                "Personal_phone": row.get("Personal_phone")
            })
    return result

# Поиск записей по фамилии
def search_entries_by_name(last_name: str) -> List[Dict[str, str]]:
    data = get_all_records()
    result = []
    for row in data:
        if last_name.lower() in row.get("Last_Name").lower():
            result.append({
                "Last_Name": row.get("Last_Name"),
                "First_Name": row.get("First_Name"),
                "Middle_Name": row.get("Middle_Name"),
                "Organization": row.get("Organization"),
                "Work_phone": row.get("Work_phone"),
                "Personal_phone": row.get("Personal_phone")
            })
    return result

# Генерация случайных данных
def random_data(number_of_lines: int) -> bool:
    new_data = []
    fake = Faker()
    number_of_lines = int(number_of_lines)
    for _ in range(number_of_lines):
        new_data.append({"ID": fake.uuid4(),
                         "Last_Name": fake.last_name(),
                         "First_Name": fake.first_name(),
                         "Middle_Name": fake.first_name(),
                         "Organization": fake.company(),
                         "Work_phone": fake.phone_number(),
                         "Personal_phone": fake.phone_number()})
    record_new_information(new_data)
    return True

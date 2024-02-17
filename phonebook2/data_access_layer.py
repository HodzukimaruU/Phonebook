from typing import List, Dict
import csv


# Получение всех записей из файла phonebook.csv
def get_all_records() -> List[Dict[str, str]]:
    with open('phonebook.csv', encoding='utf8') as sp_file:
        return list(csv.DictReader(sp_file))

# Получение заголовков ключей из файла phonebook.csv
def key_headers() -> List[str]:
    with open('phonebook.csv', encoding='utf8') as file:
        return csv.DictReader(file).fieldnames

# Запись новой строки данных в файл phonebook.csv
def record_new_data_line(new_data_line: Dict[str, str]) -> None:
    header = key_headers()
    with open('phonebook.csv', 'a', encoding='utf8', newline='') as new_file:
        writer = csv.DictWriter(new_file, fieldnames=header)
        writer.writerow(new_data_line)

# Запись новой информации в файл phonebook.csv
def record_new_information(new_information: List[Dict[str, str]]) -> None:
    header = key_headers()
    with open('phonebook.csv', 'w', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(new_information)

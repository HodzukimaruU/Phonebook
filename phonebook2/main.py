# Модуль main.py - точка входа в приложение и пользовательский интерфейс. Запуск с помощью -> python3 main.py.

from business_logic import (
    add_new_entry,
    random_data,
    search_entries_by_name,
    search_entries_by_organization,
    edit_entry,
    get_entries_page
    )

from validations import (
    validate_user_choice,
    validate_generation_number,
    validate_last_name,
    validate_first_name,
    validate_middle_name,
    validate_organization,
    validate_work_number,
    validate_personal_number,
    validate_last_name_edit,
    validate_first_name_edit,
    validate_middle_name_edit,
    validate_organization_edit,
    validate_personal_number_edit,
    validate_work_number_edit
)

from data_access_layer import get_all_records
from errors import IncorrectUserInputError
from faker import Faker


fake=Faker()

while True:
    choice = input("1 - Display Entries\n"
                   "2 - Add Entry\n"
                   "3 - Edit Entry\n"
                   "4 - Search Entries by Organization \n"
                   "5 - Search Entries by Last Name\n"
                   "6 - Random Data\n"
                   "7 - Exit\nYour choice: ")
    
    try:
        validate_user_choice(user_choice=choice)
    except IncorrectUserInputError as err:
        print(err)
        continue
    
    if choice == '1':
        page_number = int(input("Enter page number: "))
        entries_per_page = 5  # Количество записей на одной странице
        entries = get_entries_page(page_number, entries_per_page)
        for entry in entries:
            print(entry)

    elif choice == '2':
        id = fake.uuid4()
        last_name = input("Enter last name: ")
        try:
            validate_last_name(last_name=last_name)
        except IncorrectUserInputError as err:
            print(err)
            continue
        first_name = input("Enter first name: ")
        try:
            validate_first_name(first_name=first_name)
        except IncorrectUserInputError as err:
            print(err)
            continue
        middle_name = input("Enter middle name: ")
        try:
            validate_middle_name(middle_name=middle_name)
        except IncorrectUserInputError as err:
            print(err)
            continue
        organization = input("Enter organization: ")
        try:
            validate_organization(organization=organization)
        except IncorrectUserInputError as err:
            print(err)
            continue
        work_phone = input("Enter work_phone: ")
        try:
            validate_work_number(work_phone=work_phone)
        except IncorrectUserInputError as err:
            print(err)
            continue
        personal_phone = input("Enter personal phone: ")
        try:
            validate_personal_number(personal_phone=personal_phone)
        except IncorrectUserInputError as err:
            print(err)
            continue
        
        if add_new_entry(id=id,
                         last_name=last_name,
                         first_name=first_name,
                         middle_name=middle_name,
                         organization=organization,
                         work_phone=work_phone,
                         personal_phone=personal_phone):
            print('The new company has added')

    elif choice == '3':
        id = input("Enter ID of the entry to edit: ")

        # Получение существующей записи по ID
        existing_entry = None
        for entry in get_all_records():
            if entry.get("ID") == id:
                existing_entry = entry
                break

        if existing_entry:
            print("Leave fields blank to keep the existing values.")
            try:
                new_last_name = input(f"Enter new last name [{existing_entry['Last_Name']} or press Enter to skip]: ")
                if new_last_name.strip() != '':
                    validate_last_name_edit(last_name=new_last_name)
            except IncorrectUserInputError as err:
                print(err)
                continue
            
            try:
                new_first_name = input(f"Enter new first name [{existing_entry['First_Name']} or press Enter to skip]: ")
                if new_first_name.strip() != '':
                    validate_first_name_edit(first_name=new_first_name)
            except IncorrectUserInputError as err:
                print(err)
                continue

            try:
                new_middle_name = input(f"Enter new middle name [{existing_entry['Middle_Name']} or press Enter to skip]: ")
                if new_middle_name.strip() != '':
                    validate_middle_name_edit(middle_name=new_middle_name)
            except IncorrectUserInputError as err:
                print(err)
                continue

            try:
                new_organization = input(f"Enter new organization [{existing_entry['Organization']} or press Enter to skip]: ")
                if new_organization.strip() != '':
                    validate_organization_edit(organization=new_organization)
            except IncorrectUserInputError as err:
                print(err)
                continue

            try:
                new_work_phone = input(f"Enter new work phone [{existing_entry['Work_phone']} or press Enter to skip]: ")
                if new_work_phone.strip() != '':
                    validate_work_number_edit(work_phone=new_work_phone)
            except IncorrectUserInputError as err:
                print(err)
                continue

            try:
                new_personal_phone = input(f"Enter new personal phone [{existing_entry['Personal_phone']} or press Enter to skip]: ")
                if new_personal_phone.strip() != '':
                    validate_personal_number_edit(personal_phone=new_personal_phone)
            except IncorrectUserInputError as err:
                print(err)
                continue

            if edit_entry(id=id,
                        last_name=new_last_name,
                        first_name=new_first_name,
                        middle_name=new_middle_name,
                        organization=new_organization,
                        work_phone=new_work_phone,
                        personal_phone=new_personal_phone):
                print('The entry has been successfully edited.')
        else:
            print("Entry not found.")


    elif choice == '4':
        organization = input("Enter organization to search for entry: ")
        res = search_entries_by_organization(organization=organization)
        print(res)

    elif choice == '5':
        last_name = input("Enter last name to search for entry: ")
        res = search_entries_by_name(last_name=last_name)
        print(res)

    elif choice == '6':
        number_of_lines = (input('Enter a number of records for generation: '))
        try:
            validate_generation_number(number_of_lines=number_of_lines)
        except IncorrectUserInputError as err:
            print(err)
            continue
        random_data(number_of_lines=number_of_lines)
        print('A new random data has generated.')

    elif choice == '7':
        print("Good luck!")
        break

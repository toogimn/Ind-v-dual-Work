import json
import os
import time

gradebook = []


def welcome_screen():
    ascii_art = r"""
   ____                 _       _                 __  __                                    
  / ___| ___   ___   __| | __ _| |_ ___  _ __    |  \/  | __ _ _ __   __ _  __ _  ___ _ __  
 | |  _ / _ \ / _ \ / _` |/ _` | __/ _ \| '__|   | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__| 
 | |_| | (_) | (_) | (_| | (_| | || (_) | |      | |  | | (_| | | | | (_| | (_| |  __/ |    
  \____|\___/ \___/ \__,_|\__,_|\__\___/|_|      |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|    
                                                                           |___/           
    """
    print(ascii_art)
    time.sleep(2)


def main_menu():
    print("""
========= Grade Book Menu =========
1. Add New Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Summary Statistics
7. Save to File
8. Load from File
9. Recursive Count
10. Help / Instructions
11. Clear All Data
0. Exit
===================================
""")


def add_record():
    name = input("Enter student name: ")
    grades = []
    while True:
        grade = input("Enter grade (or 'q' to quit): ")
        if grade.lower() == 'q':
            break
        try:
            grades.append(float(grade))
        except ValueError:
            print("Invalid grade. Please enter a number.")
    record = {"name": name, "grades": grades}
    gradebook.append(record)
    print("Record added.\n")


def view_records():
    if not gradebook:
        print("No records available.\n")
        return
    for i, student in enumerate(gradebook, 1):
        print(f"{i}. {student['name']} - Grades: {student['grades']}")
    print()


def search_record():
    name = input("Enter name to search: ")
    found = False
    for student in gradebook:
        if student['name'].lower() == name.lower():
            print(f"Found: {student['name']} - {student['grades']}")
            found = True
    if not found:
        print("Student not found.\n")


def update_record():
    name = input("Enter student name to update: ")
    for student in gradebook:
        if student['name'].lower() == name.lower():
            print(f"Current grades: {student['grades']}")
            new_grades = []
            while True:
                grade = input("Enter new grade (or 'q' to quit): ")
                if grade.lower() == 'q':
                    break
                try:
                    new_grades.append(float(grade))
                except ValueError:
                    print("Invalid grade.")
            student['grades'] = new_grades
            print("Grades updated.\n")
            return
    print("Student not found.\n")


def delete_record():
    name = input("Enter student name to delete: ")
    for i, student in enumerate(gradebook):
        if student['name'].lower() == name.lower():
            gradebook.pop(i)
            print("Student deleted.\n")
            return
    print("Student not found.\n")


def summary_stats():
    if not gradebook:
        print("No records to calculate.\n")
        return
    for student in gradebook:
        if student['grades']:
            avg = sum(student['grades']) / len(student['grades'])
            print(f"{student['name']} - Avg: {avg:.2f}")
        else:
            print(f"{student['name']} has no grades.")
    print()


def save_to_file():
    with open("gradebook.json", "w") as f:
        json.dump(gradebook, f)
    print("Data saved to gradebook.json\n")


def load_from_file():
    global gradebook
    try:
        with open("gradebook.json", "r") as f:
            gradebook = json.load(f)
        print("Data loaded.\n")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading file.\n")


def recursive_count(index=0):
    if index >= len(gradebook):
        return 0
    return 1 + recursive_count(index + 1)


def help_menu():
    print("""
Instructions:
- Add students and their grades
- View, search, update or delete student records
- Save/load data using files
- Use 'Summary Statistics' for average grades
""")


def clear_all_data():
    confirm = input("Are you sure to clear all data? (yes/no): ")
    if confirm.lower() == "yes":
        gradebook.clear()
        print("All data cleared.\n")
    else:
        print("Cancelled.\n")


def main():
    welcome_screen()
    while True:
        main_menu()
        try:
            choice = input("Enter your choice: ")
            match choice:
                case "1": add_record()
                case "2": view_records()
                case "3": search_record()
                case "4": update_record()
                case "5": delete_record()
                case "6": summary_stats()
                case "7": save_to_file()
                case "8": load_from_file()
                case "9": print(f"Total records: {recursive_count()}\n")
                case "10": help_menu()
                case "11": clear_all_data()
                case "0":
                    print("Goodbye!")
                    break
                case _: print("Invalid option.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()

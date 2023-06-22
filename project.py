from student import Student
from interface import mini_interface, interface, print_list
from getch import pause
from shirtificate import PDF
import re
import os
import csv
import random


def main():
    students = []
    while True:
        interface()
        choice = input("Your choice: ")
        os.system("clear")
        match choice:
            case "1":
                student = Student.get()
                students.append(student)
            case "2":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    update_information(students)
            case "3":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    students.sort(key=lambda s: s.gpa, reverse=True)
                    print("Sorting successfully!")
            case "4":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    print_list(students)
            case "5":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    print(
                        "Enter ID of student you want to check if the student exists in the list"
                    )
                    id = id_validate()
                    if does_exist(students, id):
                        print("Student exists in the list.")
                    else:
                        print("Student doesn't exist in the list.")
            case "6":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    print("Enter ID of student you want to remove from the list")
                    id = id_validate()
                    remove_student(students, id)
            case "7":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    write_csv(students)
                    print("Writing data to file successfully!")
            case "8":
                students = read_csv()
                if len(students) == 0:
                    print("CSV file is empty.")
                else:
                    print("Reading data from file successfully!")
            case "9":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    id = id_validate()
                    if append_csv(students, id):
                        print("Adding successfully!")
                    else:
                        print("Student already exists in the CSV file.")
            case "10":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    if print_tshirt(students) == True:
                        print("Printed successfully!")
                    else:
                        print("There is no student who has GPA higher than 3.6")

            case "11":
                if is_empty(students):
                    print("The current list is empty.")
                else:
                    result = pick_random(students)
                    for student in students:
                        if student.id == result:
                            print(f"The luckiest person is {student.name} !!!")
                            break
            case _:
                print("Exiting!")
                os.system("clear")
                break
        pause("Press any key to continue.")
        os.system("clear")


def is_empty(students):
    if len(students) == 0:
        return True
    return False


def id_validate():
    while True:
        try:
            id = int(input("ID: ").strip())
            return id
        except ValueError:
            print("Invalid ID.")


def name_validate():
    while True:
        try:
            name = input("Name: ").strip().title()
            re.sub(" +", " ", name)
            if not name.replace(" ", "").isalpha():
                raise ValueError
            return name
        except ValueError:
            print("Invalid name.")


def major_validate():
    while True:
        try:
            major = input("Major: ").strip().upper()
            majors = ["CS", "IT", "DS", "BL", "BA", "DA", "LAW", "ART"]
            if major not in majors:
                raise ValueError
            return major
        except ValueError:
            print("Invalid major.")


def gpa_validate():
    while True:
        try:
            gpa = float(input("GPA: ").strip())
            if gpa > 4:
                raise ValueError
            return gpa
        except ValueError:
            print("Invalid GPA. Please enter again!")


def get_id_list(students):
    return [student.id for student in students]


def does_exist(students, id):
    id_list = get_id_list(students)
    if id in id_list:
        return True
    return False


def update_information(students):
    print("Enter ID of student you want to update")
    id = id_validate()
    for student in students:
        if student.id == id:
            while True:
                mini_interface()
                choice = input("Your choice: ")
                match choice:
                    case "1":
                        new_id = id_validate()
                        if does_exist(students, new_id):
                            print(
                                "This ID already exists in the list\nUpdating unsuccessfully."
                            )
                        else:
                            student.id = new_id
                            print("Updated successfully!")
                    case "2":
                        new_name = name_validate()
                        student.name = new_name
                        print("Updated successfully!")
                    case "3":
                        new_major = major_validate()
                        student.major = new_major
                        print("Updated successfully!")
                    case "4":
                        new_gpa = gpa_validate()
                        student.gpa = new_gpa
                        print("Updated successfully!")
                    case _:
                        print("Stop updating.")
                        return
                pause("Press any key to continue.")
                os.system("clear")
    print("Student doesn't exist in the list.")


def remove_student(students, id):
    if does_exist(students, id):
        for student in students:
            if student.id == id:
                students.remove(student)
                student = None
                print("Deleting successfully!")
    else:
        print("Deleting unsuccessfully as student doesn't exist in the list.")


def write_csv(students):
    with open("students_list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "major", "gpa"])
        for student in students:
            writer.writerow(
                {
                    "id": student.id,
                    "name": student.name,
                    "major": student.major,
                    "gpa": student.gpa,
                }
            )


def read_csv():
    students_dict = []
    with open("students_list.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_dict.append(row)
    students = []
    for student in students_dict:
        students.append(
            Student(student["id"], student["name"], student["major"], student["gpa"])
        )
    return students


def append_csv(students, id):
    flag = False
    students_csv = read_csv()
    id_csv = get_id_list(students_csv)
    with open("students_list.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "major", "gpa"])
        for student in students:
            if student.id not in id_csv and student.id == id:
                writer.writerow(
                    {
                        "id": student.id,
                        "name": student.name,
                        "major": student.major,
                        "gpa": student.gpa,
                    }
                )
                flag = True
    return flag


def pick_random(students):
    result = random.choice(get_id_list(students))
    for student in students:
        if student.id == result:
            return result


def get_fname(name):
    name = name.split(" ")
    fname = name[0]
    # lname = name[-1]
    return fname


def print_tshirt(students):
    e_students = []
    for student in students:
        if student.gpa >= 3.6:
            e_students.append(student)
    if len(e_students) == 0:
        return False
    for student in e_students:
        fname = get_fname(student.name)
        length = 0
        if len(fname) == 2:
            length = 74.5
        elif len(fname) == 3:
            length = 71
        elif len(fname) == 4:
            length = 68
        elif len(fname) == 5:
            length = 64
        elif len(fname) == 6:
            length = 60.5
        elif len(fname) == 7:
            length = 57.5
        elif len(fname) == 8:
            length = 54.5
        elif len(fname) == 9:
            length = 51.5
        pdf = PDF(fname, length)
        pdf.save(f"{fname}.pdf")
    return True


if __name__ == "__main__":
    main()

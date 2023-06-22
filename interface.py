from tabulate import tabulate


def interface():
    menu = [
        {"No.": 1, "Function": "Adding student information to the list."},
        {"No.": 2, "Function": "Updating student information by ID."},
        {"No.": 3, "Function": "Sorting student list by GPA in descending order."},
        {"No.": 4, "Function": "Printing all students information and total students."},
        {"No.": 5, "Function": "Checking if student exists in the list by their ID."},
        {"No.": 6, "Function": "Deleting student information by their ID."},
        {"No.": 7, "Function": "Writing all students information to CSV File."},
        {"No.": 8, "Function": "Reading all students information from CSV File."},
        {"No.": 9, "Function": "Adding student's information to CSV File by ID."},
        {"No.": 10, "Function": "Printing shirt for students who have GPA > 3.6."},
        {"No.": 11, "Function": "Finding the luckiest person in the list"},
        {"No.": 12, "Function": "Exiting."},
    ]
    print(tabulate(menu, headers="keys", tablefmt="outline"))


def mini_interface():
    menu = [
        {"No.": 1, "Items": "ID"},
        {"No.": 2, "Items": "Name"},
        {"No.": 3, "Items": "Major"},
        {"No.": 4, "Items": "GPA"},
        {"No.": 5, "Items": "Stop adjusting"},
    ]
    print(tabulate(menu, headers="keys", tablefmt="outline"))


def print_list(students):
    lists = [
        {
            "ID": student.id,
            "Name:": student.name,
            "Major": student.major,
            "GPA": student.gpa,
        }
        for student in students
    ]
    print(
        tabulate(
            lists,
            headers="keys",
            tablefmt="grid",
            colalign=("left", "left", "left", "left"),
        )
    )
    print("Total students:", len(students))

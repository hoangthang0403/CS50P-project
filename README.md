# **STUDENT MANAGEMENT PROGRAM**
#### *Description: This is a final project for my CS50P course and for practicing purpose. These functions below are displayed for user to use on my program.*
+ Adding student to the list with following information: ID, Name, Major, GPA.
+ Updating student information by their ID.
+ Sorting student list by GPA in descending order.
+ Checking if student exists in the list by their ID.
+ Deleting student information by their ID.
+ Writing all students information to CSV File.
+ Reading all students information from CSV File.
+ Adding student's information to CSV File by their ID.
+ Printing shirt for students who have GPA > 3.6.
+ Finding the luckiest person in the list by using random library.
---
## **FILES IN PROJECT**

### **project.py**
- This file is a main file, use to run the program, and many functions besides helping running the program.

### **test_project.py**
- This file is an unit test file, to ensure the functions is worked properly on my project. There are few functions that i use to test, including:
    + is_empty to check if the student list is empty or not.
    + pick_random to pick a random person in the list.
    + get_fname to get student's first name.
    + is_validid: to check if id is valid(number) or not.
    + is_validname: to check if name is valid or not.
    + is_validmajor: to check if major is valid("CS", "IT", "DS", "BL", "BA", "DA", "LAW", "ART") or not.
    + is_validgpa: to check if gpa is valid or not (0 <= gpa <= 4).

### **student.py**
- Student class, which contains attributes of student, is used to instantiate an student object in project.py. This file is also used to validate student information.

### **interface.py**
- Displaying menu or student list on console.
### **shirtificate.py**
- Printing a T-shirt for students who have GPA greater or equal to 3.6 to PDF file.

### **shirtificate.png**
- Image of a red T-shirt which i get from CS50P course.

### **student_list.csv**
- A CSV file used to store student information.
- Here is the format of my CSV file:
    + id,name,major,gpa

### **requirements.txt**
- pip installed libraries for my project, including:
    + re
    + os
    + csv
    + tabulate
    + getch
    + fpdf
    + black
    + pytest
---
### **DOCUMENTATION**
- [https://www.geeksforgeeks.org/]
- [https://docs.python.org/3/library/]
- [https://www.w3schools.com/]
- [https://pypi.org/]
---
### **ABOUT CS50P**
- CS50P is an openware course from Havard University and taught by *Professor David J Malan*.
- CS50P is an introduction to the art of programming with Python. This course teach us from basic levels with Python to advanced levels, provided me a foundation about Python programming. *Professor David J Malan* really knows the best way to deliver knowledge to us on his lectures and this course made me satisfied after I finished it. Once again shout out to *Professor David J Malan* for his work.
---
## **THANK YOU FOR YOUR ATTENTION !!!**

from project import is_empty, get_fname, get_id_list, pick_random
from student import Student, is_validid, is_validname, is_validmajor, is_validgpa

def test_is_empty():
    students = []
    assert is_empty(students) == True
    students.append(Student("1", "Keanu Reeves", "Art", "4.0"))
    assert is_empty(students) == False


def test_get_fname():
    assert get_fname("John Watson") == "John"
    assert get_fname("Robert Downey Jr") == "Robert"


def test_pick_random():
    students = []
    students.append(Student("1", "Thang Nguyen", "CS", "3.9"))
    students.append(Student("2", "Emily Cooper", "DA", "2.0"))
    students.append(Student("3", "Tom Hiddleston", "BA", "3.55"))
    id_list = get_id_list(students)
    assert pick_random(students) in id_list


def test_validid():
    assert is_validid("1") == True
    assert is_validid("   10     ") == True
    assert is_validid(",") == False
    assert is_validid("1.") == False
    assert is_validid("A") == False


def test_validname():
    assert is_validname("   John    Watson  ") == True
    assert is_validname("JAMES BOnd") == True
    assert is_validname("An") == True
    assert is_validname("123") == False
    assert is_validname("J4mes B0nd") == False
    assert is_validname("Neymar Jr.") == False


def test_validmajor():
    assert is_validmajor("cs") == True
    assert is_validmajor("  art  ") == True
    assert is_validmajor("DOCTOR") == False
    assert is_validmajor("BI") == False #Not available in the major list


def test_validgpa():
    assert is_validgpa("3.2") == True
    assert is_validgpa("0") == True
    assert is_validgpa("4.0") == True
    assert is_validgpa("2") == True
    assert is_validgpa("-2.0") == False
    assert is_validgpa("4.1") == False
    assert is_validgpa("ABC") == False






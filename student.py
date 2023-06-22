import re


def main():
    ...


class Student:
    def __init__(self, id, name, major, gpa):
        self.id = id
        self.name = name
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"{self._id} - {self._name} - {self._major} - {self._gpa}"

    @classmethod
    def get(cls):
        # Input and check valid ID
        while True:
            try:
                id = int(input("ID: ").strip())
                break
            except ValueError:
                print("Invalid ID. Please enter again!")
        # Input and check valid name
        while True:
            try:
                name = input("Name: ").strip().title()
                name = re.sub(" +", " ", name)
                if not name.replace(" ", "").isalpha():
                    raise ValueError
                break
            except ValueError:
                print("Invalid name. Please enter again!")
        # Input and check valid major
        while True:
            try:
                major = (
                    input("Major(CS, BL, BA, DS, DA, LAW, IT,ART): ").strip().upper()
                )
                majors = ["CS", "BL", "BA", "DS", "DA", "LAW", "IT", "ART"]
                if major not in majors:
                    raise ValueError
                break
            except ValueError:
                print("Invalid major. Please enter again!")

        # Input and check valid GPA
        while True:
            try:
                gpa = float(input("GPA: ").strip())
                if gpa > 4 or gpa < 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid GPA. Please enter again!")

        return cls(id, name, major, gpa)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        try:
            if isinstance(id, str):
                id = int(id.strip())
            self._id = id
        except ValueError:
            print("Invalid ID.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        try:
            name = name.strip().title()
            name = re.sub(" +", " ", name)
            # name = " ".join(name.split(" "))
            if not name.replace(" ", "").isalpha():
                raise ValueError
            self._name = name
        except ValueError:
            print("Invalid name.")

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        try:
            major = major.strip().upper()
            majors = ["CS", "BL", "BA", "DS", "DA", "LAW", "IT", "ART"]
            if major not in majors:
                raise ValueError
            self._major = major
        except ValueError:
            print("Invalid major.")

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, gpa=0):
        # Check valid GPA
        try:
            if isinstance(gpa, str):
                gpa = float(gpa.strip())
            if gpa > 4 or gpa < 0:
                raise ValueError
            self._gpa = gpa
        except ValueError:
            print("Invalid GPA.")


def is_validid(id):
    try:
        if isinstance(id, str):
            id = int(id.strip())
        return True
    except ValueError:
        return False


def is_validname(name):
    try:
        name = name.strip().title()
        name = re.sub(" +", " ", name)
        if not name.replace(" ", "").isalpha():
            raise ValueError
        return True
    except ValueError:
        return False


def is_validmajor(major):
    try:
        major = major.strip().upper()
        majors = ["CS", "BL", "BA", "DS", "DA", "LAW", "IT", "ART"]
        if major not in majors:
            raise ValueError
        return True
    except ValueError:
        return False


def is_validgpa(gpa):
    # Check valid GPA
    try:
        if isinstance(gpa, str):
            gpa = float(gpa.strip())
        if gpa > 4 or gpa < 0:
            raise ValueError
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()

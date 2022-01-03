# position, name, age, level, salary
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 5000]


# class
class SoftwareEngineer:
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information


se1 = SoftwareEngineer("max", 20, "Junior", 5000)
se2 = SoftwareEngineer("Lisa", 25, "Senior", 5000)
se3 = SoftwareEngineer("Lisa", 25, "Senior", 5000)

# instance
se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

print(se2 == se3)

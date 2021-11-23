import random


class Employee:
    def __init__(self, name: str = " ", age: int = 0, salary: int = 0):
        self.name = name
        self.age = age
        self.salary = salary

    def printData(self):
        return f"Name: {self.name}| Age: {self.age} year old | Salary: {self.salary}"

    def get_salary(self):
        return self.salary


class Programmer(Employee):
    def __init__(self, name: str = "", age: int = 0, salary: int = 0, programmingLanguage: str = ""):
        super().__init__(name, age, salary)
        self.programmingLanguage = programmingLanguage

    def printData(self):
        return f"Name: {self.name}| Age: {self.age} year old | Salary: {self.salary} | Programming Language {self.programmingLanguage}"


class DataAnalitics(Employee):
    def __init__(self, name: str = "", age: int = 0, salary: int = 0, databaseTool: str = ""):
        super().__init__(name, age, salary)
        self.databaseTool = databaseTool

    def printData(self):
        return f"Name: {self.name}| Age: {self.age} year old | Salary: {self.salary} Tenge | DatabaseTool {self.databaseTool}"


def outMiddleSalary(lists):
    sum_of_salary = 0
    tmp = len(lists)
    for j in range(tmp):
        sum_of_salary += lists[j].get_salary()
    print("middle salary: ",sum_of_salary / tmp)


def outData(lists):
    for j in range(len(lists)):
        print(f"{j + 1}){lists[j].printData()}")


def createObj(lists, proG, dataA):
    list_name = ["Dias", "Nurmuhamed", "Adiya", "Abilay", "Madi", "Nurdana", "Danael", "Aruzhan"]
    list_programmingLang = ["Python", "C", "C++", "GO", "Kotlin", "C#", "Ruby"]
    list_dbTool = ["MSSQL", "MYSQL", "MONGO", "SQLITE", "ORACLE", "PosterSql"]
    for j in range(proG):
        lists.append(Programmer(random.choice(list_name), random.randint(18, 23), random.randint(300000, 900000),
                                random.choice(list_programmingLang)))
    for j in range(dataA):
        lists.append(DataAnalitics(random.choice(list_name), random.randint(18, 23), random.randint(400000, 1000000),
                                   random.choice(list_dbTool)))


lists = []
createObj(lists, 2, 3)
outData(lists)
outMiddleSalary(lists)

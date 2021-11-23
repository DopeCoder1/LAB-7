import random


class User:

    def __init__(self, id=0, login="", password="", name="", surname=""):
        self.id = id
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname

    def getData(self):
        return f"Id{self.id}) | Login:{self.login} | Password:{self.password} | Name:{self.name} | Surname:{self.surname}"


class Staff(User):

    def __init__(self, id=0, login="", password="", name="", surname="", salary=0):
        super().__init__(id, login, password, name, surname)
        self.salary = salary
        self.subject = []

    def getData(self):
        return f"Id{self.id}) | Login:{self.login} | Password:{self.password} | Name:{self.name} | Surname:{self.surname} | Salary:{self.salary} | Subject:{self.subject}"

    def addSubject(self, subjectName):
        self.subject.append(subjectName)


class Student(User):

    def __init__(self, id=0, login="", password="", name="", surname="", gpa=0):
        super().__init__(id, login, password, name, surname)
        self.gpa = gpa
        self.course = []

    def getData(self):
        return f"Id{self.id}) | Login:{self.login} | Password:{self.password} | Name:{self.name} | Surname:{self.surname} | Gpa:{self.gpa} | Course:{self.course}"

    def addCourse(self, courseName):
        self.course.append(courseName)


list_name = ["Dias", "Nurmuhamed", "Adiya", "Abilay", "Madi", "Nurdana", "Danael", "Aruzhan"]
list_programmingLang = ["Python", "Java Script", "C++", "GO", "Kotlin", "C#", "Ruby"]
list_dbTool = ["MSSQL", "MYSQL", "MONGO", "SQLITE", "ORACLE", "PosterSql"]
list_surname = ["Alimbayev", "Ganibaev", "Muhtarov", "Sadyrbaev", "Nazarbaev", "Abilkhan", "Kyzyrov", "Gaip"]


def randomPassWord(length=4):
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(length))


def createObj(lists, Student_l, Staff_l, User_l):
    for j in range(Student_l):
        lists.append(
            Student(j, randomPassWord(5), randomPassWord(), random.choice(list_name), random.choice(list_surname),random.randint(1, 3)))
        lists[j].addCourse(random.choice(list_programmingLang))
    for i in range(Student_l,Student_l+Staff_l):
        lists.append(Staff(i, randomPassWord(5), randomPassWord(), random.choice(list_name), random.choice(list_surname),random.randint(300000,500000)))
        lists[i].addSubject(random.choice(list_programmingLang))
    for z in range(Student_l+Staff_l, Student_l+Staff_l+User_l):
        lists.append(User(z, randomPassWord(6), randomPassWord(6), random.choice(list_name), random.choice(list_surname)))

def outData(lists):
    for j in range(len(lists)):
        print(f"{lists[j].getData()}")


lists = []
createObj(lists,3,5,3)
outData(lists)

import random


class Book:

    def __init__(self, name, code, pages):
        self.name = name
        self.code = code
        self.pages = pages

    def getBookData(self):
        return f"Name:{self.name} | Code:{self.code} | Pages:{self.pages}"


class ScientificBook(Book):

    def __init__(self, name, code, pages, price, publicsher):
        super().__init__(name, code, pages)
        self.price = price
        self.publicsher = publicsher

    def getBookData(self):
        return f"Name:{self.name} | Code:{self.code} | Pages:{self.pages} | Price:{self.price} | Publisher:{self.publicsher}"


class LiteratureBook(Book):

    def __init__(self, name, code, pages, author, publishedYear):
        super().__init__(name, code, pages)
        self.author = author
        self.publishedYear = publishedYear

    def getBookData(self):
        return f"{self.name} | Code:{self.code} | Pages:{self.pages} | Author:{self.author} | Publisher year:{self.publishedYear}"


class Library:

    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.county = country
        self.lists = []

    def addBook(self, Book):
        self.lists.append(Book)

    def printLibraryData(self):
        for j in range(len(lists)):
            print(f"{j}){lists[j]}")
        return f"Name:{self.name} | City:{self.city} | Country:{self.county}"


list_book = ['Краткая история времени', 'Космос', 'Эгоистичный ген', 'Происхождение видов','Структура научных революций', 'Против метода']
list_author_sc = ['Стивен Уильям Хокинг', 'Карл Саган', 'Ричард Докинз', 'Чарлз Дарвин', 'Томас Кун', 'Фейерабенд, Пол']
list_publisher = ['Альпина Паблишер', 'Эксмо', 'Издательский дом Питер', 'Попурри', 'Азбука-Аттикус', 'Corpus']
list_book_li = ['1984', 'Американская трагедия', 'Фауст', 'Сто лет одиночества', 'Мартин Иден', 'Илиада']


def createObj(lib_name, city, country, lists, Sc, Lt):
    lb = Library(lib_name, city, country)
    for j in range(Sc):
        # tmp = ScientificBook("Harry Potter",1020,300,5000,"Almaty book")
        buffer = ScientificBook(random.choice(list_book), random.randint(1000,2000), random.randint(300,500), random.randint(5000,8000), random.choice(list_publisher))
        lists.append(buffer.getBookData())
    for j in range(Lt):
        buffer2 = LiteratureBook(random.choice(list_book_li), random.randint(2000,3000), random.randint(400,800),random.choice(list_author_sc),random.randint(1950,2010))
        lists.append(buffer2.getBookData())
    lb.addBook(lists)
    print(lb.printLibraryData())

lists = []
createObj("Almaty Library", "Almaty", "KZ", lists, 2,3)
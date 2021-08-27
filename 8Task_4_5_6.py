# Task 4.
# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class ToStorageError(StorageError):
    def __init__(self, text):
        self.text = f"Can't go to storage:\n {text}"


class ToDepartmentError(StorageError):
    def __init__(self, text):
        self.text = f"Can't be transferred:\n {text}"


class ValidateItemError(StorageError):
    pass


class Storage:
    def __init__(self):
        self.__storage = []

    def to_storage(self, items):
        if not all([isinstance(item, OfficeTech) for item in items]):
            raise ToStorageError(f"{items} might be out of scope")
        self.__storage.extend(items)

    def to_department(self, index: int, department: str):
        if not isinstance(index, int):
            raise ToDepartmentError(f"Incorrect index {type(index)}'")
        item: OfficeTech = self.__storage[index]

        if item.department != "Available":
            raise ToDepartmentError(f"{item} belongs to the '{item.department}'")
        item.department = department

    def to_filter(self, **kwargs):
        for i in self.__storage:
            if all([i.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield self.__storage.index(i), i

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        return self.__storage[index]

    def __delitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        del self.__storage[index]

    def __iter__(self):
        return self.__storage.__iter__()

    def __str__(self):
        return f"{len(self.__storage)} pieces of equipment are stored"


class OfficeTech:

    def __init__(self, model: str, manufacturer: str, format: str, price: float, name="equipment"):
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.format = format
        self.price = price
        self.department = "Available"
        self.printing = True if self.__class__ in (Printer, Copier) else False
        self.scanning = True if self.__class__ in (Scanner, Copier) else False

    def __str__(self):
        return f"{self.model} {self.manufacturer}"


class Printer(OfficeTech):
    printing = True
    scanning = False

    def __init__(self, *args):
        super().__init__(name="Printer", *args)


class Scanner(OfficeTech):
    printing = False
    scanning = True

    def __init__(self, *args):
        super().__init__(name="Scanner", *args)


class Copier(OfficeTech):
    printing = False
    scanning = True

    def __init__(self, *args):
        super().__init__(name="Copier", *args)


storage = Storage()

params = ["model", "manufacturer", "format", "price"]
list_of_equipment = ["Printer", "Scanner", "Copier"]

item_1 = Printer("Aurora AD 220MNW", "Apple", "A4", 89666)
item_2 = Scanner("IM SC456", "HP", "A2", 10000)
item_3 = Printer("Ink Tank 15", "HP", "A0", 666)
item_4 = Copier("Lukyanenko", "USSR", "A5", 546372)

storage.to_storage([item_1, item_2, item_3, item_4])

print(storage)

for index, item in storage.to_filter(manufacturer="HP"):
    storage.to_department(index, "Brutal Murder Imagining Department")
    print(f"The {item.name} {item} would go to the \"Brutal Murder Imagining Department\"")

for index, item in storage.to_filter(department="Available"):
    print(f"{item.name} {item} index({index}) is available")

print(storage)
for index, item in storage.to_filter(price=666):
    del storage[index]

print(storage)


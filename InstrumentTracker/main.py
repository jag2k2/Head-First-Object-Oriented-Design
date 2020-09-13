from typing import List


class Guitar:
    _serial_number: str
    _builder: str
    _model: str
    _type: str
    _back_wood: str
    _top_wood: str
    _price: float

    def __init__(self, serial_number: str, price: float, builder: str, model: str, type: str, back_wood: str,
                 top_wood: str) -> None:
        self._serial_number = serial_number
        self._builder = builder
        self._model = model
        self._type = type
        self._back_wood = back_wood
        self._top_wood = top_wood
        self._price = price

    def get_serial_number(self) -> str:
        return self._serial_number

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float) -> None:
        self._price = new_price

    def get_builder(self) -> str:
        return self._builder

    def get_model(self) -> str:
        return self._model

    def get_type(self) -> str:
        return self._type

    def get_back_wood(self) -> str:
        return self._back_wood

    def get_top_wood(self) -> str:
        return self._top_wood


class Inventory:
    _guitars = List[Guitar]

    def __init__(self) -> None:
        self._guitars = []

    def add_guitar(self, serial_number: str, price: float, builder: str, model: str, type: str, back_wood: str,
                   top_wood: str) -> None:
        guitar: Guitar = Guitar(serial_number, price, builder, model, type, back_wood, top_wood)
        self._guitars.append(guitar)

    def get_guitar(self, serial_number: str) -> Guitar:
        for i in range(len(self._guitars)):
            if self._guitars[i].get_serial_number == serial_number:
                return self._guitars[i].get_serial_number

    def search(self, search_guitar: Guitar) -> Guitar:
        for i in range(len(self._guitars)):
            if self._guitars[i].get_builder() == search_guitar.get_builder():
                if self._guitars[i].get_model() == search_guitar.get_model():
                    if self._guitars[i].get_type() == search_guitar.get_type():
                        if self._guitars[i].get_back_wood() == search_guitar.get_back_wood():
                            if self._guitars[i].get_top_wood() == search_guitar.get_top_wood():
                                return self._guitars[i]


inventory: Inventory = Inventory()
inventory.add_guitar("V132", 1000, "Fender", "Stratocaster", "electric", "Alder", "Alder")
inventory.add_guitar("V133", 2000, "Gibson", "Les Paul", "electric", "Pine", "Pine")
inventory.add_guitar("V134", 2500, "Martin", "GPC", "acoustic", "Balsa", "Balsa")

erin_preferences: Guitar = Guitar("", 0, "Fender", "Stratocaster", "electric", "Alder", "Alder")

result: Guitar = inventory.search(erin_preferences)

if result is not None:
    print("You might like this one:")
    print("Serial Number: " + result.get_serial_number())
else:
    print("Sorry we don't have anything for you")



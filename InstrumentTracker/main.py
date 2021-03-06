from typing import List
from enum import Enum


class Wood(Enum):
    INDIAN_ROSEWOOD = 0
    BRAZILIAN_ROSEWOOD = 1
    MAHOGANY = 2
    MAPLE = 3
    COCOBOLO = 4
    CEDAR = 5
    ADIRONDACK = 6
    ALDER = 7
    SITKA = 8


class Builder(Enum):
    FENDER = 0
    MARTIN = 1
    GIBSON = 2
    COLLINGS = 3
    OLSON = 4


class Type(Enum):
    ELECTRIC = 0
    ACOUSTIC = 1


class GuitarSpec:
    _builder: Builder
    _model: str
    _type: Type
    _back_wood: Wood
    _top_wood: Wood
    _num_strings: float

    def __init__(self, builder: Builder, model: str, type: Type, back_wood: Wood, top_wood: Wood,
                 num_strings: float) -> None:
        self._builder = builder
        self._model = model
        self._type = type
        self._back_wood = back_wood
        self._top_wood = top_wood
        self._num_strings = num_strings

    def get_builder(self) -> Builder:
        return self._builder

    def get_model(self) -> str:
        return self._model

    def get_type(self) -> Type:
        return self._type

    def get_back_wood(self) -> Wood:
        return self._back_wood

    def get_top_wood(self) -> Wood:
        return self._top_wood

    def get_num_strings(self) -> float:
        return self._num_strings

    def matches(self, other_spec: 'GuitarSpec') -> bool:
        if self._builder is other_spec.get_builder():
            if self._model.lower() == other_spec._model.lower():
                if self._type is other_spec._type:
                    if self._back_wood is other_spec._back_wood:
                        if self._top_wood is other_spec._top_wood:
                            if self._num_strings == other_spec._num_strings:
                                return True
        else:
            return False


class Guitar:
    _serial_number: str
    _price: float
    _spec: GuitarSpec

    def __init__(self, serial_number: str, price: float, spec: GuitarSpec) -> None:
        self._serial_number = serial_number
        self._price = price
        self._spec = spec

    def get_serial_number(self) -> str:
        return self._serial_number

    def get_price(self) -> float:
        return self._price

    def set_price(self, new_price: float) -> None:
        self._price = new_price

    def get_spec(self) -> GuitarSpec:
        return self._spec


class Inventory:
    _guitars = List[Guitar]

    def __init__(self) -> None:
        self._guitars = []

    def add_guitar(self, serial_number: str, price: float, spec: GuitarSpec) -> None:
        guitar: Guitar = Guitar(serial_number, price, spec)
        self._guitars.append(guitar)

    def get_guitar(self, serial_number: str) -> Guitar:
        for j in range(len(self._guitars)):
            if self._guitars[j].get_serial_number == serial_number:
                return self._guitars[j].get_serial_number

    def search(self, search_spec: GuitarSpec) -> List[Guitar]:
        _matching_guitars: List[Guitar] = []
        for i in range(len(self._guitars)):
            if self._guitars[i].get_spec().matches(search_spec):
                _matching_guitars.append(self._guitars[i])
        return _matching_guitars


inventory: Inventory = Inventory()
spec1: GuitarSpec = GuitarSpec(Builder.FENDER, "Stratocaster", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
inventory.add_guitar("V132", 1000, spec1)
spec2: GuitarSpec = GuitarSpec(Builder.GIBSON, "Les Paul", Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE, 6)
inventory.add_guitar("V133", 2000, spec2)
spec3: GuitarSpec = GuitarSpec(Builder.MARTIN, "GPC", Type.ACOUSTIC, Wood.CEDAR, Wood.CEDAR, 6)
inventory.add_guitar("V134", 2500, spec3)
spec4: GuitarSpec = GuitarSpec(Builder.FENDER, "Stratocaster", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)
inventory.add_guitar("V135", 2900, spec4)

erin_preferences: GuitarSpec = GuitarSpec(Builder.FENDER, "stratocaster", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6)

results: List[Guitar] = inventory.search(erin_preferences)

if results:
    for i in range(len(results)):
        print("You might like this one:")
        print("Builder: " + results[i].get_spec().get_builder().name)
        print("Model: " + results[i].get_spec().get_model())
        print("Type: " + results[i].get_spec().get_type().name)
        print("Back and sides: " + results[i].get_spec().get_back_wood().name)
        print("Top: " + results[i].get_spec().get_top_wood().name)
        print("Strings: " + str(results[i].get_spec().get_num_strings()))
        print("Price: " + str(results[i].get_price()))
        print("")
else:
    print("Sorry we don't have anything for you")



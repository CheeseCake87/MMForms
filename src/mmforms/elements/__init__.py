class BaseInput:
    _start = "<input "
    _end = ">"
    _type: str = None
    _name: str = None
    _id: str = None
    _value: str = None
    _class: str = None
    _required: bool = False

    def __init__(self, name):
        self._name = name

    def type(self, type_: str):
        self._type = type_
        return self

    def id(self, id_: str):
        self._id = id_
        return self

    def value(self, value: str):
        self._value = value
        return self

    def class_(self, class_: str):
        self._class = class_
        return self

    def required(self):
        self._required = True
        return self

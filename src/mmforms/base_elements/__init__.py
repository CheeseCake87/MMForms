class BaseDiv:
    _start = "<div "
    _start_end = ">"
    _end = "</div>"
    _id: str = None
    _class: str = None
    _style: str = None

    def id(self, id_: str):
        self._id = id_
        return self

    def class_(self, class_: str):
        self._class = class_
        return self

    def style(self, style_: str):
        self._style = style_
        return self


class BaseStartDiv:
    _start = "<div "
    _start_end = ">"
    _id: str = None
    _class: str = None
    _style: str = None

    def id(self, id_: str):
        self._id = id_
        return self

    def class_(self, class_: str):
        self._class = class_
        return self

    def style(self, style_: str):
        self._style = style_
        return self


class BaseInput:
    _start = "<input "
    _end = ">"
    _type: str = None
    _name: str = None
    _id: str = None
    _value: str = None
    _class: str = None
    _required: bool = False
    _checked: bool = False

    def name(self, name: str):
        self._name = name
        return self

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

    def checked(self):
        self._checked = True
        return self



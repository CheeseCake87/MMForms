class BaseDiv:
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

    def t_button(self):
        self._type = 'type="button" '
        return self

    def t_checkbox(self):
        self._type = 'type="checkbox" '
        return self

    def t_color(self):
        self._type = 'type="color" '
        return self

    def t_date(self):
        self._type = 'type="date" '
        return self

    def t_datetime_local(self):
        self._type = 'type="datetime-local" '
        return self

    def t_email(self):
        self._type = 'type="email" '
        return self

    def t_file(self):
        self._type = 'type="file" '
        return self

    def t_hidden(self):
        self._type = 'type="hidden" '
        return self

    def t_image(self):
        self._type = 'type="image" '
        return self

    def t_month(self):
        self._type = 'type="month" '
        return self

    def t_number(self):
        self._type = 'type="number" '
        return self

    def t_password(self):
        self._type = 'type="password" '
        return self

    def t_radio(self):
        self._type = 'type="radio" '
        return self

    def t_range(self):
        self._type = 'type="range" '
        return self

    def t_reset(self):
        self._type = 'type="reset" '
        return self

    def t_search(self):
        self._type = 'type="search" '
        return self

    def t_submit(self):
        self._type = 'type="submit" '
        return self

    def t_tel(self):
        self._type = 'type="tel" '
        return self

    def t_text(self):
        self._type = 'type="text" '
        return self

    def t_time(self):
        self._type = 'type="time" '
        return self

    def t_url(self):
        self._type = 'type="url" '
        return self

    def t_week(self):
        self._type = 'type="week" '
        return self

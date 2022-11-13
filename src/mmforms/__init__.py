class Form:
    _start = "<form>"
    _end = "</form>"

    def __init__(self, **kwargs):
        for k, a in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, a.build())

    def getattr(self, k):
        return getattr(self, k)

    def build(self):
        _out = str()
        for k, v in self.__dict__.items():
            _out += f"{v}"

        return f'{self._start}{_out}{self._end}'

    def upval(self, element, value):
        if hasattr(self, element):
            pass
            # print("hasattr")
            # print("value", value)

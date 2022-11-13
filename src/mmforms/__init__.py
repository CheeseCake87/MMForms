import re
from collections import OrderedDict
from typing import Union

from markupsafe import Markup

from .base_elements import BaseInput, BaseDiv, BaseStartDiv


def update_value(element, value) -> str:
    def process(raw, new_value):
        if 'type="text"' in raw:
            pattern, replace = r'value="(.*?)"', rf'value="{new_value}"'
            if re.search(pattern, raw) is not None:
                return re.sub(pattern, replace, raw)
            return raw.replace('<input ', f'<input value="{new_value}" ')

        if 'type="checkbox"' in raw:
            if isinstance(new_value, bool):  # if value is bool
                if new_value:  # if value is True
                    if 'checked="checked"' in raw:
                        return raw
                    return raw.replace('>', f' checked="checked">')
                # if value is False
                if 'checked="checked"' in raw:
                    return raw.replace(' checked="checked"', '')
                return raw

    if isinstance(element, Markup):
        return Markup(process(element.unescape(), value))
    if isinstance(element, str):
        return process(element, value)
    if hasattr(element, "compile"):
        return process(element.compile(raw=True), value)


class Input(BaseInput):
    _start = "<input "
    _end = ">"

    def compile(self, raw: bool = False) -> Union[str, Markup]:
        _type_, _name_, _id_, _value_, _class_ = str(), str(), str(), str(), str()
        _required_, _checked_ = str(), str()
        if self._type:
            _type_ = f'type="{self._type}" '
        if self._name:
            _name_ = f'name="{self._name}" '
        if self._id:
            _id_ = f'id="{self._id}" '
        if self._value:
            _value_ = f'value="{self._value}" '
        if self._class:
            _class_ = f'class="{self._class}" '
        if self._required:
            _required_ = f'required="required" '
        if self._checked:
            _checked_ = f'checked="checked" '

        __out = f'{self._start}{_type_}{_name_}{_id_}{_value_}{_class_}{_required_}{_checked_}{self._end}'.replace(' >', '>')

        if raw:
            return __out
        return Markup(__out)


class Div(BaseDiv):
    _element = None

    def __init__(self, element: any = None) -> None:
        self._element = self._set_element(element)

    @staticmethod
    def _set_element(element: any) -> str:
        if element is None:
            return ""
        if isinstance(element, str):
            return element
        if isinstance(element, list):
            return "".join([e.compile(raw=True) for e in element])
        if isinstance(element, Markup):
            return element.unescape()
        if hasattr(element, "compile"):
            return element.compile(raw=True)

    def compile(self, raw: bool = False) -> Union[str, Markup]:
        _id_, _class_, _style_ = str(), str(), str()
        if self._id:
            _id_ = f'id="{self._id}" '
        if self._class:
            _class_ = f'class="{self._class}" '
        if self._style:
            _style_ = f'style="{self._style}" '

        __out = f'{self._start}{_id_}{_class_}{_style_}{self._start_end}{self._element}{self._end}'.replace(' >', '>')
        if raw:
            return __out
        return Markup(__out)


class StartDiv(BaseStartDiv):
    def compile(self, raw: bool = False) -> Union[str, Markup]:
        _id_, _class_, _style_ = str(), str(), str()
        if self._id:
            _id_ = f'id="{self._id}" '
        if self._class:
            _class_ = f'class="{self._class}" '
        if self._style:
            _style_ = f'style="{self._style}" '

        __out = f'{self._start}{_id_}{_class_}{_style_}{self._start_end}'.replace(' >', '>')
        if raw:
            return __out
        return Markup(__out)


class EndDiv:
    @staticmethod
    def compile(raw: bool = False) -> Union[str, Markup]:
        __out = '</div>'
        if raw:
            return __out
        return Markup(__out)


class InputGroup:
    elements = OrderedDict()

    __wrap_count = 0

    def __init__(self, **kwargs):
        for k, a in kwargs.items():
            if isinstance(a, str):
                self.elements[a] = a
            if isinstance(a, Markup):
                self.elements[a] = a.unescape()
            if hasattr(a, "compile"):
                self.elements[k] = a.compile(raw=True)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.elements})"

    def wrap(self, element: Union[Markup, str, Div]):
        if isinstance(element, Div):
            self.__wrap_count += 1
            # add element to the start of the OrderedDict
            start = f'__start_{self.__wrap_count}__'
            end = f'__end_{self.__wrap_count}__'

            self.elements = OrderedDict(
                {
                    start: element.compile(raw=True).replace('</div>', ''),
                    **self.elements,
                    end: '</div>'
                }
            )
        return self

    def get_element(self, k) -> Union[None, str]:
        if k in self.elements:
            return self.elements[k]
        return None

    def compile(self, raw: bool = False) -> Union[str, Markup]:
        _out = [v for v in self.elements.values()]
        if raw:
            return "".join(_out)
        return Markup("".join(_out))

    def all(self) -> dict:
        print(self.__dict__)
        return {k: Markup(v) for k, v in self.elements.items()}

    def update_value(self, element: Union[Markup, str], value: Union[bool, str, int]) -> None:
        if element in self.elements:
            self.elements[element] = update_value(self.elements[element], value)

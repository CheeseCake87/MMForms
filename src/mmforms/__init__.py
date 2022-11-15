import re
from collections import OrderedDict
from typing import Union

from markupsafe import Markup

from .base_elements import BaseInput, BaseDiv


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
    def compile(self, raw: bool = False) -> Union[str, Markup]:
        name = id_ = value = class_ = str()
        required = checked = str()
        if self._name:
            name = f'name="{self._name}" '
        if self._id:
            id_ = f'id="{self._id}" '
        if self._value:
            value = f'value="{self._value}" '
        if self._class:
            class_ = f'class="{self._class}" '
        if self._required:
            required = f'required="required" '
        if self._checked:
            checked = f'checked="checked" '

        out = (
            '<input '
            f'{self._type}'
            f'{name}'
            f'{id_}'
            f'{value}'
            f'{class_}'
            f'{required}'
            f'{checked}'
            '>'
        )

        if raw:
            return out
        return Markup(out)


class Div(BaseDiv):
    _element = None

    def __init__(self, element: any = None) -> None:
        self._element = self._make_element_raw(element)

    @staticmethod
    def _make_element_raw(element: any) -> str:
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
        id_ = class_ = style = str()
        if self._id:
            id_ = f'id="{self._id}" '
        if self._class:
            class_ = f'class="{self._class}" '
        if self._style:
            style = f'style="{self._style}" '

        out = (
            '<div '
            f'{id_}'
            f'{class_}'
            f'{style}'
            '>'
            f'{self._element}'
            '</div>'
        )
        if raw:
            return out
        return Markup(out)


class InputGroup:
    _elements: OrderedDict = None
    _wrap_count: int = None

    def elements(self, **kwargs):
        wrap_count = 0
        elements = OrderedDict()

        for k, a in kwargs.items():
            if isinstance(a, str):
                elements[a] = a
            if isinstance(a, Markup):
                elements[a] = a.unescape()
            if hasattr(a, "compile"):
                elements[k] = a.compile(raw=True)

        self._wrap_count = wrap_count
        self._elements = elements

    def __call__(self) -> dict:
        return self.dict()

    def __repr__(self):
        return f"{self.__class__.__name__}({self._elements})"

    def wrap(self, element: Union[Markup, str, Div]):
        if isinstance(element, Div):
            self._wrap_count += 1
            # add element to the start of the OrderedDict
            start = f'__start_{self._wrap_count}__'
            end = f'__end_{self._wrap_count}__'

            self._elements = OrderedDict(
                {
                    start: element.compile(raw=True).replace('</div>', ''),
                    **self._elements,
                    end: '</div>'
                }
            )
        return self

    def get_element(self, k) -> Union[None, str]:
        if k in self._elements:
            return self._elements[k]
        return None

    def compile(self, raw: bool = False) -> Union[str, Markup]:
        out = [v for v in self._elements.values()]
        if raw:
            return "".join(out)
        return Markup("".join(out))

    def dict(self) -> dict:
        return {k: Markup(v) for k, v in self._elements.items()}

    def update_value(self, element: Union[Markup, str], value: Union[bool, str, int]) -> None:
        if element in self._elements:
            self._elements[element] = update_value(self._elements[element], value)

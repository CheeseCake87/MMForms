import re
from collections import OrderedDict
from typing import Union

from markupsafe import Markup

from .base_elements import BaseInput, BaseDiv
from .factories import MethodFactory


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
    _elements: OrderedDict = None
    _start: str = None

    def __init__(self) -> None:
        self._elements = OrderedDict()

    def __repr__(self):
        return f"{self.__class__.__name__}({self._elements})"

    def _encapsulate(self, elements: OrderedDict):
        id_ = class_ = style = str()
        if self._id:
            id_ = f'id="{self._id}" '
        if self._class:
            class_ = f'class="{self._class}" '
        if self._style:
            style = f'style="{self._style}" '
        self._start = (
            '<div '
            f'{id_}'
            f'{class_}'
            f'{style}'
            '>'
        )
        return OrderedDict(
            {
                "__start__": self._start,
                **elements,
                "__end__": '</div>'
            }
        )

    def elements(self, **kwargs):
        self._elements = MethodFactory.elements(kwargs, self._elements)
        return self

    def compile(self, raw: bool = False) -> Union[str, Markup]:
        out = [v for v in self._encapsulate(self._elements).values()]
        if raw:
            return "".join(out)
        return Markup("".join(out))

    def dict(self) -> dict:
        return {k: Markup(v) for k, v in self._encapsulate(self._elements).items()}


class Group:
    _elements: OrderedDict = None
    _wrap_count: int = None

    def __init__(self) -> None:
        self._elements = OrderedDict()
        self._wrap_count = 0

    def __repr__(self):
        return f"{self.__class__.__name__}({self._elements})"

    def elements(self, **kwargs):
        self._elements = MethodFactory.elements(kwargs, self._elements)
        return self

    def wrap(self, element: Union[Div]):
        self._wrap_count += 1
        self._elements = MethodFactory.wrap(element, self._elements, self._wrap_count)
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


class Form:
    name: str = None
    _elements: OrderedDict = None
    _wrap_count: int = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self._elements = OrderedDict()

    def __repr__(self):
        return f"{self.__class__.__name__}({self._elements})"

    def __call__(self):
        return self.dict()

    def elements(self, **kwargs):
        self._elements = MethodFactory.elements(kwargs, self._elements)
        return self

    def groups(self, *args: Group):
        self._elements = MethodFactory.groups(args, self._elements)
        return self

    def wrap(self, element: Union[Div]):
        self._wrap_count += 1
        self._elements = MethodFactory.wrap(element, self._elements, self._wrap_count)
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

    def update_value(self, input_field: str, value: Union[bool, str, int]) -> None:
        if input_field in self._elements:
            self._elements[input_field] = update_value(self._elements[input_field], value)

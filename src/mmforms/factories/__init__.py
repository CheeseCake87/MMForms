from collections import OrderedDict
from typing import Union, TypeVar

from markupsafe import Markup

Div = TypeVar('Div')


class MethodFactory:
    @staticmethod
    def wrap(element: Union[Div], elements: OrderedDict, count: int) -> OrderedDict:
        start = f'__start_{count}__'
        end = f'__end_{count}__'
        return OrderedDict(
            {
                start: element.compile(raw=True).replace('</div>', ''),
                **elements,
                end: '</div>'
            }
        )

    @staticmethod
    def elements(kwa, elements: OrderedDict) -> OrderedDict:
        for k, a in kwa.items():
            if isinstance(a, str):
                elements[k] = a
            if isinstance(a, Markup):
                elements[k] = a.unescape()
            if hasattr(a, "compile"):
                elements[k] = a.compile(raw=True)
        return elements

    @staticmethod
    def groups(args, elements: OrderedDict) -> OrderedDict:
        for v in args:
            if hasattr(v, "dict"):
                _ = v.dict()
                for i, (ik, iv) in enumerate(_.items()):
                    if "__" in ik:
                        elements.update({f"__{i}__": iv})
                    elif ik in elements:
                        elements.update({f"{ik}_{i}": iv})
                    else:
                        elements.update({ik: iv})
        return elements

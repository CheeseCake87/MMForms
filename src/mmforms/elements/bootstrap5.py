from . import BaseInput


class Input(BaseInput):
    _start = "<input "
    _end = ">"

    def build(self):
        _type_, _name_, _id_, _value_, _class_ = str(), str(), str(), str(), str()
        _required_ = str()
        if self._type:
            _type_ = f'type="{self._type}" '
        if self._name:
            _name_ = f'name="{self._name}" '
        if self._id:
            _id_ = f'id="{self._id}" '
        if self._value:
            _value_ = f'value="{self._value}" '
        if self._class:
            _class_ = f' {self._class}'
        if self._required:
            _required_ = f'required '
        return f'{self._start}{_type_}{_name_}{_id_}{_value_}class="form-control{_class_}" {_required_}{self._end}'

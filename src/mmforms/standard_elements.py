from ._base_elements import BaseInput, BaseInputGroup, BaseForm


class Input(BaseInput):
    def __init__(self, *args):
        super().__init__(*args)


class InputGroup(BaseInputGroup):
    def __init__(self, *args):
        super().__init__(*args)


class Form(BaseForm):
    def __init__(self, *args):
        super().__init__(*args)

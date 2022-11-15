from flask import Flask, render_template

from src.mmforms import Input, Div, InputGroup

app = Flask(__name__)

wrap_div = Div().class_('form-group')

test_form = InputGroup() \
    .wrap(wrap_div) \
    .elements(
    first_name=Input().t_text().name('first_name').id('first_name').class_('form-group').required(),
    last_name=Input().t_text().name('last_name').id('last_name').required(),
    submit=Input().t_submit().name('submit').id('submit').value('Submit')
)

test_form_1 = InputGroup() \
    .wrap(wrap_div) \
    .wrap(wrap_div) \
    .elements(
    address_1=Input().t_text().name('address_1').id('address_1').required(),
    address_2=Input().t_text().name('address_2').id('address_2'),
)

print(test_form_1.compile())
print(test_form_1.dict())


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', test_form=test_form.dict(), test_form_1=test_form_1.dict())


if __name__ == '__main__':
    app.run()

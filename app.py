from flask import Flask, render_template

from src.mmforms import InputGroup, Input, Div

app = Flask(__name__)

wrap_div = Div().class_('form-group')

first_name = Input().type('text').name('first_name').id('first_name').required()
last_name = Input().type('text').name('last_name').id('last_name').required()

test_form = InputGroup(
    first_name=first_name.class_('form-control'),
    last_name=last_name.class_('form-control')
).wrap(wrap_div)

test_form_1 = InputGroup(
    first_name=first_name.class_('form-control'),
    last_name=last_name.class_('form-control')
).wrap(wrap_div)


test_form.update_value('first_name', 'John')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html', test_form=test_form.all(), test_form_1=test_form_1.all())


if __name__ == '__main__':
    app.run()

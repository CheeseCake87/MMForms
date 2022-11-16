from flask import Flask, render_template

from src.mmforms import Input, Div, Group, Form

app = Flask(__name__)

first_name = Input().t_text().name('first_name').id('first_name').class_('form-group').required()
last_name = Input().t_text().name('last_name').id('last_name').required()
submit = Input().t_submit().name('submit').id('submit').value('Submit')

name_group = Group().elements(
    first_name=first_name,
    last_name=last_name,
    submit=submit.class_('form-group'),
).wrap(Div().class_('form-group'))

name_form = Form("name").groups(name_group)

for key, value in name_form.dict().items():
    print(key, value)


@app.route('/')
def hello_world():
    return render_template('index.html', name_form=name_form.dict())


if __name__ == '__main__':
    app.run()

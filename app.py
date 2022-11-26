from flask import Flask, render_template


from src.mmforms.standard_elements import Form, InputGroup, Input
from src.mmforms.bootstrap_elements import InputGroup as BSInputGroup

app = Flask(__name__)

form = Form("test_form").add_input_groups(
    BSInputGroup(
        Input("name").t_text(),
        Input("email").t_email(),
    ),
).add_inputs(
    Input("password").t_password(),
)

form.update_value("name", "test")

print(form)

@app.route('/')
def hello_world():
    return render_template('index.html', form=form.compile())


if __name__ == '__main__':
    app.run()

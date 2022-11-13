from flask import Flask, render_template

from src.mmforms import Form
from src.mmforms.elements.bootstrap5 import Input

app = Flask(__name__)

test_form = Form(
    new_input=Input("name").type("text").id("name").class_("form-input").required()
)

# print(dir(test_form))
# print(test_form.getattr("new_input"))
print(test_form.build())

test_form.upval("new_input", "new_value")


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

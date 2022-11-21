from flask import Flask, render_template

from src.mmforms import Input, InputGroup, Form
from src.mmforms.bootstrap import BootstrapInput

app = Flask(__name__)

first_name = BootstrapInput("first_name").t_text()
middle_name = Input("middle_name").t_text()
last_name = Input("last_name").t_text()

address_line_1 = Input("address_line_1").t_text()
address_line_2 = Input("address_line_2").t_text()
address_line_3 = Input("address_line_3").t_text()

postcode = Input("postcode").t_text()
city_town = Input("city_town").t_text()

name_ig = InputGroup(
    first_name.class_("col-4"),
    middle_name,
    last_name,
).wrap(class_="input-group", id_="name_ig")

print(name_ig)

address_ig = InputGroup(
    address_line_1,
    address_line_2,
    address_line_3
).wrap(class_="input-group")

city_town_ig = InputGroup(
    city_town,
    postcode
).wrap(class_="input-group")

name_form = Form("name")

name_form.add_input_groups(
    name_ig,
    address_ig,
    city_town_ig
)

print(name_form)


@app.route('/')
def hello_world():
    return render_template('index.html', name_form=name_form.markup())


if __name__ == '__main__':
    app.run()

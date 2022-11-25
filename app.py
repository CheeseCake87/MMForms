from flask import Flask, render_template

from src.mmforms import Input, InputGroup, Form
from src.mmforms.bootstrap import BootstrapInput

app = Flask(__name__)

first_name = BootstrapInput("first_name").t_text().value("John")
middle_name = Input("middle_name").t_text().value("John1")
last_name = Input("last_name").t_text().value("John2")

address_line_1 = Input("address_line_1").t_text().value("address_line_1")
address_line_2 = Input("address_line_2").t_text().value("address_line_2")
address_line_3 = Input("address_line_3").t_text().value("address_line_3")

postcode = Input("postcode").t_text().value("postcode")
city_town = Input("city_town").t_text().value("city_town")

car = Input("car").t_text().value("car")

car_group = InputGroup(car).wrap(class_="col-12 col-md-6")

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

name_form.add_inputs(
    car
)

print(name_form)


@app.route('/')
def hello_world():
    return render_template('index.html', name_form=name_form.markup())


if __name__ == '__main__':
    app.run()

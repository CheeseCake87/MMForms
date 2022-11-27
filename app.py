from flask import Flask, render_template

from src.mmforms.standard_elements import Form, Input, Label

app = Flask(__name__)

form = Form("test_form").inputs(
    Input("name").t_text(),
    Input("car_type_volvo").t_radio().name("car_type_radio").value("volvo").id("volvo"),
    Label().for_("volvo").text("Volvo"),
    Input("car_type_saab").t_radio().name("car_type_radio").value("saab").id("saab"),
    Label().for_("saab").text("Saab"),
)

print(form)


@app.route('/')
def hello_world():
    return render_template('index.html', form=form.compile())


if __name__ == '__main__':
    app.run()

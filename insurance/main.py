
from dataclasses import dataclass
from flask import Flask,render_template
from forms import InputForm
from model import Calc

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

@app.route('/', methods=["GET","POST"])
def hello():
    iform = InputForm()
    if iform.validate_on_submit():
        return render_template('home.html', form = iform, data=Calc(iform.age.data, iform.bmi.data, iform.smoker.data))
    else:
        print(iform.errors)
    return render_template('home.html', form = iform, data= "")

if __name__ == '__main__':
    app.run()


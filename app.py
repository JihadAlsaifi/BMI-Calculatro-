from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    if request.method == 'POST':
        height = int(request.form['height'])
        weight = int(request.form['weight'])
        if height > 0 and weight > 0:
            bmi = weight / ((height / 100) ** 2)
    return render_template('index.html', bmi=bmi)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = '17102003'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    if not name or not email:
        flash('Please fill out both name and email fields.', 'error')
        return render_template('form.html') 

    return render_template('resutl.html', name=name, email=email)



if __name__ == '__main__':
    app.run(debug=True)

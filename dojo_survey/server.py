from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app.secret_key = "i almost forgot my secret key"

@app.route('/')
def dojo_survey():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('results.html')

@app.route('/process', methods=['POST'])
def data():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments'] 
    return redirect('/result')

if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 8000)

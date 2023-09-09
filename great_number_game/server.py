from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)

app.secret_key = 'This is my secret key'

@app.route('/')
def number_game():
    if 'number' not in session:
        session['number'] = random.randint(1,100)
    session['hard_mode'] = request.form.get('hard')

    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if request.form['guess'] is not '':
        counter()
        session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

def counter():
    if 'amount' not in session:
        session['amount'] = 1
    else:
        session['amount'] +=1




if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 8000)

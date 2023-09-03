from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "this is my secret key"

@app.route('/')
def counter():
    if 'amount' not in session:
        session['amount'] = 0
    else:
        session['amount'] +=1
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_count')
def add_two():
    session['amount'] +=2
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, host= 'localhost', port = 8000)
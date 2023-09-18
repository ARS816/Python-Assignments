from flask import Flask, render_template, session,redirect, request
import random

app = Flask(__name__)

app.secret_key = 'Butterfly leaf'

@app.route('/')
def ninja_gold():
    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():
    if 'gold' not in session:
        session['gold'] = 0
    else:
        if request.form['building'] == 'farm':
                session['new_gold'] = random.randint(10,20)
                session['gold'] += session['new_gold']
        elif request.form['building'] == 'cave':
                session['new_gold'] = random.randint(5,10)
                session['gold'] += session['new_gold']
        elif request.form['building'] == 'house':
                session['new_gold'] = random.randint(2,5)
                session['gold'] += session['new_gold']
        elif request.form['building'] == 'casino':
                session['new_gold'] = random.randint(-50,50)
                session['gold'] += session['new_gold']
        return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    session['gold']=0
    return redirect('/')

def counter():
    if 'amount' not in session:
        session['amount'] = 1
    else:
        session['amount'] +=1


if __name__ == '__main__':
    app.run(debug = True, host = 'localhost', port = 8000)


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('index.html', size = 8)

@app.route('/<int:size>')
def custom_size1(size):
    return render_template('index.html', size = size)

if __name__=="__main__":    
    app.run(debug=True, host="localhost", port=8000)


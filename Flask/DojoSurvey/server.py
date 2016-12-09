from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'alsdfkj'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    print request.form
    print request.form['locations']
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['fav_language'] = request.form['fav_language']
    session['comments'] = request.form['comments']
    return redirect ('/result')

@app.route('/result')
def show_result():
    return render_template('result.html')
app.run(debug=True)

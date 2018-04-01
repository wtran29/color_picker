from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_color():
	print "Got Color Info"
	red = request.form['red']
	green = request.form['green']
	blue = request.form['blue']
	print request.form

	
	return render_template('index.html', red = request.form['red'], green = request.form['green'], blue = request.form['blue'])

app.run(debug=True)
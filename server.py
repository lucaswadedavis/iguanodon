import uuid
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/message')
def messages():
	return jsonify({
        'id': uuid.uuid4(),
        'message': 'Official Iguanodon Message'
        })

@app.route('/message/<message>')
def message(message):
    return jsonify({
        'id': uuid.uuid4(),
        'message': message
        })

if __name__ == '__main__':
    app.run()


from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
	return "hello"

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5005))
	app.run(port=port, debug=True)

from flask import Flask
import os # (1) Library for os calls

PORT=os.getenv('PORT',8080) #(2) get env
app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<p>Hello, Raymond!</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)

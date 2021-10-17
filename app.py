from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/description', methods=['POST'])
def get_n_recommendations():
    request_post = request.json
    request_description = request_post["keywords"]



    return jsonify()


if __name__ == '__main__':
    app.run()

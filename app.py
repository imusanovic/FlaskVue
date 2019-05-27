from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/test', methods=['GET'])
def test():
    user = {
        'ime': 'Pero',
        'prezime': 'Peric',
        'adresa': {'ulica': 'Kruzna', 'broj': 7, 'grad': 'Rijeka'},
        'mobitel': '0981234567'
    }

    return jsonify(user)


if __name__ == '__main__':
    app.run()

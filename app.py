from flask import Flask, jsonify, request
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


# CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# testing data
users = [
    {
        'ime': 'Pero',
        'prezime': 'Peric',
        'adresa': {'ulica': 'Kruzna', 'broj': 7, 'grad': 'Rijeka'},
        'mobitel': '0981234567'
    },
    {
        'ime': 'Ivo',
        'prezime': 'Ivic',
        'adresa': {'ulica': 'Kvadratna', 'broj': 3, 'grad': 'Pula'},
        'mobitel': '0957654321'
    }
]


@app.route('/users', methods=['GET', 'POST'])
def all_users():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        adresa = post_data.get('adresa')
        user = {
            'ime': post_data.get('ime'),
            'prezime': post_data.get('prezime'),
            'adresa': adresa,
            'mobitel': post_data.get('mobitel')
        }
        users.append(user)
        response_object['users'] = users
    else:
        response_object['users'] = users
        response_object['status'] = 'failure'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()

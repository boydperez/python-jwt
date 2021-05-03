import jwt
import datetime
from flask import Flask, jsonify, request, make_response


# Instantiate flask app
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'


@app.route('/')
def index():
    return """<h3>Available endpoints</h3>
        <ul>
            <li><a href="/authenticate">/authenticate</a></li> 
            <li><a href="/public">/public</a></li> 
            <li><a href="/private">/private</a></li> 
        </ul>
    """


@app.route('/authenticate')
def login():
    # Basic access authentication 
    if request.authorization:
        if request.authorization.username == 'username' and request.authorization.password == 'password':
            token = jwt.encode({'user': request.authorization.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')

            return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/private')
def protected():
    token = request.args.get('token')  # http:///127.0.0.1:5000/route?token=[token]

    # Check if query string 'token' exists
    if not token:
        return jsonify({'message': "Token is missing"}), 403

    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        print(data)
    except:
        return jsonify({'message': "Invalid token"}), 403
    return jsonify({'message': "Token is valid"})


@app.route('/public')
def unprotected():
    return jsonify({'message': "Open to the public"})


if __name__ == '__main__':
    app.run(debug=True)

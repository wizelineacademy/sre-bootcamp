from flask import Flask
from flask import jsonify
from flask import request
from methods import Token, Restricted, SHA512
import os
from mysql.connector import connect, Error

app = Flask(__name__)
login = Token()
protected = Restricted()
sha512 = SHA512()

# Just a health check
@app.route("/")
def url_root():
    return "OK"

# Just a health check
@app.route("/_health")
def url_health():
    return "OK"

# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form['username']
    password = request.form['password']

    try:
        with connect(
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASS"),
            database=os.environ.get("DB_NAME")
        ) as connection:
            db_query = "SELECT * FROM users WHERE username = '%s'" % (username)
            with connection.cursor() as cursor:
                cursor.execute(db_query)
                result = cursor.fetchone()
                if sha512.verify(result[1], password, result[2]):
                    res = { "token": login.generate_token(username) }
                    return res, 200
                else:
                    res = { "msg": "Forbidden" }
                    return res, 403
    except Error as e:
        print(e)
        return "Error when tryign to connect to DB"
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')
    auth_token = auth_token.replace('Bearer ', '')
    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

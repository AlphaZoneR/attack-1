import flask

if __name__ == '__main__':
    app = flask.Flask(__name__)
    app.secret_key = input('secret key: ')
    session_interface = flask.sessions.SecureCookieSessionInterface()
    serializer = session_interface.get_signing_serializer(app)
    email = input('user email: ')
    print(serializer.dumps({"user": {"email": email, "permissions": "admin"}}))
#! /usr/bin/env python

# See https://pythonhosted.org/Flask-JWT/

# This also doesn't work by default because Flask-JWT doesn't support RSA tokens.
# See https://ai-facets.org/how-to-use-rs256-tokens-with-flask-jwt/

import logging

from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update({
    'TESTING': True,
    'DEBUG': True,
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    'JWT_ALGORITHM': 'RS256',
    'JWT_VERIFY': False,    # TODO
    'JWT_REQUIRED_CLAIMS': ['exp', 'iat']
})


def authenticate(username, password):
    return None


def identity(payload):
    return payload


jwt = JWT(app, authenticate, identity)


@app.route("/whoami")
@jwt_required()
def whoami():
    return '%s' % current_identity

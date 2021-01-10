#! /usr/bin/env python

# See: https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/

# Looks like RS256 is not supported :(

import json
import logging

from flask import Flask
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update({
    'TESTING': True,
    'DEBUG': True,
    'JWT_ALGORITHM': 'RS256',
    'JWT_PUBLIC_KEY': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlIMeXCeQJ3lzYrcMA1b/rhDO/QcR7VH0A+VWrcRglp9E9JabzGKyHTwiZHqFOwIhCGCsCSO1EOOCe+/kjjojTdS5fi8eTY7XCL0yFcJTzWWSMiZWq42pMMFGpIz7piaBTKr7DFYt4kN4zTfGlC140W7zyCqLM3QGK7Pfgtlstof1zA6urjNWDzTDqvfQvUEwX/kfnrSOBC2+9aIcv2dYz9BXbvhdstEn9k3fLfrG6ZD+FwhLWm1suq80SUHtmf6Iz/F8245ieSU0YN2QObYjAoiwruD5KXUikJQcqeZK1jAGTSqSxtXnvuN6M/Qq52Nu2lSKCE7AJaaf9EuDkJ3PJwIDAQAB'  # TODO: download it from Keycloak
})
jwt = JWTManager(app)


@app.route("/whoami")
@jwt_required
def whoami():
    current_user = get_jwt_identity()
    return json.dumps(current_user)

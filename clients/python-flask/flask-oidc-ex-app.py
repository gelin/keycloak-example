#! /usr/bin/env python

# See: https://github.com/larsw/flask-oidc-ex/blob/master/examples/api.py

# This example is not working.
# Because by default the nbf claim in the token is required
# when the JWT is verified by the python-jwt lib,
# but the claim not provided by Keycloak (https://lists.jboss.org/pipermail/keycloak-user/2019-January/017014.html)
# and it's not possible to configure the behavior in flast-oidc-ex.

import json
import logging

from flask import Flask
from flask_oidc_ex import OpenIDConnect

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config.update({
    'TESTING': True,
    'DEBUG': True,
    'OIDC_PROVIDER': 'http://keycloak:8080/auth/realms/example',
    'OIDC_RESOURCE_SERVER_ONLY': True,
    'OIDC_RESOURCE_SERVER_VALIDATION_MODE': 'offline',
    'OIDC_USER_INFO_ENABLED': False,
    'JWT_REQUIRED_CLAIMS': ['exp', 'iat']
})
oidc = OpenIDConnect(app)


@app.route("/whoami")
@oidc.accept_token(require_token=True)
def whoami():
    info = oidc.user_getinfo(['email', 'given_name', 'family_name'])
    return json.dumps(info)

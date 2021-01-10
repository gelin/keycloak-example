#! /usr/bin/env python

# See: https://flask-oidc2.readthedocs.io/en/latest/

# This OIDC implementation supports Google+ and Ipsilon, but not Keycloak directly.
# So, it's not configured easily for Keycloak.

import json
import logging

from flask import Flask, g
from flask_oidc import OpenIDConnect

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update({
    'TESTING': True,
    'DEBUG': True,
    'OIDC_PROVIDER': 'http://keycloak:8080/auth/realms/example',
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_RESOURCE_SERVER_ONLY': True,
    'OIDC_USER_INFO_ENABLED': False,
})
oidc = OpenIDConnect(app)


@app.route("/whoami")
@oidc.accept_token()
def whoami():
    return json.dumps(g.oidc_token_info)

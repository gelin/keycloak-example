#! /usr/bin/env python

import logging
import re

from flask import Flask, request, jsonify

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config.update({
    'TESTING': True,
    'DEBUG': True,
})


@app.route("/whoami")
def whoami():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        m = re.fullmatch(r'Bearer\s+(?P<token>\S+)', auth_header)
        if m:
            token = m.group('token')
            return jsonify(token=token), 200
    return "Unauthorized", 401

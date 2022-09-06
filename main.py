import os

from flask import Flask
from flask import request
from hvac import Client


VAULT_ADDR = os.getenv("VAULT_ADDR", "http://127.0.0.1:8200")
NOMAD_ROLE = os.getenv("NOMAD_ROLE", "admin")


app = Flask(__name__)


@app.route('/')
def root():
    # TODO: Render a basic page that checks for existance of token in local storage and displays form
    return f"""
<html>
<body>
<a href="/login">Login</a>
</form>
</html>
"""


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return f"""
<html>
<body>
<form action="/login" method="POST">
Username <input type="text" name="username"/>
Password <input type="password" name="password"/>
<input type="submit" value="Submit"/>
</form>
</html>
"""
    elif request.method == "POST":
        client = Client(VAULT_ADDR)
        username, password = request.form["username"], request.form["password"]
        client.auth_userpass(username, password)
        assert client.is_authenticated()
        nomad_creds = client.read(f"nomad/creds/{NOMAD_ROLE}")
        nomad_token = nomad_creds["data"]["secret_id"]
        return f"""
<html><head>
<script>localStorage.setItem("nomadTokenSecret", "{nomad_token}");</script>
</head>
<body>Logged in. Go back now.</body></html>
"""


app.run(host="0.0.0.0", port=5000)

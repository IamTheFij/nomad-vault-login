import os

from flask import Flask
from flask import request
from hvac import Client


BIND_HOST = os.getenv("BIND_HOST", "0.0.0.0")
BIND_PORT = int(os.getenv("BIND_PORT", "5000"))

VAULT_ADDR = os.getenv("VAULT_ADDR", "http://127.0.0.1:8200")
NOMAD_ROLE = os.getenv("NOMAD_ROLE", "admin")


app = Flask(__name__)


@app.route("/")
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
<p>Username <input type="text" name="username"/></p>
<p>Password <input type="password" name="password"/></p>
<p>Role <input type="text" name="role" value="admin"/></p>
<p><input type="submit" value="Submit"/></p>
</form>
</html>
"""
    elif request.method == "POST":
        client = Client(VAULT_ADDR)
        username, password = request.form["username"], request.form["password"]
        client.auth.userpass.login(username, password)
        assert client.is_authenticated()

        role = request.form.get("role")
        nomad_creds = client.read(f"nomad/creds/{role or NOMAD_ROLE}")
        nomad_token = nomad_creds["data"]["secret_id"]
        return f"""
<html><head>
<script>localStorage.setItem("nomadTokenSecret", "{nomad_token}"); window.location.replace("/ui/settings/tokens");</script>
</head>
<body>Logged in. Go <a href="/ui/settings/tokens">back to Nomad</a></body></html>
"""


app.run(host=BIND_HOST, port=BIND_PORT)

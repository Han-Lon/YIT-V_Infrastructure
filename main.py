from flask import Flask
from flask import Response
server = Flask(__name__)


@server.route('/', defaults={'path': ''})
@server.route('/<path:path>')
def hello(path):
    # Prints the path after https://<url>/...
    # Used for retrieving the OAuth Verifier value in Twitter's 3 legged OAuth handshake
    print(path)
    resp = Response(status=200)
    return resp


if __name__ == "__main__":
    server.run(host='0.0.0.0')


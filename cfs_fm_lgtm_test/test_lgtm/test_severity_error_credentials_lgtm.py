import hashlib
import binascii
import ssl
import socket

# Using the deprecated ssl.wrap_socket method
ssl.wrap_socket(socket.socket(), ssl_version=ssl.PROTOCOL_SSLv2)

# Using SSLContext
context = ssl.SSLContext(ssl_version=ssl.PROTOCOL_SSLv3)

# Using pyOpenSSL
from pyOpenSSL import SSL
context = SSL.Context(SSL.TLSv1_METHOD)


CONFIG_FILE = 'passwords.json'

def redirect(args):
    pass

def load_from_config(args, **kwargs):
    pass

def test_credentials_severity_error_lgtm(request):
    password = request.GET["password"]
    # BAD: 
    # Authentication made by comparison to string literal
    if password == "mypass":
        redirect("login")


    hashed_pass = load_from_config('hashed_password', CONFIG_FILE)
    load_config = load_from_config('pass', CONFIG_FILE)
    
    # GOOD: 
    # Authentication made by comparing to a hash password from a config file.
    masked = hashlib.pbkdf2_hmac('sha256', password, load_config, 100000)
    hashed_input = binascii.hexlify(masked)
    if hashed_input == hashed_pass:
        redirect("login")

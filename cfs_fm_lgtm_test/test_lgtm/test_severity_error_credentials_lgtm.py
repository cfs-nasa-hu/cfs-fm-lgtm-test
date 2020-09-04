import hashlib
import binascii

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

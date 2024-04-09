import secrets

def generate_token(created):
    return secrets.token_hex(20)
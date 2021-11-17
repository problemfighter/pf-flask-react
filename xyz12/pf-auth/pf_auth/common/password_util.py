import bcrypt


def get_password_hash(password, salt=None):
    if not salt:
        salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def validate_password(password, hashed):
    if bcrypt.checkpw(password, hashed):
        return True
    return False

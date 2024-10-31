import hashlib


def read(file):
    with open(file, "r") as file:
        return [line.strip() for line in file]


def hash_pass(password):
    return hashlib.sha1(password.encode()).hexdigest()


def crack_sha1_hash(hash, use_salts = False):

    for password in read("top-10000-passwords.txt"):
        for salt in read("known-salts.txt"):
            for salted_password in [password + salt, salt + password, password]:
                if hash_pass(salted_password) == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"















    return True
import hashlib

with open("server_password.txt", "r") as f:
    password = f.readline().strip()

with open("server_password.txt", "w") as f:
    p = hashlib.sha384()
    p.update(f'{password}'.encode('utf-8'))
    f.write(p.hexdigest())
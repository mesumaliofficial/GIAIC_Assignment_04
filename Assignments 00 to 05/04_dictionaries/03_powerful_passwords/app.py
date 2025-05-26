import hashlib

def hash_safe(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_check):
    store_logins = {
        "syedmesumjaffary@gmail.com": "f70ba2d931a78cb8020c84e55fd751a0068c20e93409b2d75a158cb35ce92895",  # 
        "dabang@gmail.com": "e6a267bb0bf98f350b61acc90e178761c32d17190be8ecd6b14111020b05886f",           # mango220
        "davidlaid@gmail.com": "187f10ab3650b8b817e4622632bf78ccc1ffda68863950c5cdd550500c311a1d"          # strawberry200
    }

    if email in store_logins and store_logins[email] == hash_safe(password_check):
        return True
    else:
        return False

print(login("dabang@gmail.com", "mango220"))  # ✅ Output: True
print(login("dabang@gmail.com", "wrongpass"))  # ❌ Output: False

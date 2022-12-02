import secrets
import string

def CreatePass():
    extra = '#!¡?¿=/&~'
    palabras = string.ascii_letters + string.digits + extra
    password = ''.join(secrets.choice(palabras) for i in range(32))
    return password

print(CreatePass())
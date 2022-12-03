import secrets
import string

def CreatePass():
    extra = '#!¡?¿=/&~' # You can also add here string.punctuation (It'll use everything)
    strings_used = string.ascii_letters + string.digits + extra
    password = ''.join(secrets.choice(strings_used) for i in range(32)) # You can change this number so you can have the lenght you desire
    return password

print(CreatePass())

import string
import secrets
def created_password(long):
    todo_caracteres = string.ascii_letters + string.digits + string.punctuation
    password=""
    for _ in range (long):
        password += secrets.choice(todo_caracteres)
        return password
    new_password = created_password(input("Wrrite a number of length password"))
    print(new_password)
        
        
    




import string
import secrets

def created_password(long):
    todo_caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(long):
        password += secrets.choice(todo_caracteres)

    return password

while True:
    new_password = created_password(int(input("Provide a number of character in your password=>")))
    print(new_password)
    keep_password = input("Do you want to keep this password? (yes/no)=>")
    if keep_password.lower() == 'yes' or "y":
        break

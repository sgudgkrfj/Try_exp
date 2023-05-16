#1
"""class  InvalidFileFormatError(Exception):
    def __init__(self, username):
        self.username=username

#InvalidLengthError
#InvalidCharacterError



def register_user(username):
    if len(username)<5:
        raise InvalidFileFormatError(username)
    else:
        print("Вас зарегано! ")
#приклад використання
try:
    username=input("Введіть імя користувача: ")
    register_user(username)
except InvalidFileFormatError as e:
    print(f"Неправельне ім'я користувача {e.username} "
          f"мінімум 5 символів")




#2
class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password=password

def validete_password(password):
    g=0
    for i in password:
        if i.isnumeric():
            g+=1
    if g==0 and len(password)<8:
        raise InvalidPasswordError(password)
    else:
        print("Вас зареганоyy!")

try:
    password=input("Введіть пароль: ")
    validete_password(password)
except InvalidPasswordError as r:
    print(f"Неправильно введений пароль {r.password}")

#3"""
class InvalidFileFormatError(Exception):
    def __init__(self,f):
        self.f=f

def read_file(f):
    try:
        with open(f,"r") as file:
            content = file.read()
            print("Вміст файлу:", content)
    except IOError:
        raise InvalidFileFormatError(f)

try:
    read_file(input("Введіть назву файлу:"))
except InvalidFileFormatError as e:
   print(f"Невірний формат файлу {e.f}")








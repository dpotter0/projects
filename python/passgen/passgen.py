import string
import secrets
import uuid

print ("\n\nThanks for checking out Dan's super cool password generator.\n  This has been built to refresh myself on python concepts.\n\nI hope you enjoy.\n\n")

numOfPws = int(input("Enter number of passwords to generate:    "))
numOfTok = int(input("Enter number of API tokens to generate:    "))
numOfUuid = int(input("Enter number of UUIDs to generate:    "))

print ("Ok. Here are " + str(numOfPws) + " passwords for you")

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(string.punctuation)

    for i in range(6):
        password += secrets.choice(randomSource)

    passwordList = list(password)
    secrets.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

for i in range(0, numOfPws):
    print ("Password " + str(i) + ": ", randomPassword())

for i in range(0, numOfTok):
    print ("API Token " + str(i) + ": ", secrets.token_hex(32))

for i in range(0, numOfUuid):
    stringId  = uuid.uuid4()
    print ("UUID " + str(i) + ": ",  stringId)
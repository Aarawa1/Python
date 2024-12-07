import random
import string

def generatePassword():
  length = random.randint(8, 30)
  password = [
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits)
  ]

  all_characters = string.ascii_letters + string.digits
  while len(password) < length:
    password.append(random.choice(all_characters))

  random.shuffle(password)

  return ''.join(password)

def main():
  password = generatePassword()

  print("Generiertes Passwort:", password)


main()
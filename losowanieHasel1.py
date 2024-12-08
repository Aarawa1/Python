import random


def qwertzu():
  length = int(input("Lenght of pass: "))
  if length < 8:
    return "Blad"

  list = [
    chr(random.randint(65, 90)),  # Duze litery
    chr(random.randint(97, 122)),  # male litery
    chr(random.randint(48, 57))  # cyfry
  ]

  for i in range(length - len(list)):
    randomNr = random.randint(0, 2)

    if randomNr == 0:
      list.append(chr(random.randint(65, 90)))
    elif randomNr == 1:
      list.append(chr(random.randint(97, 122)))
    elif randomNr == 2:
      list.append(chr(random.randint(48, 57)))

  newPasswort = ''.join(list)
  print(newPasswort)

qwertzu()
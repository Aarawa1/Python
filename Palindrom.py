#def checkPalindrom(word):
  #return word == word[::-1]

def checkPalindrom(word):
  word = word.lower()

  length = len(word) # dlugosc slowa

  for i in range(length // 2):  # Tylko do polowy danego slowa sprawdzamy
    firstCharacter = word[i] # idzie od przodu po kolei od 0, 1, 2.. do polowy slowa
    secondCharacter = word[length - i - 1] # idzie od tylu 6, 5, 4... az do polowy

    if word[i] != word[length - i - 1]:
      return False

  return True

def main():
  play = True
  print("Slowo, albo q jesli koniec programu")

  while(play): # while petla - dziala tak dluga dopoki uzytkownik nie wpisze "q"
    userInput = str(input())

    if(userInput == "q"):
      play = False
    else:
      if checkPalindrom(userInput): # sprawdzanie co zwroci checkPalindrom()
        print(f"'{userInput}' jest palindromem!")
      else:
        print(f"'{userInput}' nie jest palindromem.")

main()
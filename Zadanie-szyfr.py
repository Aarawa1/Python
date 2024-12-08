def getAlphabet():
  alphabet_mapping = (
    ("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4),
    ("F", 5), ("G", 6), ("H", 7), ("I", 8), ("J", 9),
    ("K", 10), ("L", 11), ("M", 12), ("N", 13), ("O", 14),
    ("P", 15), ("Q", 16), ("R", 17), ("S", 18), ("T", 19),
    ("U", 20), ("V", 21), ("W", 22), ("X", 23), ("Y", 24), ("Z", 25)
  )
  return alphabet_mapping

def szyfrowanie(text, key):
  charTextList = [50 if char == " " else char for char in text] # 50 as space
  mappedAlphabet = getAlphabet()

  letters = [pair[0].lower() for pair in mappedAlphabet] # 1 elementy z tupel, ale pisane malymi literami
  keyMapped = getKeyMapping(key)

  # petla do wypisania liter w naszym zdaniu jako liczby
  charsAsNumbers = []
  for oneChar in charTextList:
    if oneChar in letters:
      charsAsNumbers.append(letters.index(oneChar))
    elif oneChar == 50:
      charsAsNumbers.append(50)
    else:
      return "Letter is not in the alphabet"

  newText = []
  maxValue = len(letters)
  for i in range(len(charsAsNumbers)):
    if charsAsNumbers[i] == 50:
      newText.append(50)
      continue

    keyNumber = keyMapped[i % len(keyMapped)] # jesli key ma dlugosc 3, to wartosci 0, 1, 2, 0, 1, 2...
    textNumber = charsAsNumbers[i]
    sum = keyNumber + textNumber
    newNumber = sum if sum < maxValue else sum % len(letters)

    newText.append(newNumber)

  stringList = mapToCharacters(newText)
  return stringList


def mapToCharacters(numberList):
  mappedAlphabet = getAlphabet()
  letters = [pair[0].lower() for pair in mappedAlphabet]

  result = []
  for num in numberList:
    if num == 50:
      result.append(" ")
    else:
      result.append(letters[num])

  return ''.join(result)


def getKeyMapping(key):
  charKeyList = [char for char in key] # rozkladanie slow w kluczu na pojedyncze litery
  mappedAlp = getAlphabet()
  letters = [pair[0].lower() for pair in mappedAlp]

  keyMapped = []
  for oneChar in charKeyList:
    if oneChar in letters:
      keyMapped.append(letters.index(oneChar))
    else:
      return "Letter is not in the alphabet"

  return keyMapped


def main():
  text = input("Give text: ")
  key = input("Key (without spaces): ") ## key must be shorter than text

  newWord = szyfrowanie(text, key)
  print(newWord.upper())

main()

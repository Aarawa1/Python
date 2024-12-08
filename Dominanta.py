def checkForDominantaInList(list):
  allCharactersList = [] # [(liczba, ileRazWystapila)]

  for char in list:
    amount = checkIfInTupelAndReturnAmount(allCharactersList, char)

    if amount != 0:
      for i, tup in enumerate(allCharactersList): # i - ile razy liczba wystepuje w liscie
        if tup[0] == char:
          allCharactersList[i] = (char, tup[1] + 1)
          break
    else:
      allCharactersList.append((char, 1))

  return getDominanta(allCharactersList)

def checkIfInTupelAndReturnAmount(list, char):
  firstElementsList = [pair[0] for pair in list]

  for i in range(len(firstElementsList)):
    if char == firstElementsList[i]:
      return firstElementsList[i]
  return 0

def getDominanta(allCharactersList):
  frequencies = [tup[1] for tup in allCharactersList]
  max_frequency = max(frequencies)

  count_max_frequency = frequencies.count(max_frequency)
  if count_max_frequency > 1:
    return "Nie ma dominanty"

  dominant_char = max(allCharactersList, key=lambda x: x[1])  # key - czyli jaka wartosc bedzie sprawdzana
  return f"Dominante: {dominant_char[0]} mit {dominant_char[1]} Vorkommen"

def main():
  list = (1, 1, 1, 1, 4, 2, 5, 6, 3, 5, 5, 5, 5)
  print(checkForDominantaInList(list))

main()
def checkForDominantaInList(list):
  allCharactersList = []

  for char in list:
    amount = checkIfInTupelAndReturnAmount(allCharactersList, char)
    if amount != 0:
      for i, tup in enumerate(allCharactersList):
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
  dominant_char = max(allCharactersList, key=lambda x: x[1])
  return (f"Dominante: {dominant_char[0]} mit {dominant_char[1]} Vorkommen")

def main():
  list = (1, 1, 1, 4, 2, 5, 6, 3, 5, 5, 5, 5)
  print(checkForDominantaInList(list))

main()
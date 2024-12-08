import random

def generateLists():
  bigList = []

  for _ in range(100):
    bigList.append((random.randint(31, 62), (random.randint(31, 62))))

  return bigList

def convertToAscii(bigList):
  resultString = ""

  for pair in bigList:
    total = pair[0] + pair[1]
    if total <= 91 and total >= 65:
      resultString += chr(total)

  return resultString

def main():
  bigList = generateLists()
  resultString = convertToAscii(bigList)

  # Output results
  print(f"Generated string: {resultString}")
  print(f"Length of the string: {len(resultString)}")

main()
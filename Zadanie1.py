import random

def createList():
  list = []

  itemsAmount = random.randint(1, 20)
  for _ in range(itemsAmount):
    list.append(random.randint(1, 20))

  return list

def checkList(list):
  if len(list) < 2: return True

  difference = list[0] - list[1]
  for i in range(0, len(list) - 1):
    if abs(list[i] - list[i+1]) != difference:
      return False
  return True

def main():
  validLists = []
  totalValids = 0

  for x in range(100):
    list = createList()
    isValid = checkList(list)
    if(isValid):
      totalValids += 1
      validLists.append(list)

  print("Anzahl der Listen mit korrekter Sequenz: {totalValids}")
  print("Korrekte Listen:")
  for valid in validLists:
    print(valid)

main()
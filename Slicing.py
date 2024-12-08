import random

def createList():
  list = []

  itemsAmount = random.randint(1, 20) # randomowe wybieranie ile elementow ma ta lista posiadac
  for _ in range(itemsAmount): # petla, od 0 do randomowo wybranej dlugosci
    list.append(random.randint(1, 20))

  return list

def calculateSumOfSlicedElements(random_list):
  if len(random_list) < 6:
    return "Za krotka lista"

  first_three = random_list[:3]
  last_three = random_list[-3:]
  return sum(first_three) + sum(last_three)


def main():
  # Generiere eine zufällige Liste
  random_list = createList()
  print(random_list)

  result = calculateSumOfSlicedElements(random_list)
  print("Suma pierwszych i ostatnich 3 elementow:", result)


main()

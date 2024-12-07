import random

#################################

def createGenotyp():
  list = ["A", "B", "C", "D", "E"]

  newGenotyp = list[0] + list[0] + "".join(createRandomTypes(list)) + list[1] + list[1]

  return newGenotyp

def createRandomTypes(list):
  newList = []

  while True:
    try:
      amount = int(input("Amount of genotypes, from 200 to 500: "))
      if 200 <= amount <= 500:
        break
      else:
        print("Please enter a number between 200 and 500.")
    except ValueError:
      print("Invalid input. Please enter a valid number.")

  for _ in range(amount):
    newList.append(list[random.randint(0, len(list) - 1)])

  return newList

def main():
  genotyp = createGenotyp()
  ##correct = checkGenotyp(genotyp)
  ##print(correct)

main()
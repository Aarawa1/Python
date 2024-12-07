def checkList(list):
  if not list: return "Blad danych"

  newList = []
  count = 1
  length = len(list)
  for i in range(0, len(list) - 1):
    if list[i] == list[i+1]:
      count+=1
    else:
      newList.append(count)
      newList.append(list[i])
      count = 1

  newList.append(count)
  newList.append(list[-1])

  return newList


list = []
secondList = [10, 10, 20, 30, 30, 50, 60, 60]
A = [1, 1, 3, 2, 2, 2, 1]

emptyList = checkList(list)
print(emptyList)

secList = checkList(secondList)
print(secList)

thirdList = checkList(A)
print(thirdList)
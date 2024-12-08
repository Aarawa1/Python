def removeDuplicates(input_list):
  unique_list = []

  for element in input_list:
    is_duplicate = False

    for unique_element in unique_list:
      if element == unique_element:
        is_duplicate = True
        break

    if not is_duplicate:
      unique_list.append(element)

  return unique_list

def main():
  example_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
  result = removeDuplicates(example_list)

  print("Oryginalna lista:", example_list)
  print("Lista bez duplikatów:", result)

main()
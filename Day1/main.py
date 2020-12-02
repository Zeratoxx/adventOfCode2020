
def search_two_correct_summands(list_of_numbers, goal):
    for i in range(0, len(list_of_numbers)):
        for j in range(i, len(list_of_numbers)):
            if list_of_numbers[i] + list_of_numbers[j] == goal:
                return [list_of_numbers[i], list_of_numbers[j]]

def search_three_correct_summands(list_of_numbers, goal):
    for i in range(0, len(list_of_numbers)):
        for j in range(i, len(list_of_numbers)):
            for k in range(j, len(list_of_numbers)):
                if list_of_numbers[i] + list_of_numbers[j] + list_of_numbers[k] == goal:
                    return [list_of_numbers[i], list_of_numbers[j], list_of_numbers[k]]

def search_summands(list_of_numbers, goal, number_of_summands=2):
    if number_of_summands == 2:
        return search_two_correct_summands(list_of_numbers, goal)
    elif number_of_summands == 3:
        return search_three_correct_summands(list_of_numbers, goal)
    else:
        return []

def get_product(list_of_numbers):
    result = 1
    for x in list_of_numbers:
        result = result * x
    return result

def run():
    with open('./data/input', "r") as inputFile:
        numbers = list(map(int, inputFile.read().splitlines()))

    correct_two_summands = search_summands(numbers, 2020, 2)
    product_of_two = get_product(correct_two_summands)
    print(correct_two_summands)
    print(product_of_two)

    correct_three_summands = search_summands(numbers, 2020, 3)
    product_of_three = get_product(correct_three_summands)
    print(correct_three_summands)
    print(product_of_three)

    with open('results.txt', 'w') as f:
        for item in correct_two_summands:
            f.write("%s, " % item)
        f.write("\n\n")
        f.write("%s" % product_of_two)
        f.write("\n\n\n\n")
        for item in correct_three_summands:
            f.write("%s, " % item)
        f.write("\n\n")
        f.write("%s" % product_of_three)


if __name__ == '__main__':
    run()

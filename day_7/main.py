from day_7.bag import Bag
from day_7.rule import Rule
from day_7.search_engine import search_for_bags_that_can_contain_given_bag_recursively, \
    get_amount_of_bags_that_given_bag_contains_recursively_start, complete_tree


def get_data(input_path):
    with open(input_path, "r") as inputFile:
        data = inputFile.read().splitlines()
    return data


def run():
    data = get_data("./data/input")
    rules = []
    for line in data:
        rules.append(Rule(line))

    print(f'data: {data}')
    print(f'last data entry: {data[-1]}')
    print(f'lenght: {len(data)}')
    print("")
    for rule in rules:
        print(rule.__str__())
    print(f'lenght: {len(rules)}')

    # print("")
    # print("")
    # valid_bags = search_for_bags_that_can_contain_given_bag_recursively(rules, [Bag("shiny", "gold")])
    # for bag in valid_bags:
    #     print(bag)
    # print("")
    # print(f'lenght: {len(valid_bags)}')

    print("")
    print("")
    sum_of_bags = get_amount_of_bags_that_given_bag_contains_recursively_start(rules, {Bag("shiny", "gold"): 1})
    for line in reversed(complete_tree):
        print(line)
    print(f'sum_of_bags: {sum_of_bags}')


def run2():
    data = get_data("./data/example")
    rules = []
    for line in data:
        rules.append(Rule(line))

    print(f'data: {data}')
    print(f'last data entry: {data[-1]}')
    print(f'lenght: {len(data)}')
    print("")
    for rule in rules:
        print(rule.__str__())
    print(f'lenght: {len(rules)}')

    # print("")
    # print("")
    # valid_bags = search_for_bags_that_can_contain_given_bag_recursively(rules, [Bag("shiny", "gold")])
    # for bag in valid_bags:
    #     print(bag)
    # print("")
    # print(f'lenght: {len(valid_bags)}')

    print("")
    print("")
    sum_of_bags = get_amount_of_bags_that_given_bag_contains_recursively_start(rules, {Bag("shiny", "gold"): 1})
    for line in reversed(complete_tree):
        print(line)
    print(f'sum_of_bags: {sum_of_bags}')


def run3():
    data = get_data("./data/example2")
    rules = []
    for line in data:
        rules.append(Rule(line))

    print(f'data: {data}')
    print(f'last data entry: {data[-1]}')
    print(f'lenght: {len(data)}')
    print("")
    for rule in rules:
        print(rule.__str__())
    print(f'lenght: {len(rules)}')

    # print("")
    # print("")
    # valid_bags = search_for_bags_that_can_contain_given_bag_recursively(rules, [Bag("shiny", "gold")])
    # for bag in valid_bags:
    #     print(bag)
    # print("")
    # print(f'lenght: {len(valid_bags)}')

    print("")
    print("")
    sum_of_bags = get_amount_of_bags_that_given_bag_contains_recursively_start(rules, {Bag("shiny", "gold"): 1})
    for line in reversed(complete_tree):
        print(line)
    print(f'sum_of_bags: {sum_of_bags}')


if __name__ == '__main__':
    run()
    # run2()
    # run3()

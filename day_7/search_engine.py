complete_tree = []


def search_for_bags_that_can_contain_given_bag_recursively(rules, searched_bags):
    valid_bags = []
    for rule in rules:
        for rule_rest in rule.rule_restrictions:
            if rule_rest.bag in searched_bags:
                if rule.bag not in valid_bags:
                    valid_bags.append(rule.bag)
                if rule.bag not in searched_bags:
                    searched_bags.append(rule.bag)
                    return search_for_bags_that_can_contain_given_bag_recursively(rules, searched_bags)
    return valid_bags


def get_amount_of_bags_that_given_bag_contains_recursively_start(rules, searched_bags_dict):
    rules_dict = {}
    for rule in rules:
        rules_dict[rule.bag] = rule.rule_restrictions

    complete_tree = []

    amount = get_amount_of_bags_that_given_bag_contains_recursively(rules_dict, searched_bags_dict, 0)
    for bag in searched_bags_dict:
        amount -= searched_bags_dict[bag]
    return amount


def get_amount_of_bags_that_given_bag_contains_recursively(rules_dict, searched_bags_dict, depth):
    tree_part = "|   "
    tree = ""
    amount = 0
    amount_next = 1
    amount_below = 0
    for bag in searched_bags_dict:
        for x in range(depth):
            tree += tree_part
        depth += 1
        if len(rules_dict[bag]) == 0:
            amount += searched_bags_dict[bag] * amount_next
        else:
            amount += searched_bags_dict[bag]
            for rule_rest in rules_dict[bag]:
                amount_next = get_amount_of_bags_that_given_bag_contains_recursively(
                    rules_dict,
                    {rule_rest.bag: rule_rest.amount},
                    depth
                )
                amount_below += amount_next
                amount += searched_bags_dict[bag] * amount_next
        if amount_below == 0:
            amount_below = 1
        complete_tree.append(tree + str(amount) + " = " + str(searched_bags_dict[bag]) + " + " +
                             str(searched_bags_dict[bag]) + " x " + str(amount_below) + " ; " + str(bag.__str__()))
    return amount

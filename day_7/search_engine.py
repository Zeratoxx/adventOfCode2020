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


def get_amount_of_bags_that_given_bag_contains_recursively(rules, searched_bags_dict):
    rules_dict = {}
    for rule in rules:
        rules_dict[rule.bag] = rule.rule_restrictions

    amount = 0
    for bag in searched_bags_dict:
        if len(rules_dict[bag]) == 0:
            amount += searched_bags_dict[bag] * 1
        else:
            for rule_rest in rules_dict[bag]:
                amount += searched_bags_dict[bag] * \
                          get_amount_of_bags_that_given_bag_contains_recursively(rules, {rule_rest.bag: rule_rest.amount})
    return amount

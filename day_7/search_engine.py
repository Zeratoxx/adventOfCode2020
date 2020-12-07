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

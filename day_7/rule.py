from day_7.bag import Bag
from day_7.rule_restriction import RuleRestriction


class Rule:
    def __init__(self, rule_directions):
        part_counter = 0
        word_counter = 0
        concerning_bag_color_shade = ""
        concerning_bag_color = ""

        self.rule_restrictions = []
        for part in rule_directions.split("contain"):
            if part_counter == 0:
                for word in part.split(" "):
                    if word_counter == 0:
                        concerning_bag_color_shade = word
                    if word_counter == 1:
                        concerning_bag_color = word
                    word_counter += 1
            if part_counter == 1:
                for sub_part in part.split(", "):
                    if sub_part.strip().split(" ")[0] != "no":
                        self.rule_restrictions.append(RuleRestriction(sub_part.strip()))
            part_counter += 1
        self.bag = Bag(concerning_bag_color_shade, concerning_bag_color)

    def __str__(self):
        string = f'{self.bag.shade} {self.bag.color} bags contain:\n'
        if 0 < len(self.rule_restrictions):
            for rule_rest in self.rule_restrictions:
                string += f'\t- {rule_rest.__str__()}\n'
        else:
            string += f'\t- no other bags\n'
        return string[:-1]

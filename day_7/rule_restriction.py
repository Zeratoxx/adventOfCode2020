import sys

from day_7.bag import Bag


class RuleRestriction:
    def __init__(self, rule_restriction):
        self.amount = 0
        color = ""
        color_shade = ""
        counter = 0
        for word in rule_restriction.split(" "):
            if counter == 0:
                try:
                    self.amount = int(word)
                except ValueError:
                    print(f'Error when converting string number to int number: {word}, type: {type(word)}',
                          file=sys.stderr)

            if counter == 1:
                color_shade = word
            if counter == 2:
                color = word
            counter += 1
        self.bag = Bag(color_shade, color)

    def __str__(self):
        string = f'{self.amount} {self.bag.shade} {self.bag.color} bag'
        if self.amount != 1:
            string += "s"
        return string

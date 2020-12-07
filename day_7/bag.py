class Bag:
    def __init__(self, shade, color):
        self.shade = shade
        self.color = color

    def __eq__(self, other):
        if hasattr(other, 'shade') and hasattr(other, 'color'):
            if self.shade == other.shade and self.color == other.color:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return f'{self.shade} {self.color}'

    def __hash__(self):
        return hash(self.shade + self.color)

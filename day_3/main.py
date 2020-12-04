
def get_data(input_path):
    with open(input_path, "r") as inputFile:
        tree_grid = inputFile.read().splitlines()
    return tree_grid


def count_trees(tree_grid, amount_right_move, amount_down_move=1):
    right_offset = 0
    tree_counter = 0
    for i in range(0, len(tree_grid), amount_down_move):
        tree_line = tree_grid[i]
        if tree_line[right_offset % len(tree_line)] == '#':
            tree_counter += 1
        right_offset += amount_right_move
    return tree_counter


def task_second_half(tree_grid):
    product = 1
    product *= count_trees(tree_grid, 1)
    product *= count_trees(tree_grid, 3)
    product *= count_trees(tree_grid, 5)
    product *= count_trees(tree_grid, 7)
    product *= count_trees(tree_grid, 1, amount_down_move=2)

    return product


def run():
    tree_grid = get_data("./data/input")
    encountered_trees = count_trees(tree_grid, 3)
    product = task_second_half(tree_grid)
    print("encountered trees for 3 right and 1 down: %s" % encountered_trees)
    print("product of encountered trees: %s" % product)

    with open('results.txt', 'w') as f:
        f.write("encountered trees for 3 right and 1 down: %s\n" % encountered_trees)
        f.write("product of encountered trees: %s\n" % product)


if __name__ == '__main__':
    run()

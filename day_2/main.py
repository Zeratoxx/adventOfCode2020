
def get_data(input_path):
    with open(input_path, "r") as inputFile:
        policies_and_passwords = inputFile.read().splitlines()
    policies_and_passwords_changed = []
    for item in policies_and_passwords:
        first_split = item.split(":")
        second_split = first_split[0].split()
        third_split = second_split[0].split("-")
        policies_and_passwords_changed.append([
            [second_split[1], int(third_split[0]), int(third_split[1])],
            first_split[1][1:]
        ])
    return policies_and_passwords_changed


def run():
    policies_and_passwords = get_data("./data/input")
    for item in policies_and_passwords:
        searched_char = item[0][0]
        min = item[0][1]
        max = item[0][2]
        counter = 0
        for character in item[1]:
            if character == searched_char:
                counter += 1
            if (counter > max):
                break



if __name__ == '__main__':
    run()

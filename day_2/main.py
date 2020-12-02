
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


def password_is_valid_first(policy, password):
    searched_char = policy[0]
    min_count = policy[1]
    max_count = policy[2]
    counter = 0
    for character in password:
        if character == searched_char:
            counter += 1
        if counter > max_count:
            break
    return min_count <= counter <= max_count


def password_is_valid_second(policy, password):
    searched_char = policy[0]
    first_pos = policy[1] - 1
    second_pos = policy[2] - 1

    return (password[first_pos] == searched_char and password[second_pos] != searched_char) \
           or \
           (password[first_pos] != searched_char and password[second_pos] == searched_char)


def run():
    policies_and_passwords = get_data("./data/input")

    valid_passwords = []
    for item in policies_and_passwords:
        if password_is_valid_first(item[0], item[1]):
            valid_passwords.append(item)
    with open('results_first_half.txt', 'w') as f:
        for item in valid_passwords:
            f.write("%s\n" % item)
        f.write("\n\n")
        f.write("Number of valid passwords: %s\n" % len(valid_passwords))

    valid_passwords = []
    for item in policies_and_passwords:
        if password_is_valid_second(item[0], item[1]):
            valid_passwords.append(item)
    with open('results_second_half.txt', 'w') as f:
        for item in valid_passwords:
            f.write("%s\n" % item)
        f.write("\n\n")
        f.write("Number of valid passwords: %s\n" % len(valid_passwords))


if __name__ == '__main__':
    run()

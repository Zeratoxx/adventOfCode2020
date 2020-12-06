from day_6.group import Group


def get_data(input_path):
    data = []
    with open(input_path, "r") as inputFile:
        group = []
        is_added = False
        for line in inputFile.read().splitlines():
            if line == '':
                data.append(group)
                is_added = True
                group = []
            else:
                group.append(line)
                is_added = False
        if not is_added:
            data.append(group)
    return data


def run():
    data = get_data("./data/input")
    groups = []
    for group in data:
        groups.append(Group(group))

    answered_questions_from_groups = []
    sum_group_answers = 0
    for group in groups:
        answered_questions_from_groups.append(group.questions_anyone_answered_with_yes_in_group())
        sum_group_answers += len(answered_questions_from_groups[-1])

    answered_questions_from_groups_part_two = []
    sum_group_answers_part_two = 0
    for group in groups:
        answered_questions_from_groups_part_two.append(group.questions_everybody_answered_with_yes_in_group())
        sum_group_answers_part_two += len(answered_questions_from_groups_part_two[-1])

    print(f'data: {data}')
    print(f'last data entry: {data[-1]}')
    print(f'lenght: {len(data)}')

    print(f'groups: {groups}')
    print(f'last groups entry: {groups[-1].group_members}')
    print(f'lenght: {len(groups)}')

    print(f'group answers: {answered_questions_from_groups}')
    print(f'last group answers: {answered_questions_from_groups}')
    print(f'lenght: {len(answered_questions_from_groups)}')
    print(f'sum group answers: {sum_group_answers}')

    print(f'group answers: {answered_questions_from_groups_part_two}')
    print(f'last group answers: {answered_questions_from_groups_part_two}')
    print(f'lenght: {len(answered_questions_from_groups_part_two)}')
    print(f'sum group answers: {sum_group_answers_part_two}')

    with open('results.txt', 'w') as f:
        f.write(f'valid passports part one: {0} of {len([])}\n')
        f.write(f'valid passports part two: {0} of {len([])}')


if __name__ == '__main__':
    run()

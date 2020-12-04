import string


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


class Passport:
    hex_digits = set(string.hexdigits)
    valid_eye_colors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def __init__(
            self, password_information
    ):
        self.byr = password_information.get("byr")  # Birth Year
        self.iyr = password_information.get("iyr")  # Issue Year
        self.eyr = password_information.get("eyr")  # Expiration Year
        self.hgt = password_information.get("hgt")  # Height
        self.hcl = password_information.get("hcl")  # Hair Color
        self.ecl = password_information.get("ecl")  # Eye Color
        self.pid = password_information.get("pid")  # Passport ID
        self.cid = password_information.get("cid")  # Country ID

    def is_valid_first_part(self):
        is_valid = False
        if self.byr and self.iyr and self.eyr and self.hgt and \
                self.hcl and self.ecl and self.pid:
            is_valid = True
        return is_valid

    def is_valid_second_part(self):
        is_valid = self.is_valid_first_part()
        if is_valid:
            if self.byr.isnumeric():
                is_valid = is_valid and len(self.byr) == 4 and 1920 <= int(self.byr) <= 2002
            else:
                is_valid = is_valid and False

            if self.iyr.isnumeric():
                is_valid = is_valid and len(self.iyr) == 4 and 2010 <= int(self.iyr) <= 2020
            else:
                is_valid = is_valid and False

            if self.eyr.isnumeric():
                is_valid = is_valid and len(self.eyr) == 4 and 2020 <= int(self.eyr) <= 2030
            else:
                is_valid = is_valid and False

            if self.hgt[:-2].isnumeric():
                if self.hgt[-2:] == "cm":
                    is_valid = is_valid and 150 <= int(self.hgt[:-2]) <= 193
                elif self.hgt[-2:] == "in":
                    is_valid = is_valid and 59 <= int(self.hgt[:-2]) <= 76
                else:
                    is_valid = is_valid and False
            else:
                is_valid = is_valid and False

            if self.hcl[0] == "#":
                if len(self.hcl[1:]) == 6:
                    is_valid = is_valid and all(c in self.hex_digits for c in self.hcl[1:])
                else:
                    is_valid = is_valid and False
            else:
                is_valid = is_valid and False

            is_valid = is_valid and self.ecl in self.valid_eye_colors

            if self.pid.isnumeric():
                is_valid = is_valid and len(self.pid) == 9
            else:
                is_valid = is_valid and False

        return is_valid


def get_data(input_path):
    passports = []
    with open(input_path, "r") as inputFile:
        one_passport = []
        for line in inputFile.read().splitlines():
            if line == '':
                passports.append(sorted(one_passport, key=str.lower))
                one_passport = []
            else:
                for passport_info in line.split():
                    one_passport.append(passport_info)
    return passports


def parse_data_to_passports(data):
    passports = []
    for one_passport_data in data:
        passport_args = {}
        for one_passport_attribute in one_passport_data:
            replaced = one_passport_attribute.split(":")
            passport_args[replaced[0]] = replaced[1]
        passport_object = Passport(passport_args)
        passports.append(passport_object)

    return passports


def run():
    data = get_data("./data/input")
    passports = parse_data_to_passports(data)

    valid_count_one = 0
    for passport in passports:
        if passport.is_valid_first_part():
            valid_count_one += 1

    valid_count_two = 0
    for passport in passports:
        if passport.is_valid_second_part():
            valid_count_two += 1

    print(f'valid passports part one: {valid_count_one} of {len(passports)}')
    print(f'valid passports part two: {valid_count_two} of {len(passports)}')

    with open('results.txt', 'w') as f:
        f.write(f'valid passports part one: {valid_count_one} of {len(passports)}\n')
        f.write(f'valid passports part two: {valid_count_two} of {len(passports)}')


if __name__ == '__main__':
    run()

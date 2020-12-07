import re


def is_valid_passport(passport_dict):
    passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    required_passport_fields = passport_fields - {"cid"}
    if not (required_passport_fields.issubset(passport_dict.keys())):
        return False
    if not (1920 <= int(passport_dict["byr"]) <= 2002):
        return False
    if not (2010 <= int(passport_dict["iyr"]) <= 2020):
        return False
    if not (2020 <= int(passport_dict["eyr"]) <= 2030):
        return False
    try:
        _, height_val, height_unit, _ = re.split(
            r"(\d{2,3})(cm|in)", passport_dict["hgt"]
        )
    except ValueError:
        return False
    if height_unit == "cm" and int(height_val) not in range(150, 194):
        return False
    if height_unit == "in" and int(height_val) not in range(59, 77):
        return False
    valid_hair_color = re.match(r"(#)((\d|[a-f]){6})", passport_dict["hcl"])
    if not valid_hair_color:
        return False
    if passport_dict["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    if len(passport_dict["pid"]) != 9:
        return False
    return True


def solution(input_string):
    passport_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    required_passport_fields = passport_fields - {"cid"}
    potential_passport_strs = input_string.split("\n\n")
    potential_passport_dicts = [
        dict(map(lambda s: s.split(":"), potential_passport_str.split()))
        for potential_passport_str in potential_passport_strs
    ]

    return len([ppd for ppd in potential_passport_dicts if is_valid_passport(ppd)])


if __name__ == "__main__":
    with open("input.txt") as f:
        print(solution(f.read().strip()))

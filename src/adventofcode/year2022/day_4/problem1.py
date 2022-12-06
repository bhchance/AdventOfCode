import aocd


def solution(input_string):
    def sets_fully_overlap(set1, set2):
        return set1.issuperset(set2) or set1.issubset(set2)

    def pair_to_set(p):
        start, end = map(int, p.split("-"))
        return set(range(start, end + 1))

    pairs = (map(pair_to_set, pair.split(",")) for pair in input_string.splitlines())
    pairs_overlapping = filter(lambda p: sets_fully_overlap(*p), pairs)

    return len(list(pairs_overlapping))


if __name__ == "__main__":
    year, day, part = 2022, 4, 1
    submit = True
    answer = solution(aocd.get_data())

    if submit:
        aocd.submit(answer, year=year, day=day, part=part)
    print(answer)

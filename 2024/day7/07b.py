from itertools import product

datafolder = "data"
with open(f"{datafolder}/07", "r") as file:
    data = file.read()[:-1].split("\n")


def get_result_and_terms(line):
    return line.split(":")


def get_operations(terms, ops=["+", "*"]):
    return list(product(ops, repeat=(len(terms) - 1)))


def check_combinations(terms, permutations, target_result):
    for permutation in permutations:
        permutation = list(permutation)
        result = terms[0]
        for i in range(len(permutation)):
            result = terms[0]
            for i, op in enumerate(permutation):
                if op == "+":
                    result += terms[i + 1]
                elif op == "*":
                    result *= terms[i + 1]
                elif op == "||":
                    result = int(str(result) + str(terms[i + 1]))
                else:
                    raise ValueError("Operation must be either 'add', 'mul' or '||'")
        if result == target_result:
            return result

    return 0


def check_correct(line):
    split_line = get_result_and_terms(line)
    target_result = int(split_line[0])
    terms = list(map(int, split_line[1].split(" ")[1:]))

    permutations = get_operations(terms)
    result = check_combinations(terms, permutations, target_result)

    if result > 0:
        return result

    else:
        permutations = get_operations(terms, ops=["+", "*", "||"])
        result = check_combinations(terms, permutations, target_result)
        return result

    return 0


tot = 0

for line in data:
    result = check_correct(line)
    tot += result

print(tot)

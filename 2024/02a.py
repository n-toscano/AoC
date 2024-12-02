datafolder = "data"
with open(f"{datafolder}/2.txt", "r") as file:
    data = file.read()

tot = 0
for line in data[:-1].split("\n"):
    report = [int(level) for level in line.split(" ")]
    limit = False
    if any(sorted(report) == rep for rep in [report, report[::-1]]):
        # print(report, limit)
        report = sorted(report)
        level = report[0]
        for next_level in report[1:]:
            # print(level, next_level)
            if 1 <= (next_level - level) <= 3:
                limit = True
                level = next_level
            else:
                limit = False
                level = next_level
                break
        if limit:
            tot += 1
    if limit:
        print(report, limit)

print(tot)

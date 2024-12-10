datafolder = "data"
with open(f"{datafolder}/02", "r") as file:
    data = file.read()


def check_order(original_report, idx, limit):
    report = original_report.copy()
    if idx >= 0:
        report.pop(idx)
    if any(sorted(report) == rep for rep in [report, report[::-1]]):
        report = sorted(report)
        level = report[0]
        for next_level in report[1:]:
            if 1 <= (next_level - level) <= 3:
                limit = True
                level = next_level
            else:
                limit = False
                level = next_level
                break
    return limit


tot = 0
for line in data[:-1].split("\n"):
    original_report = [int(level) for level in line.split(" ")]
    limit = False
    for idx in range(-1, len(original_report)):
        limit = check_order(original_report, idx, limit)
        if limit:
            tot += 1
            break
print(tot)

datafolder = "data"
with open(f"{datafolder}/05", "r") as file:
    data = file.read()[:-1]


def check_next_pages(page, next_pages, couples):
    target_pages = [c[1] for c in couples if c[0] == page]
    forbidden_pages = [c[0] for c in couples if c[1] == page]
    return all(page in target_pages for page in next_pages) and set(
        forbidden_pages
    ).isdisjoint(set(next_pages))


def check_update(update, couples):
    for i, page in enumerate(update[:-1]):
        next_pages = update[i + 1 :]
        condition = check_next_pages(page, next_pages, couples)
        if not condition:
            break
    return condition


couples_list, updates_list = data.split("\n\n")
couples_str = [c.split("|") for c in couples_list.split("\n")]
updates_str = [u.split(",") for u in updates_list.split("\n")]
couples = [[int(page) for page in couple] for couple in couples_str]
updates = [[int(page) for page in update] for update in updates_str]

tot = 0
for update in updates:
    if check_update(update, couples):
        tot += update[int(len(update) / 2)]
print(tot)

data = open('day_5/data', 'r').read().splitlines()
rules = [[int(x) for x in line.split("|")] for line in data if len(line) == 5] #parse rules
pages = [[int(x) for x in line.split(",")] for line in data if len(line) > 5] #parse page orders


def is_in_right_order(x, y, rules):
    for (r_before, r_after) in rules:
        if x == r_before and y == r_after:
            return True
    return False

def is_reversed(x, y, rules):
    for (r_before, r_after) in rules:
        if y == r_before and x == r_after:
            return True
    return False

correct_page_order_indices = []
for k, page_order in enumerate(pages):
    correct_order = True
    for i in range(len(page_order)-1):
        for j in range(i+1, len(page_order)):
            if not is_in_right_order(page_order[i], page_order[j], rules):
                correct_order = False
                break
        
        if not correct_order:
            break
    
    if correct_order:
        correct_page_order_indices.append(k)

result = 0
for idx in correct_page_order_indices:
    result += pages[idx][(len(pages[idx])) // 2]

print("Part 1: ", result)

result2 = 0
for k, page_order in enumerate(pages):
    if k in correct_page_order_indices: continue

    for i in range(len(page_order)-1):
        for j in range(i+1, len(page_order)):
            if is_reversed(page_order[i], page_order[j], rules):
                page_order[i], page_order[j] = page_order[j], page_order[i]
        
    result2 += page_order[len(page_order) // 2]

print("Part 2: ", result2)
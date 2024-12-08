# Part 1 
data = [[int(x) for x in line.split(" ")] for line in open('day_2/data', 'r').read().splitlines()] #split lines and digits at spaces and convert to ints

def report_is_safe(report):
    return all((earlier - later >= 1 and earlier - later <= 3) for earlier, later in zip(report, report[1:])) or all((earlier - later <= -1 and earlier - later >= -3) for earlier, later in zip(report, report[1:]))

def dampen(report, position):
    return [x for i, x in enumerate(report) if i != position]

safe_reports = 0
for report in data:
    safe_reports += 1 if report_is_safe(report) else 0
print("Part 1: ", safe_reports)

safe_reports_dampening = 0
for report in data:    
    if report_is_safe(report):
        safe_reports_dampening += 1
    else:
        for i in range(len(report)):
            temp = dampen(report=report, position=i)
            if report_is_safe(temp):
                safe_reports_dampening += 1
                break
print("Part 2: ", safe_reports_dampening)
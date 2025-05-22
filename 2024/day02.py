from pathlib import Path

data = Path(__file__.replace(".py", ".in")).read_text().strip("\n").split("\n")


# return if a report is safe, also return the index of the first affending level if the report is not safe
def is_safe(report: list[int]) -> tuple[bool, int]:
    if len(report) <= 1:
        return True

    safe = True
    inc = report[0] < report[1]

    for i in range(len(report) - 1):
        if abs(report[i] - report[i + 1]) not in (1, 2, 3):
            safe = False
            break
        if (report[i] < report[i + 1]) != inc:
            safe = False
            break

    return (safe, i + 1)


# --- part 1 ---

safe_report = 0

for report in data:
    levels = [int(l) for l in report.split()]
    safe, _ = is_safe(levels)
    if safe:
        safe_report += 1

print(safe_report)

# --- part 2 ---

import copy

safe_report = 0

for report in data:
    levels = [int(l) for l in report.split()]
    safe, index = is_safe(levels)

    if safe:
        safe_report += 1
        continue

    # remove level at (index - 2) or (index - 1) or index and check safety again
    for i in (index - 2, index - 1, index):
        if i < 0:
            continue
        new_levels = copy.deepcopy(levels)
        del new_levels[i]

        safe, _ = is_safe(new_levels)

        if safe:
            break

    if safe:
        safe_report += 1
        continue

print(safe_report)

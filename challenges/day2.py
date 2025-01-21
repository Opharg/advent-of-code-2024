import get_input
get_input.get_input(2)

# input
reports = []
with open(r'./inputs/d2.txt', 'r') as file:
    for line in file:
        line = line.strip().split(' ')
        line = [int(x) for x in line]
        reports.append(line)


def safety_check(report):
    # 0: default, 1: increasing, 2: decreasing
    state = 0
    for i in range(len(report) - 1):
        if state == 0:
            if report[i] < report[i + 1]:
                state = 1
            else:
                state = 2

        if report[i] == report[i + 1]:
            break

        if (report[i] < report[i + 1] and state == 2) or abs(report[i] - report[i + 1]) > 3:
            return False
        if (report[i] > report[i + 1] and state == 1) or report[i] - report[i + 1] > 3:
            return False
    else:
        return True


# part 1
safe_count = 0
for report in reports:
    if safety_check(report):
        safe_count += 1
print(safe_count)

# part 2
tolerated_count = 0
for report in reports:
    if safety_check(report):
        tolerated_count += 1
    else:
        for i in range(len(report)):
            mock_report = [x for x in report]
            del mock_report[i]
            if safety_check(mock_report):
                # print('old', report)
                # print('new', mock_report)
                tolerated_count += 1
                break
print(tolerated_count)

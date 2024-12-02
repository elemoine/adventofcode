with open("input") as f_:
    rows = f_.readlines()

reports = [[int(e) for e in row.strip().split()] for row in rows]


def is_safe(report):
    asc = None
    for i in range(0, len(report) - 1):
        delta = report[i + 1] - report[i]
        dir_ = delta > 0
        if asc is None:
            asc = dir_
        if dir_ != asc:
            return False
        if delta == 0 or abs(delta) > 3:
            return False
    return True


def one_level_removed(report):
    for i in range(len(report)):
        related = report.copy()
        related.pop(i)
        yield related


cnt = 0
for report in reports:
    if is_safe(report):
        cnt += 1
    else:
        for other in one_level_removed(report):
            if is_safe(other):
                cnt += 1
                break


print(cnt)

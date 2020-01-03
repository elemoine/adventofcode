import re
import datetime
from collections import defaultdict


recordpattern = re.compile(r"\[(.*)\] (.*)")
guardbeginsshiftpattern = re.compile(r"Guard #(\d+) begins shift")
timeformat = "%Y-%m-%d %H:%M"


def readrecords(inputfile):
    with open(inputfile) as f:
        lines = [l.strip() for l in f]
    records = []
    for l in lines:
        m = recordpattern.match(l)
        records.append(
            (datetime.datetime.strptime(m.group(1), timeformat), m.group(2)))
    return sorted(records, key=lambda r: r[0])


if __name__ == "__main__":
    records = readrecords("input")
    guards = defaultdict(lambda: defaultdict(int))
    guard = None
    for r in records:
        action = r[1]
        m = guardbeginsshiftpattern.match(action)
        if m:
            guard = int(m.group(1))
        if action == "falls asleep":
            begin = r[0]
        elif action == "wakes up":
            assert begin is not None
            end = r[0]
            for m in range(begin.minute, end.minute):
                guards[guard][m] += 1
    max_ = float("-inf")
    for g in guards:
        for m in guards[guard]:
            if guards[g][m] > max_:
                max_ = guards[g][m]
                guard = g
                minute = m
    print(guard, minute, guard * minute)

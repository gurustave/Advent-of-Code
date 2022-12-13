import sys

elves = [0]

for line in sys.stdin:
    if line.strip() == "":
        elves.append(0)
    else:
        elves[-1]+=int(line.strip())

print(max(elves))

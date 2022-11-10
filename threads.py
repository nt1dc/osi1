from tabulate import tabulate

file = open("threads_stat.txt")
threads = {}
for line in file:
    if line.startswith("  ") and not line.startswith("  PID"):
        ln = line.split()
        if not threads.__contains__(ln[0]):
            threads[ln[0]] = []
        threads[ln[0]].append(ln[7])
colums = ["th number", "state"]
rows = []
for key in threads:
    row = [key, threads.get(key)]
    rows.append(row)
print(rows)
with open('threads.txt', 'w') as f:
    print(tabulate(rows, colums), file=f)

from matplotlib import pyplot as plt

file = open("iostat.txt")
a = {}

attr = ["tps", "MB_read_s", "MB_wrtn_s", "MB_dscd_s", "MB_read", "MB_wrtn", "MB_dscd"]


def addValuesToMup(name, values):
    if not a.__contains__(name):
        a[name] = []
    a.get(name).append(values)


time = list(range(0, 100))
for line in file:

    if line.__contains__("loop0") or line.__contains__("loop1") or line.__contains__("sda") or line.__contains__(
            "sdb") or line.__contains__("sdc") or line.__contains__("sdd"):
        zxc = line.split()
        addValuesToMup(zxc[0], zxc[1:])

zxc = {}
for key in a.keys():
    arr = [[], [], [], [], [], [], []]
    for k in a[key]:
        for i in range(len(attr)):
            arr[i].append(float(k[i].replace(',', '.')))
    zxc[key] = arr

for i in range(len(attr)):
    for key in zxc.keys():
        plt.plot(time, zxc.get(key)[i], label=key + "_" + attr[i])
    plt.legend()
    plt.savefig("io/" + attr[i] + ".png")
    plt.close()

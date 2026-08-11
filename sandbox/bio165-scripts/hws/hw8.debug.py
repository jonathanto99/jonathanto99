# * Script 1
with open("./files/insane.fasta") as file:
    for line in file:
        if line[1] != "S":
            line = line.strip()
            print(line[2])
            if line[0] == ">":
                print(line)
            else:
                line = line.replace(" ", "")
                print(line)
        else:
            line.strip()
            print(line)

# * Script 2
str = "ATGG"
str2 = ""
count = 0
while len(str) > 1:
    str  = str[1:]
    str = str[::-1]
    str2 += str[-1]
    count = 1
    if str[0] == "A":
        print(count)
        count += 2
    elif str[0] == "C":
        print(count)
        count = "Now I'm a string"
    else:
        count += 2
print(str)
print(str2)
print(count)

# * Script 3
print("start")
with open("./files/input.txt") as inf:
    list1 = []
    list2 = []
    count = 0
    for item in inf:
        item.strip()
        if count % 2 == 0:
            list1.append(item)
            count -= 2
        else:
            list2.append(item)
            print("count")
        count += 4
    list2 = list1[::]
    list1 = list1[::-2]
    list2 = list2[::2]
    list2[0] = list2[0][:-1]
    list2[1] = list2[1][:-1]
    list2[2] = list2[2][:-1]
    print("done")

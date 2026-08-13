import math

print()
user_num = int(input("What number would you choose? "))


largest_num = user_num * user_num
digits = int(math.log10(largest_num)) + 3
# digits = len(str(largest_num))
range_scope = user_num + 1

#repeat this process
for row_num in range(1, range_scope):
    for col_num in range(1, range_scope):
        fin_num = row_num * col_num
        print(f"{fin_num:{digits}}", end = "")
    print()

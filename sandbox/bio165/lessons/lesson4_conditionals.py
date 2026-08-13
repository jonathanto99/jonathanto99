import sys

# Problem 1:
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

ordered_list = sorted([num1, num2, num3], reverse = True)
print(*ordered_list)

# Problem 2:
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a >= 70:
    print("Person 1 should eat.")
elif 51 <= a <= 69:
    print("Person 1 should consider eating.")
elif a < 51:
    print("Person 1 should not eat.")
    
if b >= 70:
    print("Person 2 should eat.")
elif 51 <= b <= 69:
    print("Person 2 should consider eating.")
elif b < 51:
    print("Person 2 should not eat.")

if c >= 70:
    print("Person 3 should eat.")
elif 51 <= c <= 69:
    print("Person 3 should consider eating.")
elif c < 51:
    print("Person 3 should not eat.")
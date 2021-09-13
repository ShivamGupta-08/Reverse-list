n = int(input("Number items in list\n"))
a = []
for i in range(n):

    list1 = input("Enter list items\n")
    a.append(list1)
print(f"My First reversed list of {a} is {list(reversed(a))}")
print(f"My Second reversed list of {a} is {a[::-1]}")
b = len(a) - 1
reverse3 = a[:]
for r in range(len(a)//2):
    reverse3[r], reverse3[len(reverse3) -r -1] = reverse3[len(reverse3) -r -1], reverse3[r]

print(f"My Third reversed list of {a} is {reverse3}")
if list(reversed(a)) == a[::-1] and a[::-1] == reverse3:
    print("All three methods give same result\n")

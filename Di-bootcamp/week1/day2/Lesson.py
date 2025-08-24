list1 = [5, 10, 15, 20, 25, 50, 20]

# Find the index of the first occurrence of 20
if 20 in list1:
    index = list1.index(20)
    list1[index] = 200

print(list1)

a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a, b, c, d)

# num = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")

i = 1
while i <= 10:
    print(i)
    i += 1
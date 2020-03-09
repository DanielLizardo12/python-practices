
# Logocal Operators

# And
# (1 > 2) and (2 < 3)

# Or
# (1 > 2) or (2 < 3)

# multiple logical Operators

if 1<2:
    print("First Block")
    if 20 < 3:
        print("Second Block")


if 1 > 2:
    print("Hello")
elif 3 == 3:
    print("Elif Ran")
else:
    print("last")


# For Loops

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {"sam":1,"frank":2,"dan":3}

for item in d:
    print(item, "[" , d[item], "]")


# Tupples

my_pairs = [(1,2), (3,4), (5,6)]

for (tup1, tup2) in my_pairs: # Unpack tupples
    print(tup1)
    print(tup2)



# While loops

i = 1

while i < 5:
    print("i is: {}".format(i))
    i += 1


for item in range(10):
    print(item)



# List Comprehention

x = [1,2,3,4]

out = []

# for num in x:
#     out.append(num**2)
#
# print(out)

# or

out = [num**2 for num in x]

print(out)

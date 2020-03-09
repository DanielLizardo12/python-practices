# Booleans
# True
# False
# 1
# 0

# Tuples
t =  (1,2,3)
print(t[0])

t = ("a", True, 123)
print(t) # Tuples are like lists but they are unmutable


# Sets
x = set()

x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
x.add(4)
x.add(4) # It can only take unique values so if we enter a lot of 4's it will only store 1
print(x) # It's unordered when printed


converted = set([1,1,1,1,1,2,2,22,2,3,3,3])
print(converted)

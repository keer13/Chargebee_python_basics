# --------------------------------
# FUNDAMENTAL DATA TYPES
# --------------------------------
# int, float, string, complex, bool

a = 7
b = 1.1
c = "keer"
d = 5 + 13j
e = True

print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))


# --------------------------------
# COLLECTION DATA TYPES
# --------------------------------
# list, tuple, set, dict

# List
a = ["item1", "item2"]

# Tuple
b = ("item1", "item2")

# Set
c = {"item1", "item2"}

# Dictionary
d = {"key1": "value1", "key2": "value2"}


# --------------------------------
# STRING OPERATIONS
# --------------------------------
a = "keerthana"

print(a[0])        # k
print(a[:4])       # keer
print(a[-5])       # t
print(a[::-1])     # reverse
print(a[4:8])      # than
print(a[::2])      # alternate chars

b = "Bavani Kandhan"

print(b[9:6:-1])   
print(b[-5:-8:-1]) 
print(b[9:-8:-1])  
print(b[-5:6:-1])  


# --------------------------------
# STRIP FUNCTIONS
# --------------------------------
c = "      welcome to python world     "

print(c.strip())   # remove both sides
print(c.rstrip())  # remove right
print(c.lstrip())  # remove left


# --------------------------------
# LIST
# --------------------------------
a = ["briyani", "fried rice", "sambar rice"]
print(type(a))

a[2] = "chicken 65"
print(a)


# --------------------------------
# SET
# --------------------------------
b = {"briyani", "fried rice", "sambar rice"}
print(type(b))

c = {1, 1.1, "i"}
print(type(c))
print(c)


# --------------------------------
# DICTIONARY
# --------------------------------
d = {1: "ravi", 2: "raj"}
print(d)
print(d[1])


# ================================
# NESTED DICTIONARY
# ================================
e = {
    "veg": {"potato": 10, "carrot": 7},
    "fruits": {"apple": 5, "banana": 10}
}

print(e)
print(e["fruits"])


# ================================
# LIST ITERATION
# ================================
k = ["apple", "banana", "mango"]

for i in k:
    print("I love", i)


# ================================
# LOOPS (PASSWORD CHECK)
# ================================
password = "keer07"
limit = 0

while limit < 3:
    enter = input("Enter your password: ")

    if enter == password:
        print("Login successful")
        break
    else:
        print("Try again")
        limit += 1
else:
    print("Attempts finished")


# ================================
# FUNCTION
# ================================
def add(a, b):
    print(a + b)

add(5, 2)



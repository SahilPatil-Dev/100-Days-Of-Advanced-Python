"""
Day 1 – Python Execution & Memory Model
Focus: Objects, references, mutability
"""

# ---------- IMMUTABLE EXAMPLE ----------
def immutable_test(x):
    print("Inside function (before):", x, id(x))
    x = x + 1
    print("Inside function (after): ", x, id(x))


a = 10
print("Before function call:", a, id(a))
immutable_test(a)
print("After function call: ", a, id(a))

print("-" * 50)


# ---------- MUTABLE EXAMPLE ----------
def mutable_test(lst):
    print("Inside function (before):", lst, id(lst))
    lst.append(100)
    print("Inside function (after): ", lst, id(lst))


numbers = [1, 2, 3]
print("Before function call:", numbers, id(numbers))
mutable_test(numbers)
print("After function call: ", numbers, id(numbers))

print("-" * 50)


# ---------- ASSIGNMENT VS COPY ----------
x = [1, 2, 3]
y = x
z = x.copy()

print("x:", x, id(x))
print("y:", y, id(y))
print("z:", z, id(z))

y.append(99)

print("\nAfter modifying y:")
print("x:", x, id(x))
print("y:", y, id(y))
print("z:", z, id(z))

# used to store list of items but unlike lists these cannot be modefied

numbers = (1,2,3)
numbers.count(3)
print(numbers[1])


# Unpacking
coordinates = (1,2,3)

coordinates[0] * coordinates[1] * coordinates[2]  # not so efficient

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]   # this again is not so efficent

x, y, z = coordinates   # line 13,14,15 can be achived with the same result
print(z)


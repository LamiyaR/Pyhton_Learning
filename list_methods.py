numbers = [5, 2, 1, 7, 4, 5, 6, 10 ,10, 10 ,49,40, 299]
numbers.append(20)
print(numbers)


numbers.insert(0, 40)
print(numbers)

numbers.remove(5)
print(numbers)



numbers.pop()
print(numbers)

print(numbers.index(40))


print(50 in numbers)  # this gives a bolean value


print(numbers.count(5))

print(numbers.sort())
numbers.sort()
print(numbers)


numbers.reverse()
print(numbers)


# write a program to remove the duplicate in a list
unique = []
for number in numbers:
    if number not in unique:
        unique.append(numbers)

numbers.clear()
print(numbers)


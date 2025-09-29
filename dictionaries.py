customer = {
    "name": "lamiya rampurwala",
    "age": "22",
    "is_verified": True

}

print(customer["name"])

print(customer.get("birthday"))


#digits to words

phone = input("Phone: ")

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

output = ""
for ch in phone:
     output += digits.get(ch, "!") + " "

print(output)


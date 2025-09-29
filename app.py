"""""
print("Lamiya Rampurawala")
print('o----')
print(' ||||')
print('*' * 10)


price = 10
price = 20 #whole number
rating = 4.9 #flaot point number (basically a deciaml)
name = 'lamiya' #string
is_published= False #boolean


print(price)
print(name)
print(is_published)

#we check in a paitent name john smith. hes 20 years old and is a new patient.

full_name = "john smith"
age = 20
is_new = True

#new code
name = input('What is your name? ')
color = input('Whats your favourite color? ')


print('Hi ' + name)
print(name + ' likes ' + color)



#ask the year i was born in and calculate whats my current age
birth_year= input('birth year: ')
print(type(birth_year))
print(type(age))
age = 2025 - int(birth_year)
print(age)



#ask user for weigth in pounds and convert in to kilograms and print on the terminal
weight_in_pounds = float(input("what your weight in pounds? "))
weight_in_kilograms = float(weight_in_pounds * 0.453592)
print('weight in kg is ' + str(weight_in_kilograms))



weight_lbs = input("what your weight in lbs? ")
weight_kg = float(weight_lbs) * 0.453592
print('weight in kg is ' + str(weight_kg))





course = ''' 
 Hi Lamiya this is our first code to you
 
 Thankyou for your support
 Team,

 '''
print(course)

course = 'Pyhton for Beginners'
print(course[0])
course = 'Pyhton for Beginners'
print(course[-6])

course = 'Pyhton for Beginners'
print(course[0:3])

another = course[:] #copies the whole string
print(another)


name = 'Jennifer'
print(name[1:-1])


first = 'lamiya'
last = 'rampurawala'

message = first + ' [' + last + '] ' 'is a coder '
msg = f'{first} [{last}] is a coder' #formatted string
print(message)
print(msg)

course = 'Python for Beginners '
print(len(course))
print(course)
print(course.upper())
print(course.lower())

print(course.find('P'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course) #gives boolean value anwser

print(course.title())


print(10 + 3)
print(10/3)
print(10//3) #this gives an interger anwser no remainder as such...it divides but gives no remainder
print(10%3)  # remainer for the division is returned
print(10**3) # to the power like 10 to the power of 3

x = 10

x = x + 3
print(x)

x += 3
print(x)

x -= 3
print(x)

#this follows BODMAS

import math
print(math.ceil(2.9))
print(math.floor(2.9))
x = 2.9
print(round(x))
print(abs(-2.9)) # always returns a positive number


input("whats the weather like? ")

is_hot = True
is_cold = True

if is_hot:
    print('Its a hot day')
    print('Drink plenty of water')
elif is_cold:
    print('Its a cold day')
    print('Wear warm clothes')
else:
    print('Its a lovely day')

print('Enjoy your day')



print('Price of house is 10M')

has_Good_credit = True
has_Bad_credit = False

if has_Good_credit:
    print('they need to put down 10%')
else:
    print('they need to put down 20%')


price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
    print(f'They need to put down ${down_payment}')
else:
    down_payment =  0.2 * price
    print(f' They need to put down ${down_payment}')

#if an applicant has hgh income and good credit eligiable for laon..... both conditions must be true
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print('eligible for loan1')

#if an applicant has hgh income or good credit eligiable for laon.......atleast one condition must be true
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print('eligible for loan2')

#if applicant has good credit AND doenst have a criminal record
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('eligible for loan3')

# AND: Both true
# OR: at least one
# NOT:


#if temperature is greater than 30
    #its a hot day
#otherwise if its less than 10
    #its a cold day
#otherwise
    #its neither hot nor cold

temperature = 35
if temperature > 30:
    print('its a hot day')
else:
    print('its not a hot day')

#if name is less than 3 characters long
#    name must be atleast 3 characters
#otherwise if its more than 50 characters long
#    name can be a maximum of 50 characters
#otherwise
#  name looks good

name = input('please enter your name   ')
name_len = len(name)

if name_len <= 3:
    print('name must be atleast 3 characters ')
elif name_len >= 50:
    print('name can be a maximum of 50 characters ')
else:
    print(' name looks good ')


weight = int (input('Enter your weight  '))
old_unit = input('lbs(L) or kgs(K)  ')
lower_case = old_unit.lower()
new_weight_kg = weight * 0.45
new_weight_lbs = weight / 0.45

if lower_case == 'l':
    print(f'weight in kgs is {new_weight_kg}' )
elif lower_case =='k':
    print(f'weight in lbs is {new_weight_lbs}' )
else:
    print('entered wrong unit')


i = 1
while i <= 5:
    print(i)
    i = i + 1
print("done")

i = 1
while i <= 5:
    print(' * ' * i)
    i = i + 1

print("done")

secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else:
    print('loseee')


command = ""

started = False
stopped = False

while True:

    command = input("> ").lower()
    if command == 'help':
        print("""
"""start - to start the car
stop - to stop the car
quit - to exit
       """ """)

    elif command == 'start':
        if started:
            print('CAR IS ALREADY STARTED!!!!!!!')
        else:
            started = True
            print('Car started......ready to go!!!')

    elif command == 'stop':
        if stopped:
            print('CAR IS ALREADY STOPPED!!!!!!!!!!!!!!!!!')
        else:
            stopped = True
            print('car stopped.')

    elif command == 'quit':
        break

    else:
        print('I dont understand.')



for item in 'python':
    print(item)

for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(item)

for item in range(10):
    print(item)

for item in range(5, 10, 2):
    print(item)

#calculate total cost of shopping items in the imaginary cart

prices = [10, 20, 30]
sum = 0

for price in prices:
    sum += price
print(f'sum: {sum}' )


#NESTED LOOP

for x in range(4):
    for y in range(4):
        print(f'({x}, {y})')
"""





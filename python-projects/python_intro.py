print("Hello World")

# Loops 
counter = 0 
while counter < 10 :
    print(counter)
    counter += 1

nums = [10,20,30,40,50]
for i in range(2,len(nums)):
    print(nums[i])

for num in nums:
    num += 5
    print(num)
print(nums)

for i, val in enumerate(nums):
    print ("i is ", i, " and val is ", val)

dogs = ["bulldogs", "frenchies", "terriers", "spaniels", "huskys"]

for i in range(2, len(dogs)):
    print(dogs[i])

for dog in dogs:
    dog += " are a type of dog"
    print(dog)
print(dogs)

for i, val in enumerate(dogs):
    print("i is ", i, "and val is ", val)

nums = [4,8,12,16,20,24,28,32]
sum_nums = 0
for val in nums: 
    sum_nums += val
print("The sum is", sum_nums)
print(f"The sum is {sum_nums}")

def hello(name = "friend"):
    print("hello!", name)
hello("Isla")
hello()

name = 'Amaya Raye'
title = "Rephactor Python Practice"

print('He said "Hi" to his frend.')
print("She's a great dancer.")

sentence = " Without " + name + ' there would be no ' + title + "."
print(sentence)

fname = 'Amaya'
lname = 'Raye'

fullname = fname + " "  + lname
print(fullname)

f_initial = fname[0]
l_initial = lname[0]
print(f_initial)
print(l_initial)

last_char = fname[-1]
print(last_char)

title = 'Rephactor Python Practice'
print(len(title))

print('Amaya' * 7)

ampersand = 8 * '&'
print(ampersand)

great_student = 'Amaya Raye'
if great_student == 'Amaya Raye':
    print('Academic Successful Semester')

name = 'Amaya'
name_in_uppercase = name.upper()
name_in_lowercase = name.lower()
print(name_in_uppercase)
print(name_in_lowercase)

# Slicing Strings 

course = "Platform Computing"
platform = course[0:8] #/Starts at zero even if not stated
print(platform)
computing = course[9:18]   #Will continue to end even if not specified
print(computing)

print(platform, computing)
course1=course[:]  # Copies a string 

# Excercise 
swap = [0,3,8,5,4]
#Output [0,3,4,5,8]

temp = swap[2]
swap[2] = swap[4]
swap[4] = temp
print(swap)


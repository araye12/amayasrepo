num = int(input("Enter a number: "))
print(num)
num += 10
print(num)

try:
    num = int(input("Enter a number: "))
    num += 10 
except:
    print("You did not enter a number.")

print("continue")

with open("movies.txt") as file:
    for line in file:
        line=line.strip()
        print(line)

print()

with open('heights.txt') as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        print(tokens)

print()

with open('heights.txt') as file:
    for line in file:
        line = line.split()
        print(line)
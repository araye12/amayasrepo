file = open("all10tests.txt", 'r')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
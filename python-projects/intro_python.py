print("hello world!")

# this is a comment 

'''
This is a line 
This is another line
'''

x = 10
print(x)
y = 10.5
x = "hello"
print(x)

# math operations 
x = 100
y = 10 
result = x//y
result = int(x/y)
print(result)

# built in functions
min_val = min(10,1)
print(min_val)
raised = pow(2,4)
print(raised)
raised = 2**4

# if statements 
x = -1 
if x < 0:
   x += 10
   y = 15
print("this will execute outside of if statement")

if x < 10:
    x += 1
elif x > 10:
    x-=1
else:
    x=100

if x < 0 and y <0:
    x+=1
    y+=1

# loops 
count=0
while count < 10:
    count += 1
    print(count)

alist = [1,2,3,4,5]
for cat in alist:
    print(cat,end="")


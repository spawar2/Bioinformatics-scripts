#sum

#there's a python function sum
# we'll use that.
# adding two lists makes a list with all the elements of both.
# set removes the duplicates
# sum sums them.

print sum( set( range(0,1000,3)+range(0,1000,5)))

a = 0
for i in range(0,1000):
    if i%3 == 0 :
        a += i
    if i %5 == 0 and not i %3 == 0:
        a += i
print a


#most of you did

a = 0
for i in range(0,1000,3):
    a += i
for i in range(0,1000,5):
    if i %3 != 0:
        a += i
print a

a = 0
for i in range(0,1000,3):
    a += i
for i in range(0,1000,5):
    a += i
for i in range(0,1000,15): # 15 is the LCM of 3,5
    a -= i
print a

# this is probably the fastest (no duplicate checking and all built in)
a = sum(range(0,1000,3))+sum(range(0,1000,5))-sum(range(0,1000,15))
print a

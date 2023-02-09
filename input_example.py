# calculate if a year is a leap year.
# leap years are divisible by 4 and
# not a century (Julian)
# except if divisible by 400

#i'm a mensch
try:
   year =  int(raw_input("Enter the year "))
except:
    print("PLEASE ENTER A YEAR")
    exit(-1)

if year %4 != 0 or (year %400 != 0 and year %100 == 0):
    print( "Not a leap year")
else:
    print( "A leap year")

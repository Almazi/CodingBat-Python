/'''
The parameter weekday is true if it is a weekday,
and the parameter vacation is true if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return true if we sleep in.

sleepIn(false, false) → true
sleepIn(true, false) → false
sleepIn(false, true) → true
'''/

def sleep_in(weekday, vacation):
  return False if (weekday == True and vacation == False) else True

/'''
monkeyTrouble
We have two monkeys, a and b, and the parameters a_smile and b_smile
indicate if each is smiling. We are in trouble if they are both smiling
or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
'''/

def monkey_trouble(a_smile, b_smile):
  return True if (not a_smile and not b_smile) or (a_smile and b_smile) else False


/'''
sumDouble
Given two int values, return their sum. Unless the two values are the same,
then return double their sum.

sumDouble(1, 2) → 3
sumDouble(3, 2) → 5
sumDouble(2, 2) → 8
'''/

def sum_double(a, b):
  return a+b if a != b else 2*(a+b)

/'''
diff21
Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
'''/

def diff21(n):
  return -1*(n-21) if n -21 <= 0 else 2*(n-21)

/'''
parrotTrouble
We have a loud talking parrot. The "hour" parameter is the current hour
time in the range 0..23. We are in trouble if the parrot is talking and
the hour is before 7 or after 20. Return true if we are in trouble.

parrotTrouble(true, 6) → true
parrotTrouble(true, 7) → false
parrotTrouble(false, 6) → false
'''/

def parrot_trouble(talking, hour):
  return True if (talking == True and (hour < 7 or hour > 20)) else False



/'''
makes10
Given 2 ints, a and b, return true if one if them is 10 or if their sum is 10.

makes10(9, 10) → true
makes10(9, 9) → false
makes10(1, 9) → true
'''/
def makes10(a, b):
  return True if a == 10 or b == 10 or a + b == 10 else False

/'''
near_hundred
Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
'''/
def near_hundred(n):
  return True if (abs(n-100) <= 10 or abs(n-200) <= 10) else False

/'''
posNeg
Given 2 int values, return true if one is negative and one is positive.
Except if the parameter "negative" is true,
then return true only if both are negative.

posNeg(1, -1, false) → true
posNeg(-1, 1, false) → true
posNeg(-4, -5, true) → true
'''/

def pos_neg(a, b, negative):
  if negative is False:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))
  elif (negative is True):
    return (a < 0 and b < 0)
#or
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b > 0) or (a > 0 and b < 0))



/'''

'''/

/'''

'''/

/'''

'''/

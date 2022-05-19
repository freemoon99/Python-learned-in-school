#myCalculator.py

#factorial function:
def factorial(n):
    try:
        n=int(n)    #cast the string argument to an integer
    except:
        return "--> Error!"
    # '0'is special:
    if n == 0:
        return 1
    #back out if too large:
    if n > 40:
        return "--> Answer will not fit on screen!"
    #for minus value:
    if n < 0:
        return "--> Error!"
    #algorithm for factorial:
    ans=n #set initial valuse of answer before loop
    while n>1:
        ans=ans*(n-1)
        n=n-1
    return ans
#convert to roman numerals function:
def to_roman(n):
    try:
        n = int(n)
    except:
        return "--> Error!"
    
    #argument larger than 4999:
    if n > 4999:
        return "--> Over the range."
    
    #tuple and dictionary generatrion:
    numberBreaks = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
    letters = {
1000 : "M", 900 : "CM", 500 : "D", 400 : "CD", 100 : "C", 90 : "XC", 50 : "L", 40 : "XL",
10 : "X", 9 : "IX", 5 : "V", 4 : "IV",
1 : "I"  }
    #algorithm start:
    result = ""
    for value in numberBreaks:
        while n >= value:
            result = result+letters[value]
            n = n-value
    return result
#convert base 10 numbers to binary function:
def to_binary(n):
    try:
        n = int(n)
        return bin(n)[2:]
    except:
        return "--> Error!"
#convert binaey to decimal function:
def from_binary(n):
    try:
        return int(n,2)
    except:
        return "--> Error!"

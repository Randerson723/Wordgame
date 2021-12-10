#message = input("What kind of subaru would you like?")
#print("let me see if I can find you a subaru")

#number = input("How many guests will be in your party?")
#number = int(number)

#if number >= 8:
    #print(" Please have a seat, we will call you momentarily")
#else:
    #print("Right this way to your table7")

number = input(" Enter a number and I will tell you if it is divisible by 10")
number = int(number)

if number % 10 == 0:
    print("The number" + str(number) + "is divisible by 10")
else:
    print("The number" + str(number) + " is not divisible by 10")

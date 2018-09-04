#To make mario pyramid of hash between length 0-23

while True:
    #Check for integer
    try:
        length = int(input('Enter a number between 0-23:'))
    except:
        print("Please enter a integer")
    #Check for length
    if length < 0 or length > 23:
        print('Please enter a number between 0 - 23')
        continue
    #Creating pyramid
    for i in range(length):
        print(('#' * (i + 2)).rjust(length+1))
    break
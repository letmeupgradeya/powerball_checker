winner_numbers = [4, 8, 19, 27, 34]
winner_powerball = [10]
numbers = []

print "The winning numbers were %s" %(winner_numbers)
numbers = raw_input("What are your numbers, separated by commas:")
power_ball = raw_input("What is your powerball number:")

numbers = [int(k) for k in numbers.split(',')]

numbers.sort()

print numbers
count = 0

for x in range(0,len(numbers)):
    if numbers[x] == winner_numbers[x]:
        count = count + 1
        print "match"
    else:
        print "not a match"

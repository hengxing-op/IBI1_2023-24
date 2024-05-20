# What does this piece of code do?
# Answer: randomly pick numbers from 1 to 10 for 100 times and add them up to a final random number, and the final random numbers have a average result of 550( because number are randomly chosen from 1 to 10, (1+10)/2*100=550)

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#give the start value 0 to a variable
progress=0

#give the start value 0 to the output variable
total_random_number=0

#start a while loop to repeat the operation 100 times
while progress<100:
	progress+=1
 #randomly pick a number from 1 to 10
	n = randint(1,10)
 #with the while loop, add up the 100 random numbers to get a random result
	total_random_number = total_random_number+n

print(total_random_number)

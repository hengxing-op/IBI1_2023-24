# on day 1, the density is 5%(only use 5 but not 5%, % will be added at last)
day=1
density=5
#the max density is 90%
max_density=90
#because the density is no more than max density,use while loop to check
while density<max_density:
    #if the density is no more than 90%, day turn into the second one
    day+=1
    #double the density
    density=2*density
#when the loop is broken, print which is that day and state the density is more than the max density)
print ("On day",str(day),", the density of culture is over",str(max_density),"%",", so the day",str(day-1), "is the day before the cell density crosses 90%")
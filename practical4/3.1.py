a=40
#define time cost before training
b=36
#define time cost after running only
c=30
#define time cost after running and strength training
d=a-b
# d is improvement from running
e=b-c
# e is improment from running and strength training
if d>e:
    print("	Improvement from running only is greater than that from running and strength training")
else:
    print("Improvement from running and strength training is greater than that from running only")
# compare which improvement is greater
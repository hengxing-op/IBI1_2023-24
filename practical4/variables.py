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
# runing and strength training had a greater effect on the 5 km time

X=1<2
Y=1>2
W= (X or Y) and (not X and Y)
print (W)
# When there are one true and one false, X or Y is true, X and Y is false, (not X and Y) is true, so (X or Y) and (not X and Y) is true, satisfies the requirement.
#When there are two trues, X or Y is true, but (not X and Y) is false, (X or Y) and (not X and Y) is false, satisfies the requirement.
#When there are two falses, X or Y is false, (not X and Y) is true, so () and () is false, satisfy the requirement.
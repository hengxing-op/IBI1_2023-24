X=1<2
Y=1>2
W= (X or Y) and (not X and Y)
print (W)
# When there are one true and one false, X or Y is true, X and Y is false, not X and Y is true, so (X or Y) and (not X and Y) is true, satisfies the condition.
#When there are two trues, X or Y is true, but (not X and Y) is false, (X or Y) and (not X and Y) is false, satisfies the condition.
#When there are two falses, X or Y is false, and (not X and Y)